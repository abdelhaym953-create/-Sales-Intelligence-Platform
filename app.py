import streamlit as st
import pandas as pd

# ======================
# إعداد الصفحة
# ======================
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# ======================
# Load Data
# ======================
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_train.csv")
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['ship_date'] = pd.to_datetime(df['ship_date'])
    df['shipping_days'] = df['shipping_time'].astype(str).str.extract('(\d+)').astype(int)
    return df

df = load_data()

# ======================
# Sidebar Navigation
# ======================
page = st.sidebar.radio("📌 Navigate", ["📊 Overview", "📈 Business Q&A"])

st.sidebar.markdown("---")
st.sidebar.info("This dashboard helps turn data into business decisions.")

# ======================
# PAGE 1: OVERVIEW
# ======================
if page == "📊 Overview":



    # ======================
    # HERO SECTION
    # ======================
    st.title("🚀 Sales Intelligence Platform")
    st.markdown("### Transform raw data into **profitable business decisions**")

    st.info("""
    This dashboard provides a complete view of sales performance, customer behavior,
    and logistics efficiency to support data-driven decision making.
    """)

    st.markdown("---")

    # ======================
    # KPIs
    # ======================
    col1, col2, col3, col4 = st.columns(4)

    total_sales = df['sales'].sum()
    total_orders = df.shape[0]
    avg_sales = df['sales'].mean()
    avg_shipping = df['shipping_days'].mean()

    col1.metric("💰 Total Revenue", f"${total_sales:,.0f}")
    col2.metric("📦 Total Orders", total_orders)
    col3.metric("📊 Avg Order Value", f"${avg_sales:.2f}")
    col4.metric("🚚 Avg Shipping Time", f"{avg_shipping:.1f} days")

    st.markdown("---")

    # ======================
    # KEY INSIGHTS (Cards Style)
    # ======================
    st.subheader("🧠 Key Insights")

    col1, col2, col3 = st.columns(3)

    top_category = df.groupby('category')['sales'].sum().idxmax()
    top_region = df.groupby('region')['sales'].sum().idxmax()
    fastest_ship = df.groupby('ship_mode')['shipping_days'].mean().idxmin()

    col1.success(f"🏆 Top Category\n\n**{top_category}** drives the highest revenue.")
    col2.info(f"🌍 Best Region\n\n**{top_region}** leads in total sales.")
    col3.warning(f"🚚 Fastest Shipping\n\n**{fastest_ship}** delivers quickest.")

    st.markdown("---")

    # ======================
    # QUICK VISUALS
    # ======================
    col1, col2 = st.columns(2)

    sales_time = df.groupby('order_date')['sales'].sum().reset_index()
    col1.line_chart(sales_time.set_index('order_date'))

    cat_sales = df.groupby('category')['sales'].sum()
    col2.bar_chart(cat_sales)

    st.markdown("---")

    # ======================
    # BUSINESS MESSAGE
    # ======================
    st.subheader("🎯 Why This Matters")

    st.markdown("""
    - 📈 Identify revenue growth opportunities  
    - 🛍️ Focus on high-performing products  
    - 🌍 Expand in top regions  
    - 🚚 Optimize logistics for better customer experience  
    """)

    st.success("✅ This dashboard is designed to support strategic and operational decisions.")

# ======================
# PAGE 2: BUSINESS Q&A
# ======================
elif page == "📈 Business Q&A":

    st.title("📈 Business Insights & Decision Support")

    st.error("⚡ This section answers critical business questions for decision-makers.")

    # ======================
    # Q1
    # ======================
    st.subheader("1. Which categories generate the most revenue?")

    cat_sales = df.groupby('category')['sales'].sum().sort_values(ascending=False)
    st.bar_chart(cat_sales)

    st.success(f"""
    💡 Insight:
    The top category is **{cat_sales.index[0]}**.

    ✅ Recommendation:
    Focus marketing and inventory on this category.
    """)

    # ======================
    # Q2
    # ======================
    st.subheader("2. How do sales change over time?")

    sales_time = df.groupby('order_date')['sales'].sum()
    st.line_chart(sales_time)

    st.info("""
    💡 Insight:
    Sales vary over time indicating trends or seasonality.

    ✅ Recommendation:
    Plan campaigns during peak periods.
    """)

    # ======================
    # Q3
    # ======================
    st.subheader("3. Which regions perform best?")

    region_sales = df.groupby('region')['sales'].sum().sort_values(ascending=False)
    st.bar_chart(region_sales)

    st.success(f"""
    💡 Insight:
    Top region is **{region_sales.index[0]}**.

    ✅ Recommendation:
    Expand business in strong regions and improve weak ones.
    """)

    # ======================
    # Q4
    # ======================
    st.subheader("4. What are the top products?")

    top_products = df.groupby('product_name')['sales'].sum().nlargest(5)
    st.bar_chart(top_products)

    st.success("""
    💡 Insight:
    Few products drive most revenue.

    ✅ Recommendation:
    Focus on best-performing products.
    """)

    # ======================
    # Q5
    # ======================
    st.subheader("5. Does shipping affect sales?")

    st.scatter_chart(df[['shipping_days', 'sales']])

    st.warning("""
    💡 Insight:
    Shipping speed may impact customer satisfaction.

    ✅ Recommendation:
    Optimize delivery time.
    """)
