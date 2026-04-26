#  Medical Cost Prediction using Machine Learning

A machine learning project that predicts **annual medical expenses** based on personal health, lifestyle, and healthcare usage data. The system is deployed using a **Streamlit web application** for real-time interaction.

## Project Overview

This project presents a machine learning-based system for predicting annual medical costs using individual health, lifestyle, and healthcare usage data.

The system uses a Gradient Boosting Regressor to model complex relationships between features such as age, BMI, medical conditions, insurance coverage, and historical medical expenses.

A Streamlit web application is developed to provide an interactive interface where users can input their data and receive real-time predictions along with risk factor analysis.

---
##  Problem Statement

Estimating future medical expenses is challenging due to multiple interacting factors such as health conditions, lifestyle habits, and healthcare usage.

Traditional methods often fail to capture these complex relationships. This project aims to develop a machine learning-based solution to provide more accurate and personalized cost predictions.

##  Dataset

- Type: Structured tabular dataset  
- Features include:
  - Age, BMI, Smoking status  
  - Diabetes, Hypertension, Heart Disease  
  - Insurance type and coverage  
  - Healthcare usage metrics  
  - Previous year medical cost  

 Note: Previous year cost is highly correlated with the target variable and significantly influences predictions.
 
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

##  Model Performance

- R² Score: 99.25%  
- MAE: ~$373  
- RMSE: ~$620  

###  Interpretation

- MAE shows average prediction error  
- Higher RMSE indicates presence of larger errors (outliers)  

 Note:
The high R² score is influenced by the inclusion of "previous_year_cost", which is strongly correlated with the target variable. This may lead to optimistic performance estimates.
---

##  Workflow

User Input → Data Encoding → Model Prediction → Cost Estimation → Risk Analysis

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

##  Why This Project Matters

Healthcare costs are unpredictable and often expensive. A predictive system can help individuals and organizations better plan finances and identify high-risk factors early.

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
