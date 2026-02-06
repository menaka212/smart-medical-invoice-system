import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "dataset", "medical_billing_dataset.csv")

data = pd.read_csv(data_path)

encoder = LabelEncoder()
data['diagnosis'] = encoder.fit_transform(data['diagnosis'])

X = data[['age', 'diagnosis', 'medicine_count', 'lab_test_count', 'consultation_fee']]
y = data['total_cost']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor()
model.fit(X_train, y_train)

with open(os.path.join(os.path.dirname(__file__), "model.pkl"), "wb") as f:
    pickle.dump(model, f)

print("✅ ML model trained and saved successfully!")
