import pandas as pd
import random
from config import products_catalog, product_brands, price_ranges, discount_options

def generate_products():
    product_data = []
    product_id = 1

    for category_id, category in enumerate(products_catalog, start=1):
        for product in products_catalog[category]:

            price = random.randint(
                price_ranges[category][0],
                price_ranges[category][1]
            )

            discount = random.choice(discount_options)

            cost_price = round(
                price * random.uniform(0.6, 0.9),
                2
            )

            product_data.append({
                "product_id": product_id,
                "product_name": product,
                "category_id": category_id,
                "brand": product_brands[product],
                "rating": round(random.uniform(3.5, 5.0), 1),
                "price": price,
                "stock_quantity": random.randint(10, 500),
                "discount_percentage": discount,
                "cost_price": cost_price
            })

            product_id += 1

    df = pd.DataFrame(product_data)

    df.to_csv(
        "data/products.csv",
        index=False
    )

    print("products.csv generated successfully!")