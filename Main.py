import os
from supabase import create_client, Client

url: str = os.environ.get("ifesif_supabase_url")
key: str = os.environ.get("ifesif_supabase_key")
supabase: Client = create_client(url, key)

response = supabase.table("presidenti").select("*").execute()
print(response)