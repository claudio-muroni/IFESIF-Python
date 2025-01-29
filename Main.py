import settings
import read
from supabase import create_client, Client

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
                        case "FLA" | "fla": pres = "Claudio"
                        case _: pres = ""
                            
                    if pres!= "":
                        response = supabase.table(table).select("ruolo","giocatore").eq("nome_presidente", pres).execute()
                        print(response)
                    else:
                        print(op3 + ": president not available")

                case _:
                    print(op2 + ": table not available")
        
        case "E" | "e" | "exit":
            print("Terminate")
            break
            
        case _:
            print(op + ": operation not available")
    

