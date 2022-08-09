# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 09:47:11 2022

@author: sajid
"""

import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('C:/Users/sajid/OneDrive/Desktop/myfirst web app/diabetes_model.sav','rb'))


def diabetes_prediction(input_data):
    
    input_data = (1,85,66,29,0,26.6,0.351,31)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    #standardize the input data
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] ==1):
        return 'The person is not diabetic'
    else:
        return'The person is diabetic'
        
        
def main():
    
    st.title('Diabetes Prediction Web app')
    
    #getting the input data from the user
    
    Pregnancies =st.text_input('Number of pregnancies')
    Glucose     =st.text_input('Glucose level')
    BloodPressure =st.text_input('Blood Pressure value')
    SkinThickness =st.text_input('Skin Thickness value')
    Insuin =st.text_input('Insulin level')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction =st.text_input('Diabetes Pedigree function value')
    Age =st.text_input('Age of a person')
    
    
    diagnosis =''
    
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreefunction, Age])
        
    st.success(diagnosis)
    
    
if __name__ =='__main__':
    main()

        
    
        
        