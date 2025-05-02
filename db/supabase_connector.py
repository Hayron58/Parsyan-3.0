from supabase import create_client
import os

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

def save_to_db(companies):
    for c in companies:
        supabase.table("companies").insert(c).execute()
