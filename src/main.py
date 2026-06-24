from utils import update_order_totals
from generate_categories import generate_categories
from generate_products import generate_products
from generate_customers import generate_customers
from generate_orders import generate_orders
from generate_order_items import generate_order_items
from generate_payments import generate_payments


def run_pipeline():

    print("Starting data generation pipeline...\n")

    print("Generating categories...")
    generate_categories()

    print("Generating products...")
    generate_products()

    print("Generating customers...")
    generate_customers()

    print("Generating orders...")
    generate_orders()

    print("Generating order items...")
    generate_order_items()

    print("Calculating order totals...")
    update_order_totals()

    print("Generating payments...")
    generate_payments()

    print("\nAll datasets generated successfully!")


if __name__ == "__main__":
    run_pipeline()