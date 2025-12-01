from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("customer_churn_model.pkl", "rb") as f:
    model_dict = pickle.load(f)

model = model_dict["model"]
feature_names = model_dict["features_names"]

with open("encoders.pkl", "rb") as f:
    preprocessor = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    tenure_value = request.form.get("tenure", "").strip()
    if tenure_value == "":
        tenure_value = 0


    data = {
        "gender": [request.form["gender"]],
        "SeniorCitizen": [int(request.form["SeniorCitizen"])],
        "Partner": [request.form["Partner"]],
        "Dependents": [request.form["Dependents"]],
        "tenure": [int(request.form["tenure"])],
        "PhoneService": [request.form["PhoneService"]],
        "MultipleLines": [request.form["MultipleLines"]],
        "InternetService": [request.form["InternetService"]],
        "OnlineSecurity": [request.form["OnlineSecurity"]],
        "OnlineBackup": [request.form["OnlineBackup"]],
        "DeviceProtection": [request.form["DeviceProtection"]],
        "TechSupport": [request.form["TechSupport"]],
        "StreamingTV": [request.form["StreamingTV"]],
        "StreamingMovies": [request.form["StreamingMovies"]],
        "Contract": [request.form["Contract"]],
        "PaperlessBilling": [request.form["PaperlessBilling"]],
        "PaymentMethod": [request.form["PaymentMethod"]],
        "MonthlyCharges": [float(request.form["MonthlyCharges"])],
        "TotalCharges": [float(request.form["TotalCharges"])],
    }

    df = pd.DataFrame(data)

    for col, encoder in preprocessor.items():
        df[col] = encoder.transform(df[col])

    prediction = model.predict(df)[0]
    proba = round(model.predict_proba(df)[0][1] * 100, 2)

    if prediction == 1:
        result = " Customer is LIKELY TO CHURN"
        color = "red"
    else:
        result = " Customer is NOT LIKELY TO CHURN"
        color = "green"

    return render_template(
        "index.html",
        result=result,
        color=color,
        probability=proba
    )

if __name__ == "__main__":
    app.run(debug=True)
