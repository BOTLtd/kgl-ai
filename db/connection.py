import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        # host=os.getenv("db.vbuffgasrckvlxoilsec.supabase.co"),
        host=os.getenv(" aws-1-eu-west-1.pooler.supabase.com"),
        database="postgres",
        user="postgres",
        password=os.getenv("0AjVnugLnaFCeQbk"),
        port=5432
    )
