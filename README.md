# 📉 Customer Churn Prediction Web App

A Machine Learning–powered web application that predicts whether a customer is likely to churn (leave a service) based on their details.

This project helps businesses identify at-risk customers and take proactive steps to improve customer retention.

---

## 🚀 Features

- 🔍 Real-time customer churn prediction
- 🖥️ Simple and user-friendly web interface
- ⚡ Fast predictions using a pre-trained ML model
- 🔤 Handles categorical data using saved encoders
- 🌐 Ready for deployment

---

## 🛠️ Tech Stack

### Frontend
- HTML (Templates)

### Backend
- Python
- Flask

### Machine Learning
- scikit-learn
- Pandas
- NumPy

---

## 📂 Project Structure

Customer-Churn-Prediction/
│── templates/ # HTML templates for UI
│── churn_app.py # Flask web application
│── customer_churn_model.pkl # Trained ML model
│── encoders.pkl # Encoders for categorical features
│── requirements.txt # Project dependencies
│── .gitignore
---

## ⚙️ How It Works

1. User enters customer details in the web form  
2. Input data is preprocessed using saved encoders  
3. The trained ML model predicts churn probability  
4. The result is displayed instantly on the web page  

---
📊 Model Details

-Algorithm: Random Forest / Logistic Regression

-Task: Binary Classification (Churn / Not Churn)

-Input: Customer demographic & service data

-Output: Churn prediction

💡 Use Cases

-Telecom companies

-Subscription-based services

-SaaS platforms

-Banking & financial services

🔮 Future Improvements

-Add prediction probability score

-Deploy on Render / Railway / AWS

-Build analytics dashboard

-Improve UI with CSS & JavaScript

-Use advanced models (XGBoost, Neural Networks)
