#  Medical Cost Prediction using Machine Learning

A machine learning project that predicts **annual medical expenses** based on personal health, lifestyle, and healthcare usage data. The system is deployed using a **Streamlit web application** for real-time interaction.

---

##  Project Overview

This project builds a regression model to estimate medical costs using features such as age, BMI, medical conditions, insurance details, and past healthcare expenses.

- Model: Gradient Boosting Regressor  
- Deployment: Streamlit Web App  
- Goal: Provide a simple, data-driven way to estimate healthcare costs and identify risk factors  

---

##  Features

- Predict **Annual Medical Cost**
- Calculate **Monthly Cost Estimate**
- Identify **Health Risk Factors**
- Interactive **Web UI using Streamlit**
- Real-time predictions

---

##  Input Features

- Age  
- BMI (Body Mass Index)  
- Smoking Status  
- Diabetes  
- Hypertension  
- Heart Disease  
- Insurance Type  
- Insurance Coverage (%)  
- Hospital Admissions per Year  
- Doctor Visits per Year  
- Number of Medications  
- Previous Year Medical Cost  

---

##  Output

- Estimated Annual Medical Cost  
- Estimated Monthly Medical Cost  
- Highlighted Risk Factors  

---

##  Machine Learning Model

- **Algorithm:** Gradient Boosting Regressor  
- Handles:
  - Non-linear relationships  
  - Feature interactions  
  - Outliers better than linear models  

---

##  Model Performance

- **R² Score:** 99.25%  
- **MAE:** ~$373  
- **RMSE:** ~$620  

###  Interpretation:
- Average prediction error ≈ $373  
- Higher RMSE indicates presence of some high-cost outliers  

---

##  Important Note on Performance

The high R² score may be influenced by the inclusion of **previous year cost**, which is strongly correlated with future expenses.

--> Model should be validated further on real-world unseen data.

---

##  Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Pickle (for model serialization)  

---

##  How to Run the Project

### 1. Clone Repository
```bash
git clone https://github.com/qasim-byte/medical-cost-prediction.git
cd medical-cost-prediction
```
---
### 2. Install Dependencies
```
pip install -r requirements.txt
```
---
### 3. Run Streamlit App
```streamlit run medical_cost_app.py```
---

### Workflow
User Input → Data Preprocessing → Model Prediction → Cost Output → Risk Analysis
---

### **Limitations**
Possible overfitting due to high accuracy
Depends on quality of input data
May not generalize well to real-world healthcare data
Not a substitute for professional medical or financial advice
---

###  **Future Improvements**
Use real-world healthcare datasets
Add more medical features (lab reports, lifestyle habits)
Apply advanced tuning and cross-validation
Improve handling of outliers (log transformation)
Deploy on cloud platforms (Render, AWS, etc.)
---

 **Author**

Qasim Ashfaq
---
### **Disclaimer**

```This project is for educational purposes only. Predictions are estimates and should not be used for real medical or financial decisions.```
---
**If you like this project**

**Give it a star on GitHub**🌟



---
