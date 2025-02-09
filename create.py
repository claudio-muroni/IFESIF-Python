import pandas

def insert_contract(supabase):
    pres = input("Presidente -> ")
    ruolo = input("Ruolo -> ")
    giocatore = input("Giocatore -> ")
    durata = input("Durata contratto -> ")
    prezzo = input("Prezzo d'acquisto -> ")
    
    response = supabase.table("presidenti").select("*").eq("nome", pres).execute()
    id = response.data[0]["id"]
    cognome = response.data[0]["cognome"]

    response = supabase.table("stagioni").select("*").eq("attiva", True).execute()
    anno = response.data[0]["anno"]

    response = supabase.table("contratti").select("*", count="exact").eq("giocatore", giocatore).execute()
    if response.count == 0:
        contract = {}
        contract["id_presidente"] = id
        contract["nome_presidente"] = pres
        contract["cognome_presidente"] = cognome
        contract["ruolo"] = ruolo
        contract["giocatore"] = giocatore
        contract["anno"] = anno
        contract["durata"] = durata
        contract["prezzo"] = prezzo
        response = supabase.table("contratti").insert(contract).execute()
    else:
        print("giocatore già presente")

    return response