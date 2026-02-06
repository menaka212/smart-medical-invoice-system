DIAGNOSIS_CHOICES = [
    ("Cardiac", "Cardiac"),
    ("Diabetes", "Diabetes"),
    ("Orthopedic", "Orthopedic"),
    ("General", "General"),
    ("Neurology", "Neurology"),
]

# MUST match LabelEncoder order used in training
DIAGNOSIS_ENCODING = {
    "Cardiac": 0,
    "Diabetes": 1,
    "General": 2,
    "Neurology": 3,
    "Orthopedic": 4,
}
DIAGNOSIS_DEFAULTS = {
    "Cardiac": {
        "lab_tests": 4,
        "medicines": 5,
        "consultation_fee": 700
    },
    "Diabetes": {
        "lab_tests": 3,
        "medicines": 4,
        "consultation_fee": 500
    },
    "Orthopedic": {
        "lab_tests": 2,
        "medicines": 3,
        "consultation_fee": 600
    },
    "General": {
        "lab_tests": 1,
        "medicines": 2,
        "consultation_fee": 300
    },
    "Neurology": {
        "lab_tests": 5,
        "medicines": 6,
        "consultation_fee": 800
    }
}
