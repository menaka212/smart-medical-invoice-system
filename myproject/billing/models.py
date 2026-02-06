from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    consultation_fee = models.FloatField()
    appointment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.diagnosis}"


class Invoice(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    medicine_count = models.IntegerField()
    lab_test_count = models.IntegerField()
    predicted_cost = models.FloatField()
    total_cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for {self.appointment.patient.name}"
