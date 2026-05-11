# Delivery Time Prediction

Machine Learning project for predicting food delivery time based on delivery conditions such as distance, weather, traffic and restaurant load.

## Business Problem

Delivery platforms need accurate delivery time estimation to improve customer experience and operational efficiency.

This project predicts delivery time in minutes using machine learning models and analyzes how factors like traffic, weather and distance affect delivery duration.

---

# Dataset

The project uses a synthetic dataset generated according to realistic delivery business logic.

Features include:

- distance_km
- weather
- traffic_level
- restaurant_load
- courier_experience_years
- hour
- weekday

Target:

- delivery_time_min

The dataset also includes realistic data quality issues:

- missing values
- outliers
- inconsistent categories
- duplicates

---

# Project Pipeline

1. Exploratory Data Analysis (EDA)
2. Data Cleaning
3. Missing Value Handling
4. Outlier Detection
5. Feature Encoding
6. Train/Test Split
7. Linear Regression Model
8. Model Evaluation
9. Drift Monitoring
10. Streamlit Deployment

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

---

# Model Metrics

Linear Regression Results:

- MAE: 4.29
- RMSE: 5.38
- R² Score: 0.93

The model predicts delivery time with an average error of approximately 4 minutes.

---

# Drift Monitoring

The project includes basic monitoring and drift analysis by comparing original and new delivery distributions over time.

Distribution drift was analyzed for:

- delivery distance
- traffic conditions
- delivery time

---

# Streamlit App

The project includes a Streamlit web application for interactive delivery time prediction.

Example input:

- distance
- weather
- traffic level
- restaurant load
- courier experience

Output:

- predicted delivery time in minutes

---

# Repository Structure

```text
delivery-time-prediction/
│
├── delivery_time_prediction.ipynb
├── delivery_time_dirty_dataset.csv
├── delivery_time_model.pkl
├── app.py
├── requirements.txt
├── README.md
