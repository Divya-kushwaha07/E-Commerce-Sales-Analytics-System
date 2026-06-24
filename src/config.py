import random
import numpy as np
from faker import Faker

# Initialize Faker for Indian-style data
fake = Faker("en_IN")

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Home Appliances",
    "Beauty",
    "Sports",
    "Toys",
    "Grocery",
    "Furniture",
    "Accessories"
]

product_brands = {
    "iPhone 16": "Apple",
    "Samsung Galaxy S25": "Samsung",
    "Dell Inspiron Laptop": "Dell",
    "Sony Headphones": "Sony",
    "Apple Watch": "Apple",

    "Men's T-Shirt": "Nike",
    "Women's Jeans": "Levi's",
    "Hoodie": "Adidas",
    "Jacket": "Puma",
    "Kurti": "Zara",

    "Atomic Habits": "Penguin",
    "Deep Work": "HarperCollins",
    "Harry Potter": "Bloomsbury",
    "The Alchemist": "HarperCollins",
    "Rich Dad Poor Dad": "Penguin",

    "Microwave Oven": "LG",
    "Refrigerator": "Samsung",
    "Washing Machine": "Whirlpool",
    "Air Conditioner": "Panasonic",
    "Mixer Grinder": "Philips",

    "Face Wash": "Nivea",
    "Lipstick": "Maybelline",
    "Perfume": "L'Oreal",
    "Shampoo": "Dove",
    "Moisturizer": "Nivea",

    "Cricket Bat": "SG",
    "Football": "Nike",
    "Badminton Racket": "Yonex",
    "Yoga Mat": "Adidas",
    "Dumbbells": "Puma",

    "Toy Car": "Hot Wheels",
    "Barbie Doll": "Barbie",
    "Lego Set": "Lego",
    "Puzzle Game": "Funskool",
    "Teddy Bear": "Disney",

    "Rice": "Aashirvaad",
    "Milk": "Amul",
    "Tea Powder": "Tata",
    "Sugar": "Fortune",
    "Cooking Oil": "Fortune",

    "Office Chair": "Godrej",
    "Study Table": "Nilkamal",
    "Sofa": "IKEA",
    "Bed": "Durian",
    "Wardrobe": "Urban Ladder",

    "Backpack": "Wildcraft",
    "Wallet": "Titan",
    "Sunglasses": "Ray-Ban",
    "Belt": "Fastrack",
    "Cap": "Nike"
}

cities = [
    "Bhopal",
    "Indore",
    "Delhi",
    "Mumbai",
    "Pune",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Jaipur",
    "Ahmedabad"
]

products_catalog = {
    "Electronics": [
        "iPhone 16",
        "Samsung Galaxy S25",
        "Dell Inspiron Laptop",
        "Sony Headphones",
        "Apple Watch"
    ],

    "Clothing": [
        "Men's T-Shirt",
        "Women's Jeans",
        "Hoodie",
        "Jacket",
        "Kurti"
    ],

    "Books": [
        "Atomic Habits",
        "Deep Work",
        "Harry Potter",
        "The Alchemist",
        "Rich Dad Poor Dad"
    ],

    "Home Appliances": [
        "Microwave Oven",
        "Refrigerator",
        "Washing Machine",
        "Air Conditioner",
        "Mixer Grinder"
    ],

    "Beauty": [
        "Face Wash",
        "Lipstick",
        "Perfume",
        "Shampoo",
        "Moisturizer"
    ],

    "Sports": [
        "Cricket Bat",
        "Football",
        "Badminton Racket",
        "Yoga Mat",
        "Dumbbells"
    ],

    "Toys": [
        "Toy Car",
        "Barbie Doll",
        "Lego Set",
        "Puzzle Game",
        "Teddy Bear"
    ],

    "Grocery": [
        "Rice",
        "Milk",
        "Tea Powder",
        "Sugar",
        "Cooking Oil"
    ],

    "Furniture": [
        "Office Chair",
        "Study Table",
        "Sofa",
        "Bed",
        "Wardrobe"
    ],

    "Accessories": [
        "Backpack",
        "Wallet",
        "Sunglasses",
        "Belt",
        "Cap"
    ]
}

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

order_statuses = [
    "Delivered",
    "Shipped",
    "Processing",
    "Cancelled"
]

price_ranges = {
    "Electronics": (10000, 100000),
    "Clothing": (500, 5000),
    "Books": (200, 1000),
    "Home Appliances": (3000, 80000),
    "Beauty": (200, 3000),
    "Sports": (500, 10000),
    "Toys": (300, 5000),
    "Grocery": (50, 2000),
    "Furniture": (5000, 50000),
    "Accessories": (200, 5000)
}

discount_options = [0, 5, 10, 15, 20, 30]

customer_segments = [
    "Regular",
    "Silver",
    "Gold",
    "Premium"
]

payment_status_mapping = {
    "Delivered": "Success",
    "Shipped": "Success",
    "Processing": "Pending",
    "Cancelled": "Failed"
}

order_status_weights = [80, 10, 7, 3]