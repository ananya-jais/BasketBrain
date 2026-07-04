import pandas as pd


def load_data():
    return pd.read_csv("data/grocery_prices.csv")


def search_products(df, grocery_list):
    return df[df["Product"].isin(grocery_list)]

def calculate_store_totals(filtered_df):

    totals = {
        "Blinkit": filtered_df["Blinkit Price"].sum(),
        "Zepto": filtered_df["Zepto Price"].sum(),
        "Instamart": filtered_df["Instamart Price"].sum(),
        "BigBasket": filtered_df["BigBasket Price"].sum()
    }

    return totals

def recommend_store(totals):

    best_store = min(totals, key=totals.get)

    best_price = totals[best_store]

    return best_store, best_price

def calculate_savings(totals):

    highest = max(totals.values())

    lowest = min(totals.values())

    savings = highest - lowest

    return savings

def calculate_delivery(filtered_df):

    delivery = {

        "Blinkit": filtered_df["Blinkit Delivery"].mean(),

        "Zepto": filtered_df["Zepto Delivery"].mean(),

        "Instamart": filtered_df["Instamart Delivery"].mean(),

        "BigBasket": filtered_df["BigBasket Delivery"].mean()

    }

    return delivery