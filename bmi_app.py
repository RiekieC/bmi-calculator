import streamlit as st

# Set page config
st.set_page_config(page_title="BMI Calculator", page_icon="🍏", layout="centered")

# Jerry Blue color
JERRY_BLUE = "#6EA8FF"

st.markdown(f"""
    <h2 style='color:{JERRY_BLUE}; text-align:center;'>🍏 Jerry's BMI Calculator</h2>
    <p style='text-align:center;'>Calculate your Body Mass Index (BMI) and find out what it means for you.</p>
""", unsafe_allow_html=True)

# Input fields
height = st.number_input("Enter your height (cm):", min_value=50, max_value=250, value=170)
weight = st.number_input("Enter your weight (kg):", min_value=10, max_value=300, value=65)

if st.button("Calculate BMI"):
    try:
        bmi = weight / ((height / 100) ** 2)

        # Categorize BMI
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        st.markdown(f"<h3 style='color:{JERRY_BLUE};'>Your BMI: {bmi:.2f}</h3>", unsafe_allow_html=True)
        st.success(f"Category: {category}")

    except Exception as e:
        st.error("Something went wrong while calculating BMI.")
else:
    st.info("Enter your height and weight above, then click 'Calculate BMI'.")
