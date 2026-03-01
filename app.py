import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------- CONFIG ----------------
st.set_page_config(page_title="KGL AI", layout="wide")

# ---------------- DARK MODE TOGGLE ----------------
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

if dark_mode:
    bg = "#0E1117"
    text = "white"
else:
    bg = "#F9FAFB"
    text = "black"

st.markdown(f"""
    <style>
    .main {{
        background-color: {bg};
        color: {text};
    }}
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER / BRANDING ----------------
col1, col2 = st.columns([1, 6])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/1046/1046784.png", width=60)

with col2:
    st.markdown("## ⚡ KGL AI Analytics")
    st.caption("Smart EV Intelligence Platform for Africa")

# ---------------- NAV ----------------
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📊 Dashboard"]
)

# ---------------- MOCK DATA ----------------
np.random.seed(1)
df = pd.DataFrame({
    "country": np.random.choice(["Rwanda", "Kenya", "Uganda"], 300),
    "station": np.random.choice(["Kigali", "Nairobi", "Kampala"], 300),
    "swaps": np.random.randint(10, 100, 300),
    "temperature": np.random.randint(20, 60, 300),
    "soc": np.random.randint(20, 100, 300),
    "lat": np.random.uniform(-2, 1, 300),
    "lon": np.random.uniform(29, 37, 300),
    "date": pd.date_range("2024-01-01", periods=300)
})

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":

    st.markdown("### 🚀 Powering Africa’s EV Ecosystem")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **KGL AI helps EV companies:**
        - Optimize battery performance  
        - Predict failures using AI  
        - Monitor stations in real-time  
        - Reduce operational costs  
        """)

        if st.button("📅 Book Demo"):
            st.success("Demo request sent! 🚀")

    with col2:
        st.image("https://images.unsplash.com/photo-1581092335397-9fa341108f5b", use_column_width=True)

    st.markdown("---")

    # KPIs for investors
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Swaps", "120K", "+18%")
    col2.metric("Active Stations", "45", "+12%")
    col3.metric("Failure Reduction", "32%", "+8%")

# ---------------- DASHBOARD ----------------
elif page == "📊 Dashboard":

    st.markdown("## 📊 Live EV Analytics Dashboard")

    # FILTERS
    col1, col2 = st.columns(2)

    with col1:
        country = st.selectbox("Country", df["country"].unique())

    with col2:
        station = st.selectbox("Station", df["station"].unique())

    filtered = df[
        (df["country"] == country) &
        (df["station"] == station)
    ]

    # ---------------- KPI CARDS ----------------
    total_swaps = filtered["swaps"].sum()
    avg_temp = filtered["temperature"].mean()
    avg_soc = filtered["soc"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Swaps", total_swaps, "+12%")
    col2.metric("Avg Temp", round(avg_temp, 1), "-2%")
    col3.metric("Avg SOC", round(avg_soc, 1), "+5%")
    col4.metric("Stations", filtered["station"].nunique())

    st.markdown("---")

    # ---------------- CHARTS ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Swap Trends")
        trend = filtered.groupby("date")["swaps"].sum()
        fig = px.line(trend, title="Swaps Over Time")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🌡 Temperature Distribution")
        fig = px.histogram(filtered, x="temperature")
        st.plotly_chart(fig, use_container_width=True)

    # ---------------- MAP ----------------
    st.subheader("🌍 Africa EV Activity Map")

    map_fig = px.scatter_mapbox(
        filtered,
        lat="lat",
        lon="lon",
        size="swaps",
        color="temperature",
        zoom=4,
        mapbox_style="carto-positron"
    )

    st.plotly_chart(map_fig, use_container_width=True)

    # ---------------- AI INSIGHT ----------------
    st.markdown("### 🤖 AI Insight")

    risk = (filtered["temperature"] > 50).sum()

    st.info(f"{risk} batteries are at high failure risk ⚠️")
