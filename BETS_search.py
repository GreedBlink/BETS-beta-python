bacen_final_ptv1 = 10
bacen_v7 = 5

def bets_search(start, description = None, src = None, periodicity = None, unit = None, code = None, view=True, lang="en"):
    if lang == "pt":
        database = base_final_ptv1

    else:
        database = bacen_v7

    if description == None and src == None and periodicity == None and unit == None and code == None:
        print("No search parameters. Please set the values of one or more parameters.")

    params = []

    if description != None:
        ## Break description parameters
        and_params = []
        or_params = []

        # Workaround
        description = ''.join([description])


bets_search(start=10)