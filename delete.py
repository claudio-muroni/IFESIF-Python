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

    delete_contract(supabase)
    return

# METHODS

def delete_contract(supabase):
    giocatore = input("Giocatore -> ")
    
    response = supabase.table("contratti").select("*", count="exact").eq("giocatore", giocatore).execute()
    if response.count != 0:
        try:
            supabase.table('contratti').delete().eq('giocatore', giocatore).execute()
            print("Contract deleted successfully")
        except:
            print("\nERROR")
    else:
        print(f"Player {giocatore} not in DB")
        return
    
    return