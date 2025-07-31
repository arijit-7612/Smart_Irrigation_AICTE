import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")

# App title and description
st.set_page_config(page_title="Smart Sprinkler System", layout="wide")
st.title("🚿 Smart Sprinkler System")
st.markdown("Enter **scaled sensor values (0 to 1)** to predict the **ON/OFF** status of 20 sprinklers across different farm parcels.")

st.divider()

# Sensor input layout: 4 columns x 5 rows
st.subheader("🌾 Sensor Readings")
sensor_values = []
cols = st.columns(4)

for i in range(20):
    col = cols[i % 4]
    with col:
        val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        sensor_values.append(val)

# Prediction section
st.divider()
center_col = st.columns([1, 1, 1])[1]
with center_col:
    if st.button("🔍 Predict Sprinkler Status"):
        input_array = np.array(sensor_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]

        st.success("✅ Prediction Complete!")
        st.markdown("### 💧 Sprinkler Status")

        # Display prediction in an expandable section
        with st.expander("See Detailed Sprinkler Status"):
            for i, status in enumerate(prediction):
                if status == 1:
                    st.markdown(f"✅ **Sprinkler {i} (parcel_{i}): ON**", unsafe_allow_html=True)
                else:
                    st.markdown(f"❌ **Sprinkler {i} (parcel_{i}): OFF**", unsafe_allow_html=True)
