import pandas as pd
from config import categories


def generate_categories():
    category_data = []

    for i, category in enumerate(categories, start=1):
        category_data.append({
            "category_id": i,
            "category_name": category
        })

    df = pd.DataFrame(category_data)

    df.to_csv(
        "data/categories.csv",
        index=False
    )

    print("categories.csv generated successfully!")