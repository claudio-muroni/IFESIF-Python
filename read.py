def read_all_from_table(supabase, table):
    return supabase.table(table).select("*").execute()