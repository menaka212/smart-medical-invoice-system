from django.shortcuts import render, redirect
from django.db.models import Sum
import random
from .utils import estimate_insurance_claim
from .utils import apply_severity_adjustment
from .forms import CostPredictionForm
from .models import Patient, Appointment, Invoice
from ml_model.predict_cost import predict_treatment_cost

from .constants import DIAGNOSIS_ENCODING, DIAGNOSIS_DEFAULTS
from .utils import (
    generate_invoice_summary,
    analyze_cost_risk,
    generate_cost_saving_suggestions,
    learn_from_history
)

# -------------------------------
# HOME VIEW
# -------------------------------
def home_view(request):
    return redirect("predict_cost")


# -------------------------------
# PREDICT COST VIEW
# -------------------------------
def predict_cost_view(request):
    predicted_cost = None
    invoice_summary = None

    if request.method == "POST":
        form = CostPredictionForm(request.POST)

        if form.is_valid():
            age = form.cleaned_data["age"]
            diagnosis_text = form.cleaned_data["diagnosis"]
            severity = form.cleaned_data["severity"]
            # -------------------------------
            # LEARN FROM HISTORY (AI ADAPTATION)
            # -------------------------------
            learned = learn_from_history(diagnosis_text)

            if learned:
                medicine_count = learned["medicines"]
                lab_test_count = learned["lab_tests"]
            else:
                defaults = DIAGNOSIS_DEFAULTS[diagnosis_text]
                medicine_count = defaults["medicines"]
                lab_test_count = defaults["lab_tests"]
            lab_test_count, medicine_count = apply_severity_adjustment(
                lab_test_count,
                medicine_count,
                severity
            )
            consultation_fee = DIAGNOSIS_DEFAULTS[diagnosis_text]["consultation_fee"]

            # Encode diagnosis for ML
            diagnosis_encoded = DIAGNOSIS_ENCODING[diagnosis_text]

            # -------------------------------
            # ML COST PREDICTION
            # -------------------------------
            predicted_cost = predict_treatment_cost(
                age=age,
                diagnosis=diagnosis_encoded,
                medicine_count=medicine_count,
                lab_test_count=lab_test_count,
                consultation_fee=consultation_fee,
            )

            # -------------------------------
            # SIMULATE REAL-WORLD ACTUAL COST
            # -------------------------------
            variation_percentage = random.randint(10, 40)
            actual_cost = int(
                predicted_cost + (predicted_cost * variation_percentage / 100)
            )

            # -------------------------------
            # DATABASE SAVE
            # -------------------------------
            patient = Patient.objects.create(
                name="Test Patient",
                age=age,
                gender="Male"
            )

            appointment = Appointment.objects.create(
                patient=patient,
                doctor_name="Dr. AI",
                diagnosis=diagnosis_text,
                consultation_fee=consultation_fee
            )

            Invoice.objects.create(
                appointment=appointment,
                medicine_count=medicine_count,
                lab_test_count=lab_test_count,
                predicted_cost=predicted_cost,
                total_cost=actual_cost
            )

            invoice_summary = generate_invoice_summary(
                diagnosis_text,
                medicine_count,
                lab_test_count
            )

    else:
        form = CostPredictionForm()

    return render(request, "billing/predict_cost.html", {
        "form": form,
        "predicted_cost": predicted_cost,
        "invoice_summary": invoice_summary
    })


# -------------------------------
# DASHBOARD VIEW
# -------------------------------
def dashboard_view(request):
    invoices = Invoice.objects.select_related(
        "appointment", "appointment__patient"
    )

    invoice_data = []

    for inv in invoices:
        risk_level, deviation = analyze_cost_risk(
            inv.predicted_cost,
            inv.total_cost
        )

        suggestions = generate_cost_saving_suggestions(
            medicine_count=inv.medicine_count,
            lab_test_count=inv.lab_test_count,
            predicted_cost=inv.predicted_cost,
            actual_cost=inv.total_cost
        )
        insurance = estimate_insurance_claim(
            diagnosis=inv.appointment.diagnosis,
            total_cost=inv.total_cost,
            deviation=deviation
        )
        invoice_data.append({
            "invoice": inv,
            "age":inv.appointment.patient.age,
            "risk": risk_level,
            "deviation": round(deviation, 2),
            "suggestions": suggestions,
            "insurance": insurance
        })

    total_revenue = Invoice.objects.aggregate(
        total=Sum("total_cost")
    )["total"] or 0

    context = {
        "invoice_data": invoice_data,
        "total_revenue": total_revenue,
        "predicted_costs": [i.predicted_cost for i in invoices],
        "actual_costs": [i.total_cost for i in invoices],
        "patient_names": [
            i.appointment.patient.name for i in invoices
        ],
    }

    return render(request, "billing/dashboard.html", context)
