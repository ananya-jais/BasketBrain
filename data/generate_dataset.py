import pandas as pd
import random

products = [
    ("Milk", "Dairy"),
    ("Bread", "Bakery"),
    ("Eggs", "Dairy"),
    ("Butter", "Dairy"),
    ("Cheese", "Dairy"),
    ("Rice", "Staples"),
    ("Wheat Flour", "Staples"),
    ("Sugar", "Staples"),
    ("Salt", "Staples"),
    ("Cooking Oil", "Staples"),
    ("Tomato", "Vegetables"),
    ("Potato", "Vegetables"),
    ("Onion", "Vegetables"),
    ("Carrot", "Vegetables"),
    ("Capsicum", "Vegetables"),
    ("Apple", "Fruits"),
    ("Banana", "Fruits"),
    ("Orange", "Fruits"),
    ("Mango", "Fruits"),
    ("Grapes", "Fruits"),
    ("Biscuits", "Snacks"),
    ("Chips", "Snacks"),
    ("Chocolate", "Snacks"),
    ("Noodles", "Snacks"),
    ("Pasta", "Snacks"),
    ("Shampoo", "Personal Care"),
    ("Soap", "Personal Care"),
    ("Toothpaste", "Personal Care"),
    ("Face Wash", "Personal Care"),
    ("Body Lotion", "Personal Care"),
    ("Detergent", "Cleaning"),
    ("Floor Cleaner", "Cleaning"),
    ("Dishwash Liquid", "Cleaning"),
    ("Garbage Bags", "Cleaning"),
    ("Toilet Cleaner", "Cleaning"),
]

rows = []

for product, category in products:

    base_price = random.randint(20, 400)

    rows.append({
        "Product": product,
        "Category": category,

        "Blinkit Price": base_price + random.randint(-15,15),
        "Blinkit Delivery": random.randint(10,20),

        "Zepto Price": base_price + random.randint(-15,15),
        "Zepto Delivery": random.randint(10,25),

        "Instamart Price": base_price + random.randint(-15,15),
        "Instamart Delivery": random.randint(10,25),

        "BigBasket Price": base_price + random.randint(-15,15),
        "BigBasket Delivery": random.randint(20,45),

        "Rating": round(random.uniform(4.0,5.0),1)
    })

df = pd.DataFrame(rows)

df.to_csv("data/grocery_prices.csv", index=False)

print("Dataset Created Successfully!")