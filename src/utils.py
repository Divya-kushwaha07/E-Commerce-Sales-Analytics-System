import random
from datetime import timedelta


def calculate_delivery_days(order_status):
    """
    Returns delivery days based on order status.
    Only delivered orders have delivery time.
    """
    if order_status == "Delivered":
        return random.randint(2, 7)
    return None


def get_payment_status(order_status):
    """
    Maps order status to payment status.
    """
    if order_status == "Delivered":
        return "Success"
    elif order_status == "Shipped":
        return "Success"
    elif order_status == "Processing":
        return "Pending"
    else:
        return "Failed"


def generate_payment_date(order_date, delivery_days):
    """
    Generates realistic payment date after order date.
    Payment usually happens within 0–3 days.
    """
    extra_days = random.randint(0, 3)
    return order_date + timedelta(days=extra_days)

import pandas as pd


def update_order_totals():
    order_items = pd.read_csv("data/order_items.csv")
    orders = pd.read_csv("data/orders.csv")

    totals = order_items.groupby("order_id")["final_price"].sum().reset_index()
    totals.rename(columns={"final_price": "total_amount"}, inplace=True)

    orders = orders.drop(columns=["total_amount"], errors="ignore")
    orders = orders.merge(totals, on="order_id", how="left")

    orders["total_amount"] = orders["total_amount"].fillna(0)

    orders.to_csv("data/orders.csv", index=False)

    print("orders.csv updated with total_amount successfully!")