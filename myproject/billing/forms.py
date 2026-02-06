from django import forms
from .constants import DIAGNOSIS_CHOICES
from django import forms

SEVERITY_CHOICES = [
    ("Mild", "Mild"),
    ("Moderate", "Moderate"),
    ("Severe", "Severe"),
]

class CostPredictionForm(forms.Form):
    age = forms.IntegerField(min_value=1, max_value=100)
    diagnosis = forms.ChoiceField(choices=[
        ("Cardiac", "Cardiac"),
        ("Diabetes", "Diabetes"),
        ("Orthopedic", "Orthopedic"),
        ("General", "General"),
        ("Neurology", "Neurology"),
    ])
    severity = forms.ChoiceField(choices=SEVERITY_CHOICES)


