import pickle
import pandas as pd
import os

# Load model once
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(CURRENT_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict_treatment_cost(age, diagnosis, medicine_count, lab_test_count, consultation_fee):
    """
    Returns predicted treatment cost
    """

    input_data = pd.DataFrame([{
        "age": age,
        "diagnosis": diagnosis,   # already encoded
        "medicine_count": medicine_count,
        "lab_test_count": lab_test_count,
        "consultation_fee": consultation_fee
    }])

    prediction = model.predict(input_data)
    return int(prediction[0])
