def insert_contract(supabase, pres, ruolo, giocatore, anno, durata, prezzo):
    response = supabase.table("presidenti").select("*").eq("nome", pres).execute()
    print(response)

    """response = supabase.table("contratti").insert({"id_presidente": 1,
                                                "nome_presidente": "Claudio",
                                                "cognome_presidente": "Muroni",
                                                "ruolo": "D",
                                                "giocatore": "Baschirotto",
                                                "anno": 2025,
                                                "durata": 2,
                                                "prezzo": 4
                                                }).execute()"""
    return response