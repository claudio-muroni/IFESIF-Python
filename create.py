import settings
import utilities

def create_page(supabase):
    if not settings.logged_in:
        credentials = utilities.ask_for_credentials()
        try:
            supabase.auth.sign_in_with_password(credentials)
            print("Logged in successfully")
            settings.logged_in = True
        except:
            print(f"Wrong credentials: {credentials}")
            return
    
    create_contract(supabase)
    return

def create_contract(supabase):
    pres = input("Presidente -> ")
    ruolo = input("Ruolo -> ")
    giocatore = input("Giocatore -> ")
    durata = input("Durata contratto -> ")
    prezzo = input("Prezzo d'acquisto -> ")
    
    try:
        response = supabase.table("presidenti").select("*").eq("nome", pres).execute()
        id = response.data[0]["id"]
        cognome = response.data[0]["cognome"]
        cash = response.data[0]["cash"]
        new_cash = {}
        new_cash["cash"] = cash - int(prezzo)
    except:
        print("\nError retrieving president's data")
        return

    response = supabase.table("stagioni").select("*").eq("attiva", True).execute()
    anno = response.data[0]["anno"]

    response = supabase.table("contratti").select("*", count="exact").eq("giocatore", giocatore).execute()
    if response.count == 0 and new_cash["cash"] >= 0:
        try:
            contract = {}
            contract["id_presidente"] = id
            contract["nome_presidente"] = pres
            contract["cognome_presidente"] = cognome
            contract["ruolo"] = ruolo
            contract["giocatore"] = giocatore
            contract["anno"] = anno
            contract["durata"] = durata
            contract["prezzo"] = prezzo
            supabase.table("contratti").insert(contract).execute()
            supabase.table("presidenti").update(new_cash).eq("nome", pres).execute()
            print("\nContract added successfully")
        except:
            print("\nERROR")
            return
    else:
        print(f"Player {giocatore} already in DB")
        return

    return