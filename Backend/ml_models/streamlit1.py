import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Robo-Advisor",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded"

)
def load_lottiefile(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)
    
c1,c2 = st.columns([2.5,1])

with c1:
    # Load the trained Random Forest Regressor model for insurance cost prediction
    with open("medical_insurance_cost.pkl", "rb") as model_file:
        random_forest_regressor = pickle.load(model_file)

    # Load the trained model for life expectancy prediction
    model_path = "Life_Expectancy_Prediction.pkl"
    with open(model_path, "rb") as model_file:
        life_expectancy_model = pickle.load(model_file)

    # Encoding mappings for insurance cost prediction
    sex_mapping = {'Male': 0, 'Female': 1}
    smoker_mapping = {'Yes': 0, 'No': 1}
    region_mapping = {'Southeast': 0, 'Southwest': 1, 'Northeast': 2, 'Northwest': 3}

    # Function to predict life expectancy
    def predict_life_expectancy(features):
        return life_expectancy_model.predict(features)

    # Retirement Savings Projection Function
    def retirement_savings_projection(initial_savings, annual_contribution, years):
        interest_rate = 0.05  # assumed annual interest rate
        savings = []

        for year in range(1, years + 1):
            initial_savings = initial_savings * (1 + interest_rate) + annual_contribution
            savings.append(initial_savings)

        return savings

    # Initialize session state to store predictions
    if 'insurance_cost_prediction' not in st.session_state:
        st.session_state.insurance_cost_prediction = None

    if 'life_expectancy_prediction' not in st.session_state:
        st.session_state.life_expectancy_prediction = None

    # Page title and subtitle for insurance cost prediction
    st.header('Retirement Planning and Health Predictions')


    # Insurance Cost Prediction Section
    st.subheader('Insurance Cost Prediction')

    # Input fields for insurance cost prediction
    age = st.number_input('Age', min_value=18, max_value=100, step=1)
    sex = st.radio('Sex', ['Male', 'Female'])
    bmi = st.number_input('BMI', min_value=10.0, max_value=60.0, step=0.1)
    children = st.number_input('Number of Children', min_value=0, max_value=10, step=1)
    smoker = st.radio('Smoker', ['Yes', 'No'])
    region = st.radio('Region', ['Southeast', 'Southwest', 'Northeast', 'Northwest'])

    sex = sex_mapping[sex]
    smoker = smoker_mapping[smoker]
    region = region_mapping[region]

    # Button to trigger the insurance cost prediction
    if st.button('Predict Insurance Cost'):
        input_data = np.array([age, sex, bmi, children, smoker, region]).reshape(1, -1)
        insurance_cost_prediction = random_forest_regressor.predict(input_data)

        # Display output in a colored box with model label
        st.session_state.insurance_cost_prediction = insurance_cost_prediction
        st.info('Insurance Cost Prediction: {:.2f}'.format(insurance_cost_prediction[0]))

    # Life Expectancy Prediction Section
    st.subheader('Life Expectancy Prediction')

    # Input fields for life expectancy prediction
    year = st.number_input("Enter the year:", min_value=2000, max_value=2025, value=2020)
    status = st.radio("Select the country status:", ["Developed", "Developing"])
    population = st.number_input("Enter the population:", min_value=0, value=20835722)
    hepatitis_b = st.number_input("Enter hepatitis B coverage (%):", min_value=0, max_value=100, value=87)
    measles = st.number_input("Enter measles cases:", min_value=0, value=2500)
    alcohol = st.number_input("Enter alcohol consumption (liters):", min_value=0.0, value=7.0)
    bmi = st.number_input("Enter BMI:", min_value=0.0, value=28.0)
    polio = st.number_input("Enter polio coverage (%):", min_value=0, max_value=100, value=90)
    diphtheria = st.number_input("Enter diphtheria coverage (%):", min_value=0, max_value=100, value=88)
    hiv_aids = st.number_input("Enter HIV/AIDS prevalence (%):", min_value=0.0, value=2.0)
    gdp = st.number_input("Enter GDP per capita:", min_value=0, value=51386)

    status_mapping = {'Developed': 0, 'Developing': 1}
    status = status_mapping[status]

    # Button to trigger the life expectancy prediction
    if st.button('Predict Life Expectancy'):
        user_inputs = pd.DataFrame({
            'year': [year],
            'status': [status],
            'population': [population],
            'hepatitis_b': [hepatitis_b],
            'measles': [measles],
            'alcohol': [alcohol],
            'bmi': [bmi],
            'polio': [polio],
            'diphtheria': [diphtheria],
            'hiv/aids': [hiv_aids],
            'gdp': [gdp],
        })
        life_expectancy_prediction = predict_life_expectancy(user_inputs)

        # Display output in a colored box with model label
        st.session_state.life_expectancy_prediction = life_expectancy_prediction
        st.success('Life Expectancy Prediction: {:.2f}'.format(life_expectancy_prediction[0]))

with c2:

    # Retirement Savings Projection Section
    st.header('Retirement Savings Projection')

    lottie1 = load_lottiefile('../assets/Animation-healthcare.json')
    st_lottie(lottie1, key="hello1")
    # Input fields for retirement savings projection
    # initial_savings = st.number_input("Initial Savings ($)", min_value=0, value=10000)
    # annual_contribution = st.number_input("Annual Contribution ($)", min_value=0, value=5000)
    # projection_years = st.number_input("Projection Years", min_value=1, value=20)

    # # Button to trigger the retirement savings projection
    # if st.button('Project Retirement Savings'):
    #     savings_projection = retirement_savings_projection(initial_savings, annual_contribution, projection_years)

    #     # Plot savings projection chart
    #     fig, ax = plt.subplots(figsize=(10, 6))
    #     ax.plot(range(1, projection_years + 1), savings_projection, marker='o')
    #     ax.set_title('Retirement Savings Projection')
    #     ax.set_xlabel('Years')
    #     ax.set_ylabel('Savings ($)')
    #     st.pyplot(fig)
    #     # Display personalized recommendation based on life expectancy and insurance cost
    #     st.subheader('Personalized Recommendation')

    #     if st.session_state.life_expectancy_prediction[0] > 80 and st.session_state.insurance_cost_prediction[0] < 20000:
    #         st.success("Congratulations! Based on your predictions, you are on track for a healthy and financially secure retirement.")
    #     else:
    #         st.warning("Consider reviewing your health and financial plan to ensure a more secure retirement.")


footer = """
<style>
    .footer {
        width: 100%;
        background-color: #d4cbb1;
        padding: 10px;
        text-align: center;
        color: black;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
    }
</style>
<div class="footer">
    <p>© 2023 Stock-Bot. All rights reserved.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
