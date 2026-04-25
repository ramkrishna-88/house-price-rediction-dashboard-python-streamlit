import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="wide")

# Load model safely
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    st.error("❌ Model not found! Run train.py first")
    st.stop()

# Title
st.title("🏠 House Price Prediction Dashboard")
st.write("Enter property details below 👇")

st.markdown("---")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Details")
    area = st.number_input("📏 Area (sq ft)", min_value=300, step=50)
    bedrooms = st.number_input("🛏 Bedrooms", min_value=1)
    bath = st.number_input("🛁 Bathrooms", min_value=1)
    balcony = st.number_input("🌇 Balconies", min_value=0)

with col2:
    st.subheader("📊 Insights")

    attached = min(bedrooms, bath)
    common = max(0, bedrooms - bath)


    st.info(f"🚿 Attached Bathrooms: {attached}")
    st.info(f"🚽 Common Bathrooms: {common}")

    if bath > bedrooms:
        st.warning("⚠️ Bathrooms ज्यादा हैं Bedrooms से")

    st.success("✔ Model: Random Forest")

st.markdown("---")

# Prediction
if st.button("🚀 Predict Price"):
    try:
        features = np.array([[area, bedrooms, bath, balcony]])
        prediction = model.predict(features)

        price = round(abs(prediction[0]), 2)
        price_per_sqft = round(price / area, 2)

        st.success(f"💰 Estimated Price: ₹ {price} Lakhs")
        st.info(f"📌 Price per sqft: ₹ {price_per_sqft}")

        st.balloons()

    except Exception as e:
        st.error(f"❌ Error: {e}")

st.markdown("---")
st.caption("💡 Tip: Bigger area & better facilities increase price")