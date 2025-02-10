def update_cash_for_pres(supabase):
    pres = input("Presidente: -> ")
    cash_diff = input("+/- cash: -> ")

    try:
        response = supabase.table("presidenti").select("*").eq("nome", pres).execute()
        cash = response.data[0]["cash"]
        new_cash = {}
        new_cash["cash"] = cash + int(cash_diff)
        if new_cash["cash"] >= 0:
            supabase.table("presidenti").update(new_cash).eq("nome", pres).execute()
            print("Cash updated successfully")
        else:
            print(f"Error: {pres} has only {cash} cr.")
            return
    except:
        print("\nERROR")

    return



def update_cash_for_all(supabase):
    cash_diff = input("+/- cash: -> ")
    response = supabase.table("presidenti").select("*").execute()
    for i in range(len(response.data)):
        cash = response.data[i]["cash"]
        pres = response.data[i]["nome"]
        new_cash = {}
        new_cash["cash"] = cash + int(cash_diff)
        if new_cash["cash"] >= 0:
            supabase.table("presidenti").update(new_cash).eq("nome", pres).execute()
            print(f"Cash updated successfully for {pres}")
        else:
            print(f"Error: {pres} has only {cash} cr.")
            continue
    
    return



def exchange_cash(supabase):

    pres1 = input("Da (Presidente): -> ")
    pres2 = input("A (Presidente): -> ")
    cash_diff = input("Cash: -> ")

    try:
        response = supabase.table("presidenti").select("*").eq("nome", pres1).execute()
        cash = response.data[0]["cash"]
        new_cash = {}
        new_cash["cash"] = cash - int(cash_diff)
        if new_cash["cash"] >= 0:
            supabase.table("presidenti").update(new_cash).eq("nome", pres1).execute()
        else:
            print(f"Error: {pres1} has only {cash} cr.")
            return

        response = supabase.table("presidenti").select("*").eq("nome", pres2).execute()
        cash = response.data[0]["cash"]
        new_cash = {}
        new_cash["cash"] = cash + int(cash_diff)
        supabase.table("presidenti").update(new_cash).eq("nome", pres2).execute()

        print("Cash updated successfully")
    except:
        print("\nERROR")

    return