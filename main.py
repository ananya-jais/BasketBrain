import streamlit as st
import optimizer

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="BasketBrain",
    page_icon="🛒",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------
st.title("🛒 BasketBrain")
st.subheader("AI Shopping Decision Engine")

# -------------------------------
# Load Dataset
# -------------------------------
df = optimizer.load_data()

st.success("Dataset Loaded Successfully ✅")

st.divider()

# -------------------------------
# User Input
# -------------------------------
user_input = st.text_area(
    "Enter Grocery Items (One Per Line)",
    height=150,
    placeholder="Milk\nBread\nRice\nEggs"
)

# -------------------------------
# Button
# -------------------------------
if st.button("Find Products"):

    grocery_list = []

    for item in user_input.split("\n"):
        item = item.strip().title()

        if item != "":
            grocery_list.append(item)

    filtered = optimizer.search_products(df, grocery_list)

    if filtered.empty:
        st.error("No matching products found.")
    else:
        st.success("Products Found ✅")
        st.dataframe(filtered)
        totals = optimizer.calculate_store_totals(filtered)
        delivery = optimizer.calculate_delivery(filtered)
        st.subheader("💰 Price Comparison")
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("🟢 Blinkit", f"₹{totals['Blinkit']}")
        col2.metric("🟣 Zepto", f"₹{totals['Zepto']}")
        col3.metric("🟠 Instamart", f"₹{totals['Instamart']}")
        col4.metric("🔵 BigBasket", f"₹{totals['BigBasket']}")
        col1.metric(
             "🟢 Blinkit",
             f"₹{totals['Blinkit']}",
             f"{delivery['Blinkit']:.0f} mins"
        )
        col2.metric(
             "🟣 Zepto",
             f"₹{totals['Zepto']}",
             f"{delivery['Zepto']:.0f} mins"
        )
        col3.metric(
             "🟠 Instamart",
             f"₹{totals['Instamart']}",
             f"{delivery['Instamart']:.0f} mins"
        )
        col4.metric(
            "🔵 BigBasket",
            f"₹{totals['BigBasket']}",
            f"{delivery['BigBasket']:.0f} mins"
        )

        best_store, best_price = optimizer.recommend_store(totals)
        savings = optimizer.calculate_savings(totals)
        st.success(
            f"""
        🏆 Recommended Store: **{best_store}**
        💰 Total Cost: ₹{best_price}
        🎉 You Save: ₹{savings}"""
        )

st.divider()

# -------------------------------
# Full Dataset
# -------------------------------
with st.expander("View Complete Dataset"):
    st.dataframe(df)