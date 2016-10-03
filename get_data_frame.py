from stemming.porter2 import stem
import sql as sql
from sql.aggregate import *
from sql.conditionals import *
import pandas as pd




def get_data_frame(code, ts=None):

    abbr = "values"

    if ts == None:

        result = bets_search(code=code, view=False)

        if len(result) != 0:
            abbr = [stem(word) for word in result[0,1]]
            freq = str(result[0, 2].strip())

        if freq == "A":
            database = "ts_anuais"
        elif freq == "Q":
            database = "ts_trimestrais"
        elif freq == "M":
            database = "ts_mensais"
        elif freq == "W":
            database = "ts_semanais"
        elif freq == "D":
            database = "ts_diarias"

        query = "select data, valor from " + database + " where serie like " + "\'" + code + "\'"
        series = sql.Query(query)

        if len(result) == 0:
            # TODO implement msg() function
            #return msg(.MSG_NOT_AVAILABLE)
    else:
        dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
        t = pd.read_csv(ts, parse_dates='', index_col='', date_parser=dateparse)
        y = pd.DataFrame(ts)
        series = pd.DataFrame(t,y)

    series.columns['dates', abbr]

    return series