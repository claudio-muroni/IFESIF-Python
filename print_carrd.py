import settings
import utilities

# PAGE
def print_page(supabase):
    op2 = input("\nWhat do you want to print?\nCC (Carrd contracts)\n-> ")
    match op2:
        case "CC" | "cc" | "carrd":
            print_carrd_contracts(supabase)
    return

#METHODS
def print_carrd_contracts(supabase):

    response = supabase.table("presidenti").select("cognome").eq("attivo", True).execute()
    for i in range(len(response.data)):
        pres = response.data[i]["cognome"]
        with open(f"carrd_{pres}.txt", 'w') as f:
            f.write("")

        contract_list = supabase.table("contratti").select("ruolo","anno","prezzo","prezzo_rinnovo","giocatore","durata").eq("cognome_presidente", pres).order("ruolo").execute()
        for j in range(len(contract_list.data)):
            carrd_row = ""
            ruolo = contract_list.data[j]["ruolo"]
            match ruolo:
                case 'P':
                    carrd_row = carrd_row + "[P]{orange}\n"
                case 'D':
                    carrd_row = carrd_row + "[D]{green}\n"
                case 'C':
                    carrd_row = carrd_row + "[C]{blue}\n"
                case 'A':
                    carrd_row = carrd_row + "[A]{red}\n"
            
            giocatore = contract_list.data[j]["giocatore"]
            carrd_row = carrd_row + f"{giocatore}\n"

            prezzo = contract_list.data[j]["prezzo"]
            carrd_row = carrd_row + f"{prezzo}\n"

            prezzo_rinnovo = contract_list.data[j]["prezzo_rinnovo"]
            carrd_row = carrd_row + f"{prezzo_rinnovo}\n"

            anno_contratto = contract_list.data[j]["anno"]
            carrd_row = carrd_row + f"{anno_contratto-1}/{anno_contratto}\n"
            
            durata = contract_list.data[j]["durata"]
            carrd_row = carrd_row + f"{durata}\n\n"

            with open(f"carrd_{pres}.txt", 'a') as f:
                f.write(carrd_row)
            

    
    return