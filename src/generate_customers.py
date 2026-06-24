import pandas as pd
import random
from config import fake, cities, customer_segments


def generate_customers():
    customer_data = []

    for customer_id in range(1, 101):

        # Step 1: Name generate
        name = fake.name()

        # Step 2: Email generate (realistic + name linked)
        email_name = name.lower().replace(" ", ".")
        email = email_name + str(random.randint(10, 99)) + "@gmail.com"

        # Step 3: Add customer record
        customer_data.append({
            "customer_id": customer_id,
            "customer_name": name,
            "email": email,
            "city": random.choice(cities),
            "signup_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),
            "gender": random.choice(["Male", "Female"]),
            "age": random.randint(18, 60),
            "customer_segment": random.choice(customer_segments)
        })

    # Step 4: Convert to DataFrame
    df = pd.DataFrame(customer_data)

    # Step 5: Save CSV
    df.to_csv("data/customers.csv", index=False)

    print("customers.csv generated successfully!")