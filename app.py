import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu

# Page setup
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="👨‍🦰🤶")

working_dir = os.path.dirname(os.path.abspath(__file__))

# Load models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes.pkl', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart.pkl', 'rb'))
kidney_disease_model = pickle.load(open(f'{working_dir}/saved_models/kidney.pkl', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction",
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Kidney Disease Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'droplet'],
        default_index=0
    )

# ======================== DIABETES PREDICTION ========================
if selected == 'Diabetes Prediction':
    st.title("🩸 Diabetes Prediction Using Machine Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0.0)
    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0.0)
    with col3:
        BloodPressure = st.number_input("Blood Pressure Value", min_value=0.0)
    with col1:
        SkinThickness = st.number_input("Skin Thickness Value", min_value=0.0)
    with col2:
        Insulin = st.number_input("Insulin Value", min_value=0.0)
    with col3:
        BMI = st.number_input("BMI Value", min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function Value", min_value=0.0)
    with col2:
        Age = st.number_input("Age", min_value=0.0)

    diabetes_result = ""

    if st.button("Diabetes Test Result"):
        # BMI categories
        NewBMI_Underweight = 1 if BMI <= 18.5 else 0
        NewBMI_Overweight = 1 if 24.9 < BMI <= 29.9 else 0
        NewBMI_Obesity_1 = 1 if 29.9 < BMI <= 34.9 else 0
        NewBMI_Obesity_2 = 1 if 34.9 < BMI <= 39.9 else 0
        NewBMI_Obesity_3 = 1 if BMI > 39.9 else 0
        NewInsulinScore_Normal = 1 if 16 <= Insulin <= 166 else 0

        # Glucose categories
        NewGlucose_Low = 1 if Glucose <= 70 else 0
        NewGlucose_Normal = 1 if 70 < Glucose <= 99 else 0
        NewGlucose_Overweight = 1 if 99 < Glucose <= 126 else 0
        NewGlucose_Secret = 1 if Glucose > 126 else 0

        user_input = [
            Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
            BMI, DiabetesPedigreeFunction, Age, NewBMI_Underweight,
            NewBMI_Overweight, NewBMI_Obesity_1, NewBMI_Obesity_2,
            NewBMI_Obesity_3, NewInsulinScore_Normal, NewGlucose_Low,
            NewGlucose_Normal, NewGlucose_Overweight, NewGlucose_Secret
        ]

        prediction = diabetes_model.predict([user_input])

        if prediction[0] == 1:
            diabetes_result = "🚨 The person has Diabetes."
        else:
            diabetes_result = "✅ The person does NOT have Diabetes."

    st.success(diabetes_result)

# ======================== HEART DISEASE PREDICTION ========================
if selected == 'Heart Disease Prediction':
    st.title("❤️ Heart Disease Prediction Using Machine Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=0.0)
    with col2:
        sex = st.selectbox("Sex", ("0 - Female", "1 - Male"))
        sex = 1 if "Male" in sex else 0
    with col3:
        cp = st.selectbox("Chest Pain Type", ("0 - Typical Angina", "1 - Atypical Angina", "2 - Non-anginal", "3 - Asymptomatic"))
        cp = int(cp.split(" - ")[0])

    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value=0.0)
    with col2:
        chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0.0)
    with col3:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ("0 - No", "1 - Yes"))
        fbs = int(fbs.split(" - ")[0])
    with col1:
        restecg = st.selectbox("Resting ECG Results", ("0 - Normal", "1 - Abnormal", "2 - Hypertrophy"))
        restecg = int(restecg.split(" - ")[0])
    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0.0)
    with col3:
        exang = st.selectbox("Exercise Induced Angina", ("0 - No", "1 - Yes"))
        exang = int(exang.split(" - ")[0])
    with col1:
        oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0)
    with col2:
        slope = st.selectbox("Slope of Peak Exercise ST Segment", ("0", "1", "2"))
        slope = int(slope)
    with col3:
        ca = st.number_input("Major Vessels Colored by Fluoroscopy", min_value=0.0)
    with col1:
        thal = st.selectbox("Thal", ("0 - Normal", "1 - Fixed Defect", "2 - Reversible Defect"))
        thal = int(thal.split(" - ")[0])

    heart_disease_result = ""

    if st.button("Heart Disease Test Result"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]
        prediction = heart_disease_model.predict([user_input])

        if prediction[0] == 1:
            heart_disease_result = "🚨 This person has Heart Disease."
        else:
            heart_disease_result = "✅ This person does NOT have Heart Disease."

    st.success(heart_disease_result)

# ======================== KIDNEY DISEASE PREDICTION ========================
if selected == 'Kidney Disease Prediction':
    st.title("🧫 Kidney Disease Prediction Using Machine Learning")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.number_input("Age", min_value=0.0)
    with col2:
        blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
    with col3:
        specific_gravity = st.number_input("Specific Gravity", min_value=0.0)
    with col4:
        albumin = st.number_input("Albumin", min_value=0.0)
    with col5:
        sugar = st.number_input("Sugar", min_value=0.0)
    with col1:
        red_blood_cells = st.selectbox("Red Blood Cells", ("0 - Normal", "1 - Abnormal"))
        red_blood_cells = int(red_blood_cells.split(" - ")[0])
    with col2:
        pus_cell = st.selectbox("Pus Cell", ("0 - Normal", "1 - Abnormal"))
        pus_cell = int(pus_cell.split(" - ")[0])
    with col3:
        pus_cell_clumps = st.selectbox("Pus Cell Clumps", ("0 - Not Present", "1 - Present"))
        pus_cell_clumps = int(pus_cell_clumps.split(" - ")[0])
    with col4:
        bacteria = st.selectbox("Bacteria", ("0 - Not Present", "1 - Present"))
        bacteria = int(bacteria.split(" - ")[0])
    with col5:
        blood_glucose_random = st.number_input("Blood Glucose Random", min_value=0.0)
    with col1:
        blood_urea = st.number_input("Blood Urea", min_value=0.0)
    with col2:
        serum_creatinine = st.number_input("Serum Creatinine", min_value=0.0)
    with col3:
        sodium = st.number_input("Sodium", min_value=0.0)
    with col4:
        potassium = st.number_input("Potassium", min_value=0.0)
    with col5:
        haemoglobin = st.number_input("Haemoglobin", min_value=0.0)
    with col1:
        packed_cell_volume = st.number_input("Packed Cell Volume", min_value=0.0)
    with col2:
        white_blood_cell_count = st.number_input("White Blood Cell Count", min_value=0.0)
    with col3:
        red_blood_cell_count = st.number_input("Red Blood Cell Count", min_value=0.0)
    with col4:
        hypertension = st.selectbox("Hypertension", ("0 - No", "1 - Yes"))
        hypertension = int(hypertension.split(" - ")[0])
    with col5:
        diabetes_mellitus = st.selectbox("Diabetes Mellitus", ("0 - No", "1 - Yes"))
        diabetes_mellitus = int(diabetes_mellitus.split(" - ")[0])
    with col1:
        coronary_artery_disease = st.selectbox("Coronary Artery Disease", ("0 - No", "1 - Yes"))
        coronary_artery_disease = int(coronary_artery_disease.split(" - ")[0])
    with col2:
        appetite = st.selectbox("Appetite", ("0 - Good", "1 - Poor"))
        appetite = int(appetite.split(" - ")[0])
    with col3:
        peda_edema = st.selectbox("Pedal Edema", ("0 - No", "1 - Yes"))
        peda_edema = int(peda_edema.split(" - ")[0])
    with col4:
        aanemia = st.selectbox("Anemia", ("0 - No", "1 - Yes"))
        aanemia = int(aanemia.split(" - ")[0])

    kidney_diagnosis = ""

    if st.button("Kidney Test Result"):
        user_input = [
            age, blood_pressure, specific_gravity, albumin, sugar,
            red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
            blood_glucose_random, blood_urea, serum_creatinine,
            sodium, potassium, haemoglobin, packed_cell_volume,
            white_blood_cell_count, red_blood_cell_count,
            hypertension, diabetes_mellitus, coronary_artery_disease,
            appetite, peda_edema, aanemia
        ]

        prediction = kidney_disease_model.predict([user_input])

        if prediction[0] == 1:
            kidney_diagnosis = "🚨 The person has Kidney Disease."
        else:
            kidney_diagnosis = "✅ The person does NOT have Kidney Disease."

    st.success(kidney_diagnosis)
