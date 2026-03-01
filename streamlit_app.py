import streamlit as st
import pandas as pd
import plotly.express as px
from supabase import create_client
from openai import OpenAI

# -----------------------
# CONFIG
# -----------------------
st.set_page_config(
    page_title="KGL AI Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🚀 KGL AI Analytics Dashboard (Demo)")

# -----------------------
# CONNECTIONS
# -----------------------
SUPABASE_URL = st.secrets["https://vbuffgasrckvlxoilsec.supabase.co"]
SUPABASE_KEY = st.secrets["sb_publishable_RfN-k0VZHztLhO-BFwtwtA_sUwv5rWR"]
OPENAI_API_KEY = st.secrets["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"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
client = OpenAI(api_key=OPENAI_API_KEY)

# -----------------------
# LOAD DATA
# -----------------------
@st.cache_data(ttl=60)
def load_data():
    careers = supabase.table("careers").select("*").execute().data
    users = supabase.table("users").select("*").execute().data
    contacts = supabase.table("contact_messages").select("*").execute().data

    return (
        pd.DataFrame(careers),
        pd.DataFrame(users),
        pd.DataFrame(contacts),
    )

careers, users, contacts = load_data()

# -----------------------
# KPI METRICS
# -----------------------
st.subheader("📊 Platform Overview")

col1, col2, col3 = st.columns(3)

col1.metric("👨‍💼 Applications", len(careers))
col2.metric("👥 Users", len(users))
col3.metric("📩 Contacts", len(contacts))

st.divider()

# -----------------------
# AI SCORING
# -----------------------
def score_candidate(cv_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Score this CV from 0 to 100. Only return a number."},
                {"role": "user", "content": cv_text},
            ],
        )
        return float(response.choices[0].message.content.strip())
    except:
        return 50

st.subheader("🧠 AI Candidate Scoring")

if st.button("Run AI Scoring"):
    with st.spinner("Scoring candidates..."):
        for _, row in careers.iterrows():
            if pd.isna(row.get("ai_score")):
                score = score_candidate(row.get("cv_text", ""))
                supabase.table("career_applications").update(
                    {"ai_score": score}
                ).eq("id", row["id"]).execute()

    st.success("✅ AI scoring completed")
    st.cache_data.clear()

st.divider()

# -----------------------
# APPLICATION ANALYTICS
# -----------------------
st.subheader("📄 Applications Insights")

if not careers.empty:

    careers["created_at"] = pd.to_datetime(careers["created_at"])

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(
            careers["role"].value_counts().reset_index(),
            x="index",
            y="role",
            title="Applications by Role",
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        if "ai_score" in careers.columns:
            fig2 = px.histogram(
                careers,
                x="ai_score",
                nbins=20,
                title="AI Score Distribution",
            )
            st.plotly_chart(fig2, use_container_width=True)

    trend = careers.groupby(careers["created_at"].dt.date).size().reset_index(name="count")

    fig3 = px.line(trend, x="created_at", y="count", title="Applications Over Time")
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# -----------------------
# USER GROWTH
# -----------------------
st.subheader("👥 User Growth")

if not users.empty:
    users["created_at"] = pd.to_datetime(users["created_at"])

    growth = users.groupby(users["created_at"].dt.date).size().reset_index(name="count")

    fig4 = px.area(growth, x="created_at", y="count", title="User Growth Trend")
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# -----------------------
# CONTACT INSIGHTS
# -----------------------
st.subheader("📬 Contact Insights")

if not contacts.empty:
    fig5 = px.pie(
        contacts["subject"].value_counts().reset_index(),
        names="index",
        values="subject",
        title="Contact Topics Distribution",
    )
    st.plotly_chart(fig5, use_container_width=True)

st.divider()

# -----------------------
# TOP CANDIDATES
# -----------------------
st.subheader("🏆 Top Candidates")

if "ai_score" in careers.columns:
    top = careers.sort_values(by="ai_score", ascending=False).head(10)
    st.dataframe(top, use_container_width=True)

# -----------------------
# RAW DATA (OPTIONAL)
# -----------------------
with st.expander("🗂 View Raw Data"):
    tab1, tab2, tab3 = st.tabs(["Applications", "Users", "Contacts"])

    with tab1:
        st.dataframe(careers)

    with tab2:
        st.dataframe(users)

    with tab3:
        st.dataframe(contacts)

# -----------------------
# EXPORT
# -----------------------
st.subheader("⬇️ Export Data")

st.download_button(
    "Download Applications CSV",
    careers.to_csv(index=False),
    "applications.csv",
)

st.caption("🔄 Auto-refresh every 60s | Demo Mode Enabled")
