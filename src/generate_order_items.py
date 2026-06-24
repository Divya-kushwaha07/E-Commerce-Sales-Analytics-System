import pandas as pd
import random


def generate_order_items():

    products_df = pd.read_csv("data/products.csv")
    orders_df = pd.read_csv("data/orders.csv")

    order_item_data = []
    order_item_id = 1

    for order_id in orders_df["order_id"]:

        # Har order me 1 se 5 unique products honge
        num_products = random.randint(1, 5)

        selected_products = products_df.sample(
            n=num_products,
            replace=False
        )

        for _, product in selected_products.iterrows():

            quantity = random.randint(1, 3)

            unit_price = product["price"]

            discount_percentage = product["discount_percentage"]

            final_price = round(
                quantity
                * unit_price
                * (1 - discount_percentage / 100),
                2
            )

            order_item_data.append({
                "order_item_id": order_item_id,
                "order_id": order_id,
                "product_id": product["product_id"],
                "quantity": quantity,
                "unit_price": unit_price,
                "discount_percentage": discount_percentage,
                "final_price": final_price
            })

            order_item_id += 1

    order_items_df = pd.DataFrame(order_item_data)

    order_items_df.to_csv(
        "data/order_items.csv",
        index=False
    )

    print("order_items.csv generated successfully!")