import streamlit as st
from supabase import create_client
import pandas as pd

url = "https://vbuffgasrckvlxoilsec.supabase.co"
key = "sb_publishable_RfN-k0VZHztLhO-BFwtwtA_sUwv5rWR"


supabase = create_client(url, key)

st.title("🚲 KGL AI Fleet Dashboard")

sessions = supabase.table("sessions").select("*").execute().data
df = pd.DataFrame(sessions)

st.subheader("Total Diagnostics")
st.metric("Sessions", len(df))

st.subheader("Recent Issues")
st.dataframe(df)

feedback = supabase.table("feedback").select("*").execute().data
df2 = pd.DataFrame(feedback)

if not df2.empty:
    accuracy = df2["was_correct"].mean() * 100
    st.metric("Accuracy %", round(accuracy,2))
