from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("gpa_prediction_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = {
            "Age": int(request.form["Age"]),
            "Gender": int(request.form["Gender"]),
            "Ethnicity": int(request.form["Ethnicity"]),
            "ParentalEducation": int(request.form["ParentalEducation"]),
            "StudyTimeWeekly": int(request.form["StudyTimeWeekly"]),
            "Absences": int(request.form["Absences"]),
            "Tutoring": int(request.form["Tutoring"]),
            "ParentalSupport": int(request.form["ParentalSupport"]),
            "Extracurricular": int(request.form["Extracurricular"]),
            "Sports": int(request.form["Sports"]),
            "Music": int(request.form["Music"]),
            "Volunteering": int(request.form["Volunteering"]),
            "GradeClass": int(request.form["GradeClass"])
        }

        input_df = pd.DataFrame([features])

        prediction = model.predict(input_df)[0]

        return render_template("index.html",
                               prediction_text=f"Predicted GPA: {round(prediction, 2)}")

    except Exception as e:
        return render_template("index.html",
                               prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)