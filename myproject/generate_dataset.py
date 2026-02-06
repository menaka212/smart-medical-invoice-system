import pandas as pd
import random

records = []

diagnoses = ["Cardiac", "Diabetes", "Orthopedic", "General", "Neurology"]
consultation_fees = [300, 500, 700]

for _ in range(300):
    age = random.randint(1, 80)
    diagnosis = random.choice(diagnoses)
    medicine_count = random.randint(1, 6)
    lab_test_count = random.randint(0, 4)
    consultation_fee = random.choice(consultation_fees)

    medicine_cost = medicine_count * random.randint(200, 500)
    lab_cost = lab_test_count * random.randint(600, 1200)

    total_cost = medicine_cost + lab_cost + consultation_fee

    records.append([
        age,
        diagnosis,
        medicine_count,
        lab_test_count,
        consultation_fee,
        total_cost
    ])

columns = [
    "age",
    "diagnosis",
    "medicine_count",
    "lab_test_count",
    "consultation_fee",
    "total_cost"
]

df = pd.DataFrame(records, columns=columns)

df.to_csv("dataset/medical_billing_dataset.csv", index=False)

print("✅ Dataset generated successfully!")
