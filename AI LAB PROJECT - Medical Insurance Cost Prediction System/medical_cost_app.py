import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.set_page_config(
    page_title="Medical Cost Predictor",
    layout="centered"
)

st.title(" Annual Medical Cost Predictor")
st.write("Fill in your details below to get an estimate of your **annual medical cost**.")
st.markdown("---")


@st.cache_resource
def load_model():
    with open("model_medical_cost.pkl", "rb") as f:
        return pickle.load(f)

obj      = load_model()
model    = obj["model"]
features = obj["features"]
encoders = obj["encoders"]


st.subheader("📋 Personal & Health Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=110, value=35, step=1)
    bmi = st.number_input("BMI", min_value=10.0, max_value=70.0, value=25.0, step=0.1,
                          help="Body Mass Index. Normal range is 18.5 – 24.9")
    smoker = st.selectbox("Smoker?", ["No", "Yes"])
    diabetes = st.checkbox("Diabetes")
    hypertension = st.checkbox("Hypertension")
    heart_disease = st.checkbox("Heart Disease")

with col2:
    insurance_type = st.selectbox("Insurance Type", ["Government", "Private"])
    insurance_coverage_pct = st.slider(
        "Insurance Coverage %", min_value=0, max_value=100, value=50,
        help="What percentage of your medical costs does your insurance cover?"
    )
    hospital_admissions = st.slider("Hospital Admissions per Year", 0, 20, 0)
    doctor_visits_per_year = st.slider("Doctor Visits per Year", 0, 30, 2)
    medication_count = st.slider("Number of Regular Medications", 0, 20, 0)
    previous_year_cost = st.number_input(
        "Previous Year Medical Cost ($)", min_value=0, max_value=100000, value=5000, step=100,
        help="How much did you spend on medical costs last year?"
    )

st.markdown("---")


if st.button(" Predict My Annual Medical Cost", use_container_width=True, type="primary"):

    # Encode categoricals using saved encoders
    smoker_enc         = encoders["smoker"].transform([smoker])[0]
    insurance_type_enc = encoders["insurance_type"].transform([insurance_type])[0]

    input_data = {
        "insurance_coverage_pct":  insurance_coverage_pct,
        "hospital_admissions":     hospital_admissions,
        "insurance_type":          insurance_type_enc,
        "medication_count":        medication_count,
        "heart_disease":           int(heart_disease),
        "previous_year_cost":      previous_year_cost,
        "smoker":                  smoker_enc,
        "diabetes":                int(diabetes),
        "hypertension":            int(hypertension),
        "doctor_visits_per_year":  doctor_visits_per_year,
        "bmi":                     bmi,
        "age":                     age,
    }

    input_df   = pd.DataFrame([input_data])[features]
    prediction = max(0, model.predict(input_df)[0])
    monthly    = prediction / 12

    st.success(" Prediction Complete!")
    st.markdown("---")

    r1, r2 = st.columns(2)
    with r1:
        st.metric(" Estimated Annual Cost", f"${prediction:,.2f}")
    with r2:
        st.metric(" Estimated Monthly Cost", f"${monthly:,.2f}")

    # Risk breakdown
    st.markdown("---")
    st.subheader(" Your Risk Factors")

    risk_flags = []
    if smoker == "Yes":         risk_flags.append(" Smoker")
    if heart_disease:           risk_flags.append(" Heart Disease")
    if diabetes:                risk_flags.append(" Diabetes")
    if hypertension:            risk_flags.append(" Hypertension")
    if hospital_admissions > 2: risk_flags.append(f" {hospital_admissions} hospital admissions")
    if bmi > 30:                risk_flags.append(f" BMI {bmi:.1f} (Obese range)")
    if medication_count > 5:    risk_flags.append(f" {medication_count} medications")

    if risk_flags:
        st.warning("Active risk factors: " + "  |  ".join(risk_flags))
    else:
        st.success("No major risk factors detected!")

    st.info(
        " **Disclaimer:** This is a model-based estimate for educational purposes only. "
        "Actual medical costs depend on many factors and vary by provider and location."
    )


st.markdown("---")
st.caption("Made with love by Qasim Ashfaq  |  Used Gradient Boosting Regressor  |  R² Score = 99.25%")
