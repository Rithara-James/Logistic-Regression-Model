import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('logistic_model.pkl','rb'))

st.title("Titanic Survival Prediction App")

Pclass = st.selectbox('Passenger class',[1,2,3])
Age = st.slider("Age", 0, 80, 25)
Sibsp = st.number_input("Number of siblings/spouses aboard", 0, 10, 0)
Parch = st.number_input("Number of parents/children aboard", 0, 10, 0)
Fare = st.number_input("Ticket fare", 0.0, 600.0, 32.0)
Sex = st.selectbox("Sex", ['male', 'female'])
Embarked = st.selectbox("Embarkation",['Q','S','C'])

Sex_female = 1 if Sex == "female" else 0
Sex_male = 1 if Sex == 'male' else 0
Embarked_Q = 1 if Embarked == 'Q' else 0
Embarked_S = 1 if Embarked == 'S' else 0
Embarked_C = 1 if Embarked == 'C' else 0

input_data = np.array([[Pclass, Age, Sibsp, Parch, Fare, Sex_female, Sex_male, Embarked_Q, Embarked_S, Embarked_C]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.write("Passenger will Survive")
    else:
        st.write("Passenger will Not Survive")
