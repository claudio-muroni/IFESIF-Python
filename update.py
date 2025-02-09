def update_cash(supabase):
    pres = input("Presidente -> ")
    cash_diff = input("+/- cash -> ")

    try:
        response = supabase.table("presidenti").select("*").eq("nome", pres).execute()
        cash = response.data[0]["cash"]
        new_cash = {}
        new_cash["cash"] = cash + int(cash_diff)
        supabase.table("presidenti").update(new_cash).eq("nome", pres).execute()
        print("Cash updated successfully")
    except:
        print("\nERROR")