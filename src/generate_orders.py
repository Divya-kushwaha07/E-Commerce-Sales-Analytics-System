import pandas as pd
import random
from datetime import date
from config import fake, cities, order_statuses, order_status_weights


def generate_orders():
    order_data = []

    for order_id in range(1, 1001):
        order_data.append({
            "order_id": order_id,
            "customer_id": random.randint(1, 100),
            "order_date": fake.date_between(
                start_date=date(2025, 1, 1),
                end_date=date(2025, 12, 31)
            ),
            "shipping_city": random.choice(cities),
            "order_status": random.choices(
                population=order_statuses,
                weights=[80, 10, 7, 3],
                k=1
             )[0]
        })

    df = pd.DataFrame(order_data)

    df.to_csv(
        "data/orders.csv",
        index=False
    )

    print("orders.csv generated successfully!")