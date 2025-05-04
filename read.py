import pandas as pd

# PAGE

def read_page(supabase):
    op2 = input("\nWhich table do you want to read?\nP (presidenti)\nC (contratti)\nR (rankings)\n-> ")
    match op2:
        case "P" | "p" | "presidenti":
            read_presidents(supabase)
            
        case "C" | "c" | "contratti":
            op3 = input("Which president?\nCLA (Claudio)\nFLA (Flavio)\n-> ")
            match op3:
                case "CLA" | "cla": pres = "Claudio"
                case "FLA" | "fla": pres = "Flavio"
                case _: pres = ""
                    
            if pres!= "":
                read_contracts_for_pres(supabase, pres)
                
            else:
                print(op3 + ": president not available")
        
        case "R" | "r" | "rankings":
            year = input("Which year? -> ")
            comp = input("Which competition? -> ")

            read_rankings_for_year_competition(supabase, year, comp)
            

        case _:
            print(op2 + ": table not available")
    return

#METHODS

def read_presidents(supabase):
    response = supabase.table("presidenti").select("nome", "cognome", "cash").execute()
    df = pd.DataFrame(response.data)
    print(df)

    return

def read_contracts_for_pres(supabase, pres):
    response = supabase.table("contratti").select("ruolo","giocatore","anno","prezzo","prezzo_rinnovo","durata").eq("nome_presidente", pres).execute()
    df = pd.DataFrame(response.data)
    print(df)
    
    return

def read_rankings_for_year_competition(supabase, year, comp):
    response = supabase.table("classifiche").select("*").eq("anno", year).eq("competizione", comp).execute()
    df = pd.DataFrame(response.data)
    print(df)
    
    return