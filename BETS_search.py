import re as re
import pandas as pd
import os
from msg import msg



def bets_search(start, description=None, src=None, periodicity=None, unit=None, code=None, view=True, lang="en"):

    filelist = os.listdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")
    os.chdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")
    # read them into pandas

    df_list = [pd.read_table(file, sep=',', index_col=0, low_memory=False) for file in filelist]

    if lang == "pt":
        database = df_list[3]

    else:
        database = df_list[1]

    if description is None and src is None and periodicity is None and unit is None and code is None:
        print(msg("No search parameters. Please set the values of one or more parameters."))

    params = []

    if description != None:
        # Break description parameters

        and_params = []
        or_params = []

        # Workaround
        description = ' '.join([description])

        # TODO regex
        # Do not match whole expressions
        exprs = re.match("~ ?'(.*?)'", description)


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