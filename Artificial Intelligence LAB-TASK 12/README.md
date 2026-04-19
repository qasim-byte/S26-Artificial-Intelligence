# 🎓 GPA Prediction System (Flask-Based Web App)

## 📌 Overview

This project is a **machine learning-based GPA prediction system** that estimates a student's GPA based on academic, behavioral, and demographic features.

The model is integrated into a **Flask web application**, allowing users to input student data through a browser interface and receive predictions in real time.

---

## ⚙️ How the Model Works

### 1. Data Representation

The model uses **numerical features only**. All categorical variables are pre-encoded into integers during training.

### Input Features:

* **Age** (10–25)
* **Gender** (1 = Male, 0 = Female)
* **Ethnicity** (Encoded numeric category)
* **Parental Education** (0–4 scale)
* **Study Time Weekly** (hours)
* **Absences** (count)
* **Tutoring** (1 = Yes, 0 = No)
* **Parental Support** (0–4 scale)
* **Extracurricular Activities** (1/0)
* **Sports Participation** (1/0)
* **Music Participation** (1/0)
* **Volunteering** (1/0)
* **Grade Class** (1–12)

---

### 2. Model Training

* The dataset was preprocessed to ensure all features are numeric.
* A machine learning model (e.g., regression-based) was trained on this data.
* The trained model was saved using:

  ```python
  joblib.dump(model, "gpa_prediction_model.pkl")
  ```

---

### 3. Prediction Logic

* User inputs are collected from the web interface.
* Inputs are converted into a structured format (`pandas DataFrame`)
* The model predicts GPA using:

  ```python
  prediction = model.predict(input_df)
  ```

---

## 🌐 Flask Integration

### Why Flask?

Flask is used to convert the ML model into a **web-accessible application**, enabling interaction without running Python scripts manually.

---

### Application Flow

1. **User opens web page**

   * Flask serves `index.html`

2. **User enters input values**

   * Form collects all feature values

3. **Form submission**

   * Data is sent to `/predict` route via POST request

4. **Backend processing**

   * Flask extracts and validates input
   * Converts data into numeric format
   * Passes it to the ML model

5. **Prediction returned**

   * GPA result is sent back to the HTML template
   * Displayed dynamically on the page

---

### Key Flask Components

#### `app.py`

* Main backend logic
* Loads trained model
* Handles routing and prediction

#### Routes:

```python
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
```

---

### Static & Template Structure

```
project/
│── app.py
│── gpa_prediction_model.pkl
│
│── templates/
│     └── index.html
│
│── static/
│     ├── css/style.css
│     └── js/script.js
```

---

## 🎯 Input Validation

Validation is handled at two levels:

### 1. Frontend (JavaScript)

* Prevents invalid ranges (e.g., Age > 25)
* Highlights incorrect fields
* Stops submission if invalid

### 2. Backend (Flask)

* Converts inputs safely
* Handles runtime errors

---

## 🚀 Running the Project

### 1. Install Dependencies

```bash
pip install flask pandas scikit-learn joblib
```

### 2. Run Flask App

```bash
python app.py
```

### 3. Open in Browser

```
http://127.0.0.1:5000
```

---

## ⚠️ Important Notes

* The model expects **exact numeric encoding**
  → Any mismatch will produce incorrect predictions

* No encoders are used during inference
  → Inputs must already be in encoded form

* Feature order must match training data

---

## 📈 Possible Improvements

* Replace numeric inputs with dropdowns/sliders
* Add model explainability (e.g., feature importance)
* Use AJAX for real-time prediction
* Deploy on cloud platforms (Render, Heroku)

---

## 📊 Summary

This project demonstrates:

* End-to-end ML pipeline deployment
* Real-time prediction via Flask
* Clean separation of frontend and backend
* Practical handling of encoded data in production

---

## 📎 Conclusion

The system successfully bridges the gap between a trained machine learning model and a usable web application, making predictions accessible through a simple and structured interface.

---
