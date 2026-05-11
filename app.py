
import joblib
import pandas as pd
import streamlit as st

model = joblib.load("delivery_time_model.pkl")

st.title("Delivery Time Prediction")

st.write("This app predicts delivery time in minutes.")

distance_km = st.number_input("Distance in km", min_value=1.0, max_value=50.0, value=5.0)
courier_experience_years = st.number_input(
    "Courier experience years",
    min_value=0.0,
    max_value=20.0,
    value=2.0,
    step=0.5
)
hour = st.slider("Hour", 0, 23, 12)
weekday = st.slider("Weekday", 0, 6, 1)

weather = st.selectbox("Weather", ["sunny", "rain", "snow"])
traffic_level = st.selectbox("Traffic level", ["low", "medium", "high"])
restaurant_load = st.selectbox("Restaurant load", ["low", "medium", "high"])

input_data = pd.DataFrame({
    "order_id": [0],
    "distance_km": [distance_km],
    "courier_experience_years": [courier_experience_years],
    "hour": [hour],
    "weekday": [weekday],
    "weather": [weather],
    "traffic_level": [traffic_level],
    "restaurant_load": [restaurant_load],
})

input_data = pd.get_dummies(input_data, drop_first=True)

input_data = input_data.reindex(
    columns=model.feature_names_in_,
    fill_value=0
)

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted delivery time: {prediction:.1f} minutes")
