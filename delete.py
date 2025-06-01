import settings
import utilities

# PAGE

def delete_page(supabase):
    if not settings.logged_in:
        credentials = utilities.ask_for_credentials()
        try:
            supabase.auth.sign_in_with_password(credentials)
            print("Logged in successfully")
            settings.logged_in = True
        except:
            print(f"Wrong credentials: {credentials}")
            return

    op2 = input("\nD (delete)\nR (refund)\n-> ")
    match op2:
        case "D" | "d" | "delete":
            delete_contract(supabase)
        case "R" | "r" | "refund":
            refund_contract(supabase)
        case _:
            print(op2 + ": operation not available")

    return

# METHODS

def delete_contract(supabase):
    giocatore = input("Giocatore -> ")
    
    response = supabase.table("contratti").select("*", count="exact").eq("giocatore", giocatore).execute()
    if response.count != 0:
        try:
            supabase.table('contratti').delete().eq('giocatore', giocatore).execute()
            print(f"Contract deleted successfully\n{giocatore} +0")
        except:
            print("\nERROR")
    else:
        print(f"Player {giocatore} not in DB")
        return
    
    return

def refund_contract(supabase):

    giocatore = input("Giocatore -> ")
    response = supabase.table("contratti").select("*", count="exact").eq("giocatore", giocatore).execute()
    if response.count != 0:
        try:
            pres = response.data[0]["nome_presidente"]
            cash_diff = response.data[0]["prezzo_rinnovo"]

            response = supabase.table("presidenti").select("*").eq("nome", pres).execute()
            cash = response.data[0]["cash"]
            new_cash = {}
            new_cash["cash"] = cash + int(cash_diff)
            
            supabase.table("presidenti").update(new_cash).eq("nome", pres).execute()
            supabase.table('contratti').delete().eq('giocatore', giocatore).execute()

            print(f"Contract refunded successfully\n{pres}: {giocatore} +{cash_diff}")
        except:
            print("\nERROR")
    else:
        print(f"Player {giocatore} not in DB")
        return

    return