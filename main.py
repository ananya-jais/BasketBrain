import streamlit as st
import pandas as pd
import optimizer
import gemini_helper
import plotly.express as px

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="BasketBrain",
    page_icon="🛒",
    layout="wide"
)

# -------------------------------
# Header
# -------------------------------

st.title("🛒 BasketBrain")

st.markdown("""
### AI-Powered Grocery Decision Intelligence

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
# Sidebar
# -------------------------------

with st.sidebar:

    st.title("🛒 BasketBrain")

    st.caption("AI Grocery Shopping Assistant")

    st.success("💸 Compare Prices")

    st.success("⚡ Save Time")

    st.success("🧠 Shop Smarter")

    st.divider()

    st.markdown("## 📊 Quick Stats")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Stores", "4")

    with col2:
        st.metric("AI", "Gemini")

    st.markdown("---")

    st.markdown("## 🏪 Supported Stores")

    st.success("🟢 Blinkit")

    st.success("🟣 Zepto")

    st.success("🟠 Instamart")

    st.success("🔵 BigBasket")

    st.markdown("---")

    st.markdown("## 🧠 BasketBrain Engine")

    st.write("✅ Price Intelligence")

    st.write("✅ AI Recommendation")

    st.write("✅ Delivery Analysis")

    st.write("✅ Smart Scheduling")

    st.write("✅ Savings Calculator")

    st.markdown("---")

    st.info("🏆 Google GenAI Hackathon 2026")

    st.caption("Made with ❤️ using Python, Streamlit & Gemini")

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

        best_store, best_price = optimizer.recommend_store(totals)
        savings = optimizer.calculate_savings(totals)

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
        st.divider()

        # -------------------------------
        # Recommendation Card
        # -------------------------------
        st.markdown(
            f"""
        <div style="
        background:linear-gradient(135deg,#00C853,#43A047);
        padding:30px;
        border-radius:20px;
        color:white;
        ">

        <h2>🏆 Best Store Recommendation</h2>

        <h1>{best_store}</h1>

        <h3>Total Basket Cost: ₹{best_price}</h3>

        <h4>You Save ₹{savings}</h4>

        <p>
        BasketBrain analyzed pricing across all supported stores and selected the most cost-effective option.
        </p>

        </div>
        """, 
        unsafe_allow_html=True
        )
        st.divider()

        # ------------------------------
        # Gemini Recommendation
        # ------------------------------
        st.markdown("## 🤖 BasketBrain AI")
        with st.spinner("🧠 BasketBrain AI is analyzing prices..."):
            analysis = gemini_helper.get_ai_recommendation(
                filtered,
                totals,
                delivery
                )
        st.info(analysis)
        st.divider()

        # ----------------------------
        # Scheduler
        # ----------------------------

        st.markdown("---")
        st.subheader("📅 Schedule this Basket")
        schedule = st.checkbox("Yes, I want to schedule this basket")
        if schedule:
            col1, col2 = st.columns(2)
            with col1:
                schedule_date = st.date_input("Select Date")
            with col2:
                schedule_time = st.time_input("Select Time")
            repeat = st.selectbox(
                "Repeat",
                [
                    "No Repeat",
                    "Weekly",
                    "Monthly"
                ]
            )
            if st.button("📅 Schedule Basket"):
                st.success(f"""
                ### ✅ Basket Scheduled Successfully
                📅 **Date:** {schedule_date}
                🕒 **Time:** {schedule_time}
                🔁 **Repeat:** {repeat}
                BasketBrain will compare the latest prices before your planned purchase and provide updated shopping insights.""")
    
        st.markdown("---")
        st.subheader("🔔 Smart Reminder")
        st.info("""
        💡 BasketBrain will re-analyze your basket at the scheduled time.

        Before you place the order, it will:

        ✅ Compare the latest prices

        ✅ Highlight the cheapest platform

        ✅ Show updated savings

        ✅ Recommend the best store based on price and delivery

        This helps you make the best purchase decision using the most recent pricing.""")
        st.divider()

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
        fig = px.bar(
            chart_df,
            x="Store",
            y="Price",
            color="Store",
            text="Price",
            color_discrete_map={
                "Blinkit": "#00C853",
                "Zepto": "#8E44AD",
                "Instamart": "#FF6F00",
                "BigBasket": "#1E88E5"
            }
        )
        fig.update_layout(
            showlegend=False,
            height=420,
            xaxis_title="",
            yaxis_title="Price (₹)",
            plot_bgcolor="white"
        )
        fig.update_traces(
            texttemplate="₹%{text}",
            textposition="outside"
        )
        st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Dataset
# -------------------------------

with st.expander("🔧 Sample Dataset"):

    st.dataframe(df, use_container_width=True)


st.markdown("---")

st.caption(
"Built using Python • Streamlit • Google Gemini • Pandas"
)