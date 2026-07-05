import streamlit as st
import pandas as pd
import optimizer
import gemini_helper

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="BasketBrain",
    page_icon="🛒",
    layout="wide"
)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:

    st.markdown("""
    <div style="
    padding:30px;
    border-radius:20px;
    background:linear-gradient(135deg,#4F8BF9,#6B5BFF);
    color:white;
    ">
    <h1>🛒 BasketBrain</h1>
    <h4>
    Compare grocery prices across Blinkit,
    Zepto, Instamart and BigBasket.
    </h4>
    <p>
    Save money.
    Save time.
    Shop smarter.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🚀 Features")
    st.success("Price Comparison")
    st.success("Delivery Time")
    st.success("Savings Calculator")
    st.success("AI Recommendation")
    st.markdown("---")
    st.info("Google GenAI Hackathon 2026")

# -------------------------------
# Header
# -------------------------------

st.title("🛒 BasketBrain")

st.markdown("""
### Your AI Grocery Decision Assistant

Compare grocery prices across **Blinkit**, **Zepto**, **Instamart** and **BigBasket**.

Save money. Save time. Shop smarter.
""")

# -------------------------------
# Load Dataset
# -------------------------------

df = optimizer.load_data()
col1, col2, col3 = st.columns(3)

col1.metric("🛍 Products", len(df))
col2.metric("🏪 Stores", 4)
col3.metric("📦 Categories", df["Category"].nunique())

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
# Compare Button
# -------------------------------

if st.button("🛒 Compare My Basket"):

    grocery_list = []

    for item in user_input.split("\n"):
        item = item.strip().title()

        if item != "":
            grocery_list.append(item)

    filtered = optimizer.search_products(df, grocery_list)

    if filtered.empty:

        st.error("No matching products found.")

    else:

        st.markdown("## 🛍 Basket Details")

        st.dataframe(
            filtered,
            use_container_width=True,
            hide_index=True
        )

        totals = optimizer.calculate_store_totals(filtered)
        delivery = optimizer.calculate_delivery(filtered)

        st.markdown("## 💰 Store Comparison")

        col1, col2, col3, col4 = st.columns(4)

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

        # -------------------------------
        # Recommendation Card
        # -------------------------------
        best_store, best_price = optimizer.recommend_store(totals)
        savings = optimizer.calculate_savings(totals)
        st.markdown(
        f"""
        <div style="
        background:#E8FFF0;
        padding:25px;
        border-radius:18px;
        border-left:8px solid #2ECC71;
        margin-top:20px;
        ">

        <h2>🏆 Recommended Store</h2>

        <h1 style="margin-bottom:5px;">
        {best_store}
        </h1>

        <h3>💰 Total Cost : ₹{best_price}</h3>

        <h4>🎉 Estimated Savings : ₹{savings}</h4>
        </div>
        """,
        unsafe_allow_html=True
        )

        st.markdown("## 🤖 BasketBrain AI")
        with st.spinner("Analyzing your basket..."):
            analysis = gemini_helper.get_ai_recommendation(
                filtered,
                totals,
                delivery
            )
        st.info(analysis)

        # -------------------------------
        # Bar Chart
        # -------------------------------

        chart_df = pd.DataFrame({

            "Store": [
                "Blinkit",
                "Zepto",
                "Instamart",
                "BigBasket"
            ],

            "Price": [
                totals["Blinkit"],
                totals["Zepto"],
                totals["Instamart"],
                totals["BigBasket"]
            ]

        })

        st.markdown("## 📊 Basket Cost Comparison")

        st.bar_chart(
            chart_df.set_index("Store")
        )

st.divider()

# -------------------------------
# Dataset
# -------------------------------

with st.expander("🔧 Developer Dataset"):

    st.dataframe(df, use_container_width=True)