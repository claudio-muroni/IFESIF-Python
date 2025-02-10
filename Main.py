import settings
import utilities
import create
import read
import update
import delete
from supabase import create_client, Client

supabase: Client = create_client(settings.url, settings.key)
logged_in = False

while True:
    op = input("\n\nDigit operations:\nC (create)\nR (read)\nU (update)\nD (delete)\nE (exit)\n-> ")
    match op:
        case "C" | "c" | "create":
            if not logged_in:
                credentials = utilities.ask_for_credentials()
                try:
                    supabase.auth.sign_in_with_password(credentials)
                    print("Logged in successfully")
                    logged_in = True
                except:
                    print(f"Wrong credentials: {credentials}")
                    continue
            
            create.create_contract(supabase)

        case "R" | "r" | "read":
            op2 = input("Which table do you want to read?\nP (presidenti)\nC (contratti)\n-> ")
            match op2:
                case "P" | "p" | "presidenti":
                    response = read.read_all_from_table(supabase, "presidenti")
                    print(response)
                
                case "C" | "c" | "contratti":
                    table = "contratti"
                    op3 = input("Which president?\nCLA (Claudio)\nFLA (Flavio)\n-> ")
                    match op3:
                        case "CLA" | "cla": pres = "Claudio"
                        case "FLA" | "fla": pres = "Flavio"
                        case _: pres = ""
                            
                    if pres!= "":
                        response = read.read_contracts_for_pres(supabase, pres)
                        print(response)
                    else:
                        print(op3 + ": president not available")

                case _:
                    print(op2 + ": table not available")
        
        case "U" | "u" | "update":
            if not logged_in:
                credentials = utilities.ask_for_credentials()
                try:
                    supabase.auth.sign_in_with_password(credentials)
                    print("Logged in successfully")
                    logged_in = True
                except:
                    print(f"Wrong credentials: {credentials}")
                    continue
            
            op3 = input("Update cash for\n1 (one presidente)\nAll (all presidents)\nEx (exchange)\n-> ")
            match op3:
                case "1":
                    update.update_cash_for_pres(supabase)
                case "All" | "all":
                    update.update_cash_for_all(supabase)
                case "Ex" | "ex":
                    update.exchange_cash(supabase)
        
        case "D" | "d" | "delete":
            if not logged_in:
                credentials = utilities.ask_for_credentials()
                try:
                    supabase.auth.sign_in_with_password(credentials)
                    print("Logged in successfully")
                    logged_in = True
                except:
                    print(f"Wrong credentials: {credentials}")
                    continue

            delete.delete_contract(supabase)

        case "E" | "e" | "exit":
            print("Terminate")
            break
            
        case _:
            print(op + ": operation not available")
    

