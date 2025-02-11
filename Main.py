import settings
import create
import read
import update
import delete
import switch_season
from supabase import create_client, Client

supabase: Client = create_client(settings.url, settings.key)

while True:
    op = input("\nDigit operations:\nC (create contracts)\nR (read tables)\nU (update cash)\nD (delete contracts)\nM (manage seasons)\nE (exit)\n-> ")
    match op:
        case "C" | "c" | "create":
            create.create_page(supabase)

        case "R" | "r" | "read":
            read.read_page(supabase)
        
        case "U" | "u" | "update":
            update.update_page(supabase)
        
        case "D" | "d" | "delete":
            delete.delete_page(supabase)

        case "M" | "m" | "manage":
            switch_season.switch_season_page(supabase)

        case "E" | "e" | "exit":
            print("Terminate")
            break
            
        case _:
            print(op + ": operation not available")
    

