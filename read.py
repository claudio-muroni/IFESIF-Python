# PAGE

def read_page(supabase):
    op2 = input("Which table do you want to read?\nP (presidenti)\nC (contratti)\n-> ")
    match op2:
        case "P" | "p" | "presidenti":
            response = read_all_from_table(supabase, "presidenti")
            print(response)
        
        case "C" | "c" | "contratti":
            op3 = input("Which president?\nCLA (Claudio)\nFLA (Flavio)\n-> ")
            match op3:
                case "CLA" | "cla": pres = "Claudio"
                case "FLA" | "fla": pres = "Flavio"
                case _: pres = ""
                    
            if pres!= "":
                response = read_contracts_for_pres(supabase, pres)
                print(response)
            else:
                print(op3 + ": president not available")

        case _:
            print(op2 + ": table not available")
    return

#METHODS

def read_all_from_table(supabase, table):
    return supabase.table(table).select("*").execute()

def read_contracts_for_pres(supabase, pres):
    return supabase.table("contratti").select("ruolo","giocatore","anno","prezzo","durata").eq("nome_presidente", pres).execute()