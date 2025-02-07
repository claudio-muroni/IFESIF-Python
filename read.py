def read_all_from_table(supabase, table):
    return supabase.table(table).select("*").execute()

def read_contracts_for_pres(supabase, pres):
    return supabase.table("contratti").select("ruolo","giocatore","anno","prezzo","durata").eq("nome_presidente", pres).execute()