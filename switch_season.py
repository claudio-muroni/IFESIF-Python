import settings
import utilities

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
            response = supabase.table("stagioni").select("anno", count="exact").eq("attiva", True).execute()
            if response.count == 1:
                anno = int(response.data[0]["anno"])
                supabase.table("stagioni").update({"attiva":False}).eq("anno", anno).execute()

                response = supabase.table("stagioni").select("anno", count="exact").eq("anno", anno+1).execute()
                if response.count > 0:
                    supabase.table("stagioni").update({"attiva":True}).eq("anno", anno+1).execute()
                else:
                    new_season = {}
                    new_season["anno"] = anno+1
                    new_season["attiva"] = True
                    supabase.table("stagioni").insert(new_season).execute()

                print(f"\nSeason successfully updated, current season {anno+1}")

        case "No" | "no":
            return
    
    return