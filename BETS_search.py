import re as re

bacen_final_ptv1 = 10
bacen_v7 = 5

def bets_search(start, description=None, src=None, periodicity=None, unit=None, code=None, view=True, lang="en"):

    if lang == "pt":
        database = base_final_ptv1

    else:
        database = bacen_v7

    if description == None and src == None and periodicity == None and unit == None and code == None:
        print("No search parameters. Please set the values of one or more parameters.")

    params = []

    if description != None:
        # Break description parameters

        and_params = []
        or_params = []

        # Workaround
        description = ' '.join([description])

        # TODO regex
        exprs = ["regex", "regex2"]

        if len(exprs) != 0:

            for i in range(len(exprs)):
                description = "string1"
                exprs[i] = "string2"
                exprs[i] = "string3"
                exprs[i] = "  string4  ".strip()
                and_params.append(''.join(["Description not like", "\'%", exprs[i], "%\'"]))


    # Match whole expressions
    exprs = "regex3"

    if len(exprs) != 0:
        for i in range(len(exprs)):
            description = re.sub(exprs[i], "", description)
            exprs[i] = re.sub("'", "", exprs[i])
            exprs[i] = exprs[i].strip()
            or_params.append(''.join(["Description like", "\'%", exprs[i], "%\'"]))

    # Do not match words
    words = description.str.extract("~ ?(.*?) ", expand=True)[0]


bets_search(start=10, description="teste")