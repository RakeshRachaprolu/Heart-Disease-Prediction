import streamlit as st

# Page Configuration
st.set_page_config(page_title="Disease Prediction", layout="wide" ,page_icon="❤️")

# Sidebar Navigation
st.sidebar.title("Choose the disease")
menu = st.sidebar.radio("", ["Heart Disease",  "About"])

# Function to display the Heart Disease Prediction UI
def heart_disease_ui():
    st.markdown("<h2 style='text-align: center;'>Heart Disease Prediction</h2>", unsafe_allow_html=True)
    st.write("### Please provide the details")

    # Form Inputs - Two Column Layout
    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input("Enter your age:")
        gender = st.text_input("For male, write 1 or 0 for female")
        chest_pain = st.text_input("Do you have Chest pain?")
        resting_bp = st.text_input("Enter your resting blood pressure:")
        cholesterol = st.text_input("Enter your cholesterol level:")
        fasting_bs = st.text_input("Enter your fasting blood sugar:")
        ecg = st.text_input("Enter your resting electrocardiographic results:")

    with col2:
        max_hr = st.text_input("Enter your maximum heart rate:")
        angina = st.text_input("Do you have exercise-induced angina?")
        old_peak = st.text_input("Enter your old peak:")
        slope = st.text_input("Enter your slope:")
        vessels = st.text_input("Enter your number of major vessels:")
        thalassemia = st.text_input("Enter your thalassemia:")

    # Predict Button
    if st.button("Predict"):
        st.success("Prediction feature will be added soon!")  # Replace with model prediction

    # Display Image
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/77/Heart_anatomy_image.png", width=150)

# Function to display About Section
def about_section():
    st.markdown("<h2 style='text-align: center;'>About This Project</h2>", unsafe_allow_html=True)
    st.write("""
    This is a **Machine Learning-based Health Prediction System** built using **Streamlit**.
    - Users can predict **Heart Disease, Diabetes, and Parkinson’s**.
    - Built with **Python, Streamlit, and ML Models**.
    - Designed by **Raghunandan M S**.
    """)

# Route based on sidebar selection
if menu == "Heart Disease":
    heart_disease_ui()

elif menu == "About":
    about_section()
