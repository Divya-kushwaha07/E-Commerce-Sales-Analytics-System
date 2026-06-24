import pandas as pd
import random

from config import payment_methods
from utils import get_payment_status, generate_payment_date


def generate_payments():

    orders_df = pd.read_csv("data/orders.csv")

    payment_data = []
    payment_id = 1

    for _, order in orders_df.iterrows():

        order_id = order["order_id"]
        order_status = order["order_status"]
        order_date = pd.to_datetime(order["order_date"])

        payment_status = get_payment_status(order_status)
        payment_date = generate_payment_date(order_date, 0)

        payment_data.append({
            "payment_id": payment_id,
            "order_id": order_id,
            "payment_method": random.choice(payment_methods),
            "payment_status": payment_status,
            "payment_date": payment_date,
            "transaction_amount": order.get("total_amount", 0)
        })

        payment_id += 1

    df = pd.DataFrame(payment_data)

    df.to_csv(
        "data/payments.csv",
        index=False
    )

    print("payments.csv generated successfully!")