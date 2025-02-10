def delete_contract(supabase):
    giocatore = input("Giocatore -> ")
    
    response = supabase.table("contratti").select("*", count="exact").eq("giocatore", giocatore).execute()
    if response.count != 0:
        try:
            supabase.table('contratti').delete().eq('giocatore', giocatore).execute()
            print("Contract deleted successfully")
        except:
            print("\nERROR")
    else:
        print(f"Player {giocatore} not in DB")
        return
    
    return