import streamlit as st
from services.analytics import load_data, compute_metrics

st.title("📊 Dashboard")

df = load_data()

# Filters
country = st.selectbox("name", df["email"].unique())
df = df[df["name"] == name]

# Metrics
metrics = compute_metrics(df)

col1, col2, col3 = st.columns(3)
col1.metric("name", metrics["name"])
col2.metric("email", round(metrics["email"], 2))
# col3.metric("Avg SOC", round(metrics["avg_soc"], 2))

# Trend
df["time"] = pd.to_datetime(df["created_at"])
trend = df.groupby(df["created_at"].dt.date).size()

st.line_chart(trend)
