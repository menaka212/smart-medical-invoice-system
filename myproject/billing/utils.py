def generate_invoice_summary(diagnosis, medicine_count, lab_test_count):
    summary = f"Patient treated for {diagnosis}. "

    if medicine_count > 0:
        summary += f"{medicine_count} medicines prescribed. "

    if lab_test_count > 0:
        summary += f"{lab_test_count} lab tests conducted. "

    summary += "Invoice generated automatically using AI-based cost prediction."

    return summary
def analyze_cost_risk(predicted, actual):
    if predicted == 0:
        return "Unknown", 0

    deviation = ((actual - predicted) / predicted) * 100

    if deviation <= 10:
        return "Normal", deviation
    elif deviation <= 25:
        return "Medium Risk", deviation
    else:
        return "High Risk", deviation
def generate_cost_saving_suggestions(
    medicine_count,
    lab_test_count,
    predicted_cost,
    actual_cost
):
    suggestions = []

    # Suggest reducing lab tests
    if lab_test_count > 2:
        suggestions.append(
            f"Reduce {lab_test_count - 2} lab test(s) to save approx ₹{(lab_test_count - 2) * 800}"
        )

    # Suggest generic medicines
    if medicine_count > 3:
        suggestions.append(
            "Consider generic medicines to save approx ₹500–₹1000"
        )

    # High cost deviation warning
    if predicted_cost > 0:
        deviation = ((actual_cost - predicted_cost) / predicted_cost) * 100
        if deviation > 25:
            suggestions.append(
                "High cost deviation detected — review treatment plan"
            )

    if not suggestions:
        suggestions.append("No major cost-saving opportunities detected")

    return suggestions
from django.db.models import Avg
from .models import Invoice

def learn_from_history(diagnosis):
    """
    Learns average lab tests & medicines from past invoices
    """
    records = Invoice.objects.filter(
        appointment__diagnosis=diagnosis
    )

    if records.count() < 3:
        return None  # Not enough data to learn

    avg_labs = records.aggregate(avg=Avg("lab_test_count"))["avg"]
    avg_meds = records.aggregate(avg=Avg("medicine_count"))["avg"]

    return {
        "lab_tests": round(avg_labs),
        "medicines": round(avg_meds)
    }
def estimate_insurance_claim(diagnosis, total_cost, deviation):
    """
    Estimates insurance coverage & approval probability
    """

    base_coverage = {
        "Cardiac": 0.8,
        "Neurology": 0.75,
        "Orthopedic": 0.7,
        "Diabetes": 0.65,
        "General": 0.5
    }

    coverage_rate = base_coverage.get(diagnosis, 0.5)

    # Reduce approval if deviation is high
    if deviation > 25:
        approval_probability = 0.5
    elif deviation > 10:
        approval_probability = 0.7
    else:
        approval_probability = 0.9

    approved_amount = int(total_cost * coverage_rate)

    return {
        "approved_amount": approved_amount,
        "approval_probability": int(approval_probability * 100)
    }
def apply_severity_adjustment(lab_tests, medicines, severity):
    if severity == "Mild":
        lab_tests = max(1, lab_tests - 2)
        medicines = max(1, medicines - 1)

    elif severity == "Severe":
        lab_tests += 2
        medicines += 2

    return lab_tests, medicines
