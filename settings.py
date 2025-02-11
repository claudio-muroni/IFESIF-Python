import os

url: str = os.environ.get("ifesif_supabase_url")
key: str = os.environ.get("ifesif_supabase_key")

logged_in = False