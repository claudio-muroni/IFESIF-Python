import settings
import utilities
import create
import read
import update
from supabase import create_client, Client

supabase: Client = create_client(settings.url, settings.key)

while True:
    op = input("\n\nDigit operations:\nC (create)\nR (read)\nU (update)\nE (exit)\n-> ")
    match op:
        case "C" | "c" | "create":
            credentials = utilities.ask_for_credentials
            try:
                supabase.auth.sign_in_with_password(credentials)
                print("Logged in successfully")
            except:
                print(f"Wrong credentials: {credentials}")
                continue
            
            create.insert_contract(supabase)

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
            credentials = utilities.ask_for_credentials
            try:
                supabase.auth.sign_in_with_password(credentials)
                print("Logged in successfully")
            except:
                print(f"Wrong credentials: {credentials}")
                continue

            update.update_cash(supabase)

        case "E" | "e" | "exit":
            print("Terminate")
            break
            
        case _:
            print(op + ": operation not available")
    

