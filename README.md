# 🏥 AI-Powered Smart Medical Invoice & Insurance Analysis System

An intelligent healthcare billing system that predicts medical treatment costs using Machine Learning, analyzes billing risk, suggests cost-saving measures, and estimates insurance claim approval probability.

This project simulates a **real-world hospital + insurance workflow** using Django and AI-driven logic.

---

## 🚀 Key Features

### 🔹 Smart Cost Prediction (ML-Based)
- Predicts treatment cost using:
  - Patient age
  - Diagnosis
  - Automatically estimated lab tests & medicines
- Uses a trained ML model (no paid APIs)

---

### 🔹 Severity-Based Intelligence
- Supports **Mild / Moderate / Severe** complaints
- Automatically adjusts:
  - Lab test count
  - Medicine count
- Prevents overestimation for small complaints

---

### 🔹 Learning from History (Adaptive AI)
- Learns average treatment patterns from past invoices
- Improves future predictions automatically
- Becomes smarter as more data is added

---

### 🔹 Cost Deviation & Risk Analysis
- Compares predicted cost vs actual billed cost
- Calculates deviation percentage
- Classifies risk:
  - Normal
  - Medium Risk
  - High Risk

---

### 🔹 Smart Cost-Saving Suggestions
- Suggests:
  - Reducing unnecessary lab tests
  - Using generic medicines
  - Reviewing treatment plans for high deviation
- Acts as a **decision-support system**

---

### 🔹 Insurance Claim Probability Estimation
- Estimates:
  - Insurance approved amount
  - Claim approval probability (%)
- Based on:
  - Diagnosis type
  - Billing deviation
- Mimics real insurance company logic

---

### 🔹 Analytics Dashboard
- Displays:
  - Patient age & diagnosis
  - Predicted vs actual cost
  - Risk level & deviation
  - Cost-saving suggestions
  - Insurance approval insights
- Includes Chart.js visualizations

---

## 🧠 Why This Project Is Special

✔ Minimal user input (only age, diagnosis, severity)  
✔ AI-assisted decision making (not manual billing)  
✔ Combines **Healthcare + AI + Insurance** logic  
✔ Real-world, interview-ready project  
✔ No paid APIs used  

---

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS, Bootstrap
- **Charts**: Chart.js
- **Database**: SQLite
- **Version Control**: Git & GitHub

---

## 📂 Project Structure
smart-medical-invoice-system/
│
├── billing/
│ ├── views.py
│ ├── models.py
│ ├── forms.py
│ ├── utils.py
│ ├── constants.py
│ └── templates/
│
├── ml_model/
│ ├── train_model.py
│ ├── predict_cost.py
│ └── model.pkl
│
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md

### System Automatically:
- Estimates labs & medicines
- Predicts cost
- Simulates real billing
- Flags overbilling risk
- Suggests cost optimizations
- Estimates insurance approval

---

## 🧪 Sample Input
Age: 45
Diagnosis: Cardiac
Severity: Mild
## 📊 Sample Output

- Predicted Cost: ₹2893
- Actual Cost: ₹3963
- Deviation: 36.99%
- Risk Level: High
- Insurance Approval Probability: 50%

---

## 🧑‍⚕️ Real-World Use Cases

- Hospitals & clinics
- Insurance companies
- Healthcare startups
- Medical auditing & compliance systems

---

## 🎤 Interview-Ready Summary

> Built an AI-powered medical billing system that predicts treatment costs, learns from historical data, analyzes billing risk, recommends cost optimizations, and estimates insurance claim approval probability.

---

## 📌 Future Enhancements

- Role-based access (Doctor / Admin)
- PDF invoice & insurance reports
- Deployment on cloud (AWS / Render)
- More advanced ML models

---

## 👩‍💻 Author

**Menaka Manavalan**  
AI & Django Developer  
GitHub: https://github.com/menaka212

---

⭐ If you find this project useful, give it a star!
