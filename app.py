# 1. Import libraries
from flask import Flask, render_template, request
import pandas as pd
import joblib

# 2. Create Flask app
app = Flask(__name__)

# 3. Load trained files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
lb = joblib.load("label_encoder.pkl")

# 4. Home page
@app.route("/")
def home():
    return render_template("index.html")

# 5. Prediction page
@app.route("/predict", methods=["POST"])
def predict():

    print(request.form)   

    cgpa = float(request.form["cgpa"])
    internships = int(request.form["internships"])
    projects = int(request.form["projects"])
    workshops = int(request.form["workshops"])
    aptitude = float(request.form["aptitude"])
    softskills = float(request.form["softskills"])
    extracurricular = int(request.form["extra"])
    training = int(request.form["training"])
    ssc = float(request.form["ssc"])
    hsc = float(request.form["hsc"])

    new_data = pd.DataFrame({
        "CGPA": [cgpa],
        "Internships": [internships],
        "Projects": [projects],
        "Workshops/Certifications": [workshops],
        "AptitudeTestScore": [aptitude],
        "SoftSkillsRating": [softskills],
        "ExtracurricularActivities": [extracurricular],
        "PlacementTraining": [training],
        "SSC_Marks": [ssc],
        "HSC_Marks": [hsc]
    })

    new_data = scaler.transform(new_data)

    prediction = model.predict(new_data)

    result = lb.inverse_transform(prediction)[0]

    return render_template("index.html", prediction=result)

# 6. Run Flask
if __name__ == "__main__":
    app.run(debug=True)