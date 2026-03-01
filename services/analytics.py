import pandas as pd
from db.connection import get_connection

def load_data():
    conn = get_connection()
    query = "SELECT * FROM contact_messages;"
    return pd.read_sql(query, conn)

def compute_metrics(df):
    return {
        "total_swaps": len(df),
        "names": len(df["name"]),
        "email": len(df["email"])
    }
