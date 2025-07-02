# Import all the necessary libraries
import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st

# Load the model and structure
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns (1).pkl")

# Let's create an User interface
st.title("Water Pollutants Predictor")
st.write("Predict the water pollutants based on Year and Station ID")

# User inputs
year_input = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("Enter Station ID", value='1')
month_input = st.number_input("Enter Month", min_value=1, max_value=12, value=1)

# Define pollutant safety thresholds
thresholds = {
    'NH4': 0.5,
    'BSK5': 3.0,
    'Suspended': 25.0,
    'O2': 5.0,
    'NO3': 10.0,
    'NO2': 0.1,
    'SO4': 250.0,
    'PO4': 0.1,
    'CL': 250.0
}

# List of pollutant names 
pollutants = ['NH4', 'BSK5', 'Suspended', 'O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

# Function to calculate percentage of safe water based on thresholds
def predict_safe_water_percentage(predicted_pollutants, thresholds):
    safe_count = 0
    for i, pollutant in enumerate(pollutants):
        predicted_value = predicted_pollutants[i]
        threshold = thresholds.get(pollutant)
        if pollutant == 'O2':
            if predicted_value >= threshold:
                safe_count += 1
        else:
            if predicted_value <= threshold:
                safe_count += 1
    safe_percentage = (safe_count / len(pollutants)) * 100
    return safe_percentage




# To encode and then predict
if st.button('Predict'):
    if not station_id:
        st.warning('Please enter the station ID')
    else:
        # Prepare the input
        input_df = pd.DataFrame({'year': [year_input], 'id':[station_id],'month': [month_input]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        # Align with model cols
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]

        # Predict
        predicted_pollutants = model.predict(input_encoded)[0]
        pollutants = ['NH4', 'BSK5', 'Suspended', 'O2', 'NO3', 'NO2', 'SO4',
       'PO4', 'CL']

        st.subheader(f"Predicted pollutant levels for the station '{station_id}' in {year_input}: in month {month_input} is")
        predicted_values = {}
        
        for p, val in zip(pollutants, predicted_pollutants):
            threshold = thresholds[p]
            if p == 'O2':
                is_safe = val >= threshold
            else:
                is_safe = val <= threshold

            status = "✅ Safe" if is_safe else "⚠️ Unsafe"
            st.write(f"{p}: {val:.2f} ({status})")

       
 # Show predicted safety percentage
        predicted_safe_percentage = predict_safe_water_percentage(predicted_pollutants, thresholds)
        st.success(f"Percentage of pollutants within limit and safety percentage of water is: {predicted_safe_percentage:.2f}%")


st.markdown("---")
with st.expander("📘 View Detailed Pollutant Thresholds and Significance"):
    st.markdown("Below are the standard limits and environmental significance of key water quality parameters:")

    data = {
        "Pollutant": ["NH₄ (Ammonium)", "BSK5 (BOD₅)", "Suspended Solids", "O₂ (Dissolved Oxygen)",
                      "NO₃ (Nitrate)", "NO₂ (Nitrite)", "SO₄ (Sulfate)", "PO₄ (Phosphate)", "Cl (Chloride)"],
        "Acceptable Limit": ["< 0.5 mg/L", "< 3 mg/L", "< 25 mg/L", "> 5 mg/L", "< 10 mg/L",
                             "< 0.1 mg/L", "< 250 mg/L", "< 0.1 mg/L", "< 250 mg/L"],
        "Environmental Significance": [
            "High levels indicate sewage/fertilizer pollution; toxic to aquatic life.",
            "Measures organic pollution; high values reduce oxygen, harming fish.",
            "Reduces light penetration and clogs gills of aquatic organisms.",
            "Essential for aquatic life; low values stress or kill organisms.",
            "Promotes eutrophication; harmful to drinking water and ecosystems.",
            "Toxic even at low levels; signals pollution and nitrogen imbalance.",
            "Generally safe in low amounts; high values affect taste, corrosion.",
            "Leads to algal blooms and oxygen depletion (eutrophication).",
            "Affects taste and salinity; harmful to freshwater organisms."
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)
