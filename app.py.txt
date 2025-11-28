import streamlit as st
import pickle
import numpy as np

# ✅ Load saved model
model = pickle.load(open("logistic_model.pkl", "rb"))

st.title("🚢 Titanic Survival Prediction App")

Pclass = st.selectbox("Passenger Class", [1,2,3])
Age = st.slider("Age", 0, 80, 25)
SibSp = st.number_input("Number of Siblings/Spouse", 0, 8, 0)
Parch = st.number_input("Number of Parents/Children", 0, 6, 0)
Fare = st.number_input("Ticket Fare", 0.0, 600.0, 32.0)
Sex = st.selectbox("Sex", ["Male", "Female"])
Embarked = st.selectbox("Port of Embarkation", ["Q", "S", "C"])

# Encoding (same as training)
sex_male = 1 if Sex == "Male" else 0
emb_Q = 1 if Embarked == "Q" else 0
emb_S = 1 if Embarked == "S" else 0

input_data = np.array([[Pclass, Age, SibSp, Parch, Fare, sex_male, emb_Q, emb_S]])

if st.button("Predict Survival"):
    result = model.predict(input_data)[0]
    
    if result == 1:
        st.success(" PASSENGER WILL SURVIVE")
    else:
        st.error(" PASSENGER WILL NOT SURVIVE")
