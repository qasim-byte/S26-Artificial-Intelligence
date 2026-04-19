#  Medical Cost Prediction using Machine Learning

A machine learning project that predicts **annual medical expenses** based on personal health, lifestyle, and healthcare usage data. The system is deployed using a **Streamlit web application** for real-time interaction.

---
##  Problem Statement

Estimating future medical costs is difficult due to multiple interacting factors such as lifestyle, chronic conditions, and healthcare usage.

Traditional estimation methods are often inaccurate or static. This project aims to develop a machine learning-based system that provides dynamic and personalized cost predictions.
##  Project Overview

This project builds a regression model to estimate medical costs using features such as age, BMI, medical conditions, insurance details, and past healthcare expenses.

- Model: Gradient Boosting Regressor  
- Deployment: Streamlit Web App  
- Goal: Provide a simple, data-driven way to estimate healthcare costs and identify risk factors  

---
##  Methodology

1. Data Collection  
   - Dataset containing health, demographic, and cost-related features  

2. Data Preprocessing  
   - Encoding categorical variables (smoker, insurance type)  
   - Handling missing values (if any)  
   - Feature selection based on importance  

3. Model Training  
   - Used Gradient Boosting Regressor  
   - Trained on structured tabular data  

4. Model Evaluation  
   - Evaluated using R², MAE, and RMSE  

5. Deployment  
   - Model saved using pickle  
   - Integrated into Streamlit web app

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

##  Evaluation Metrics Explained

- MAE (~$373): Average prediction error  
- RMSE (~$620): Indicates presence of larger errors (outliers)  
- R² (99.25%): High accuracy on dataset  

 Note: High R² may be influenced by strong correlation of previous year cost with target.

##  Important Observation

The feature "previous_year_cost" is highly correlated with the target variable.

This may increase model performance artificially and should be carefully validated on unseen data. 

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
---
```streamlit run medical_cost_app.py```


### Workflow
---
```User Input → Data Preprocessing → Model Prediction → Cost Output → Risk Analysis```


### Limitations

- Possible overfitting due to very high R² score  
- Model depends heavily on input features like previous cost  
- Dataset may not represent real-world healthcare diversity  
- Predictions may be less accurate for extreme cases (very high costs)


###  **Future Improvements**
---
- Use real-world healthcare datasets
- Add more medical features (lab reports, lifestyle habits)
- Apply advanced tuning and cross-validation
- Improve handling of outliers (log transformation)
- Deploy on cloud platforms (Render, AWS, etc.)

##  Project Structure

├── medical_cost_app.py  
├── medical_cost_notebook.ipynb  
├── model_medical_cost.pkl  
├── README.md  

##  Example Prediction

Input:
- Age: 45  
- BMI: 30  
- Smoker: Yes  
- Previous Cost: $5000  

Output:
- Annual Cost: ~$7200  
- Monthly Cost: ~$600  

 **Author**
---
```Qasim Ashfaq```

### **Disclaimer**
---
```This project is for educational purposes only. Predictions are estimates and should not be used for real medical or financial decisions.```

**If you like this project**
---
**Give it a star on GitHub**🌟

---
