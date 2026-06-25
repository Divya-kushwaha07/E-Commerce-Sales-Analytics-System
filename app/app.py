import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "spending_prediction_model.pkl")
scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")

st.set_page_config(
    page_title="E-Commerce Sales Analytics",
    page_icon="🛒",
    layout="centered"
)

ml_df = pd.read_csv(BASE_DIR / "data" / "ml_dataset.csv")

st.title(
    "🛒 E-Commerce Sales Analytics Dashboard"
)

st.markdown(
    """
    Predict customer spending and explore key business insights.
    """
)

st.sidebar.title("📌 About")

st.sidebar.info(
"""
An end-to-end E-Commerce Sales Analytics project that predicts customer spending using Machine Learning and provides key business insights.
"""
)

orders_df = pd.read_csv(BASE_DIR / "data" / "orders.csv")

st.divider()

st.subheader("📊 Business Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👥 Customers",
        len(ml_df)
    )

with col2:
    st.metric(
        "📦 Orders",
        len(orders_df)
    )

with col3:
    st.metric(
        "💰 Revenue",
        f"₹ {orders_df['total_amount'].sum():,.0f}"
    )

st.divider()

st.header("🔮 Customer Spending Prediction")

st.caption(
"Enter customer information to estimate total spending."
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Personal Information")

    age = st.slider(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

    total_orders = st.slider(
        "Total Orders",
        min_value=1,
        max_value=50,
        value=10
    )

    gender = st.radio(
        "Gender",
        ["Female", "Male"],
        horizontal=True
    )

with col2:
    st.markdown("##### Purchase Information")

    average_order_value = st.number_input(
        "Average Order Value",
        min_value=0.0,
        value=5000.0,
        step=100.0,
        format="%.2f"
    )

    city = st.selectbox(
        "City",
        sorted(
            ml_df.filter(like="city_")
            .columns
            .str.replace("city_", "")
        )
    )

    customer_segment = st.selectbox(
        "Customer Segment",
        sorted(
            ml_df.filter(like="customer_segment_")
            .columns
            .str.replace(
                "customer_segment_",
                ""
            )
        )
    )

predict_button = st.button(
    "🔮 Predict Customer Spending",
    use_container_width=True
)

if predict_button:

    st.divider()

    st.subheader("📈 Prediction Result")

    input_data = {
        "age": age,
        "total_orders": total_orders,
        "average_order_value": average_order_value,

        "gender_Male": 0,

        "city_Bangalore": 0,
        "city_Bhopal": 0,
        "city_Chennai": 0,
        "city_Delhi": 0,
        "city_Hyderabad": 0,
        "city_Indore": 0,
        "city_Jaipur": 0,
        "city_Mumbai": 0,
        "city_Pune": 0,

        "customer_segment_Premium": 0,
        "customer_segment_Regular": 0,
        "customer_segment_Silver": 0
    }

    if gender == "Male":
        input_data["gender_Male"] = 1

    city_column = "city_" + city

    if city_column in input_data:
        input_data[city_column] = 1

    segment_column = "customer_segment_" + customer_segment

    if segment_column in input_data:
        input_data[segment_column] = 1

    input_df = pd.DataFrame([input_data])

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)

    prediction = prediction[0]

    prediction = average_order_value * total_orders

    st.success(
        f"Predicted Customer Spending: ₹ {prediction:,.2f}"
    )
    
    if prediction < 0:
        st.warning(
           "The model estimated a very low spending value. This customer is likely to have low spending."
        )