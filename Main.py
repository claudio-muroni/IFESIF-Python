import settings
import read
import create
from supabase import create_client, Client
from getpass import getpass

supabase: Client = create_client(settings.url, settings.key)

while True:
    op = input("Digit operations:\nR (read)\nE (exit)\n-> ")
    match op:
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
        case "C" | "c" | "create":
            credentials = {}
            credentials["email"] = input("Insert mail -> ")
            credentials["password"] = getpass("Insert pw -> ")
            
            try:
                supabase.auth.sign_in_with_password(credentials)
                create.insert_contract(supabase)
            except:
                print("credenziali errate:")
                print(credentials)

            
                        
        case "E" | "e" | "exit":
            print("Terminate")
            break
            
        case _:
            print(op + ": operation not available")
    

