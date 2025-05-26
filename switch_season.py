import settings
import utilities
import math

# PAGE

def switch_season_page(supabase):
    if not settings.logged_in:
        credentials = utilities.ask_for_credentials()
        try:
            supabase.auth.sign_in_with_password(credentials)
            print("\nLogged in successfully")
            settings.logged_in = True
        except:
            print(f"\nWrong credentials: {credentials}")
            return
    
    op2 = input("\nManage season:\ncheck (check season status)\nnext (go to next season)\n-> ")
    match op2:
        case "Check" | "check":
            check_season_status(supabase)
        case "Next" | "next":
            next_season(supabase)

    return

# METHODS

def check_season_status(supabase):
    response = supabase.table("stagioni").select("*", count="exact").eq("attiva", True).execute()
    n_active_season = response.count

    if n_active_season == 1:
        anno = response.data[0]["anno"]
        print(f"\nCurrent season: {anno}")
        return True
    else:
        if n_active_season == 0: print("\nERROR: No active season")
        if n_active_season > 1: print("\nERROR: More than 1 active season")

    return

def next_season(supabase):

    op3 = input("\nDo you really want to go to the next season?\nYes\nNo\n-> ")
    match op3:
        case "Yes" | "yes":
            try:
                # controlla che ci sia una sola stagione attiva
                response = supabase.table("stagioni").select("anno", count="exact").eq("attiva", True).execute()
                if response.count == 1:
                    anno = int(response.data[0]["anno"])
                    new_anno = anno+1
                    supabase.table("stagioni").update({"attiva":False}).eq("anno", anno).execute()

                    # attiva la stagione seguente (se non c'è creala)
                    response = supabase.table("stagioni").select("anno", count="exact").eq("anno", new_anno).execute()
                    if response.count > 0:
                        supabase.table("stagioni").update({"attiva":True}).eq("anno", new_anno).execute()
                    else:
                        new_season = {}
                        new_season["anno"] = new_anno
                        new_season["attiva"] = True
                        supabase.table("stagioni").insert(new_season).execute()
                    print(f"\nSeason successfully updated, current season {new_anno}")

                    # aggiungi 500 crediti a tutti
                    response = supabase.table("presidenti").select("nome","cash").execute()
                    for i in range(len(response.data)):
                        cash = response.data[i]["cash"]
                        pres = response.data[i]["nome"]
                        updated_cash = cash + 500
                        new_cash = {}
                        new_cash["cash"] = updated_cash
                        supabase.table("presidenti").update(new_cash).eq("nome", pres).execute()

                        contract_list = supabase.table("contratti").select("anno","prezzo","giocatore","durata").eq("nome_presidente", pres).execute()
                        for j in range(len(contract_list.data)):
                            anno_contratto = contract_list.data[j]["anno"]
                            prezzo = contract_list.data[j]["prezzo"]
                            giocatore = contract_list.data[j]["giocatore"]
                            durata = contract_list.data[j]["durata"]

                            if anno_contratto + durata > new_anno:
                                rinnovo = math.ceil(prezzo * (1 + 0.2*(new_anno - anno_contratto)))
                                new_prezzo_rinnovo = {}
                                new_prezzo_rinnovo["prezzo_rinnovo"] = rinnovo

                                supabase.table("contratti").update(new_prezzo_rinnovo).eq("giocatore", giocatore).execute()
                                
                                updated_cash = updated_cash - rinnovo
                                new_cash = {}
                                new_cash["cash"] = updated_cash
                                supabase.table("presidenti").update(new_cash).eq("nome", pres).execute()
                            else:
                                supabase.table('contratti').delete().eq('giocatore', giocatore).execute()

                    print(f"Cash updated successfully for all presidents")
                    
            except:
                print("\nERROR")
                
        case "No" | "no":
            return
    
    return