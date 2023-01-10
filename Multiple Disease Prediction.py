# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:52:13 2023

@author: Himasai Reddy
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('himasai-1423/Disease-Prediction-Model/Multiple_Disease_Prediction_System_Diabetes.ipynb', 'rb'))

heart_disease_model = pickle.load(open('himasai-1423/Disease-Prediction-Model/Multiple_Disease_Prediction_System_Heart_Disease.ipynb','rb'))

parkinsons_model = pickle.load(open('himasai-1423/Disease-Prediction-Model/Multiple_Disease_Prediction_System_Parkinson\'s_Disease.ipynb', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', '0')
        
    with col2:
        Glucose = st.text_input('Glucose Level', '120')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', '70')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value', '20')
    
    with col2:
        Insulin = st.text_input('Insulin Level', '79')
    
    with col3:
        BMI = st.text_input('BMI value', '32')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', '0.471876')
    
    with col2:
        Age = st.text_input('Age of the Person', '35')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age', '54')
        
    with col2:
        sex = st.text_input('Sex', '0')
        
    with col3:
        cp = st.text_input('Chest Pain types', '2')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', '130')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', '309')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', '0')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', '1')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', '120')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina', '0')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', '1')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', '1.8')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', '3')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', '2')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', '214.289')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', '260.277')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', '77.973')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', '0.00567')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', '0.00003')
        
    with col1:
        RAP = st.text_input('MDVP:RAP', '0.00295')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ', '0.00317')
        
    with col3:
        DDP = st.text_input('Jitter:DDP', '0.00885')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', '0.01884')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', '0.19')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', '0.01026')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', '0.01161')
        
    with col3:
        APQ = st.text_input('MDVP:APQ', '0.01373')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA', '0.03078')
        
    with col5:
        NHR = st.text_input('NHR', '0.04398')
        
    with col1:
        HNR = st.text_input('HNR', '21.209')
        
    with col2:
        RPDE = st.text_input('RPDE', '0.462803')
        
    with col3:
        DFA = st.text_input('DFA', '0.664357')
        
    with col4:
        spread1 = st.text_input('spread1', '-5.72406')
        
    with col5:
        spread2 = st.text_input('spread2', '0.190667')
        
    with col1:
        D2 = st.text_input('D2', '2.555477')
        
    with col2:
        PPE = st.text_input('PPE', '0.148569')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
