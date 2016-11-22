import pandas as pd
import get_data_frame
import os
from pandasql import sqldf
from msg import msg

def bets_get(code, data_frame=False):

    #filelist = os.listdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")
    os.chdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")

    df = pd.read_table('bacen_v7.csv', sep=',', index_col=0, low_memory=False)


    if data_frame != False:
        return get_data_frame(code)

    data = df
    code = str(code)
    query = "SELECT Periodicity FROM data WHERE Codes LIKE" + "\'" + code + "\'"

    freq = str(sqldf(query)[0,0])
    freq = freq.strip()

    if freq == None:
        return msg("There is no corresponding entry in the metadata table.")

    aux1 = None
    aux2 = None

    if freq == "A":
        database = "ts_anuais"
        freq = 1

    elif freq == "Q":
        database = "ts_trimestrais"
        freq = 4

    elif freq == "M":
        database = "ts_mensais"
        freq = 12

    elif freq == "W":
        database = "ts_semanais"
        freq = 52

    elif freq == "D":
        database = "ts_diarias"
        freq = 365

    else:
        return msg("Malformed metadata. The value" + freq + "is not valid for 'periodicity'")

    query = "select data, valor from " + database + " where serie like " + "\'" + code + "\'"
    aux = sqldf(query)

    if len(aux[0,:]) == 0:
        return msg("Series is empty in database" + database)

    aux = aux.dropna()

    if aux[:,1].dtype == "category":
        aux[:,1] = aux[:,1].astype('float64')

    if aux[:,0].dtype == "category":
        aux[:,0] = aux[:,0].astype('float64')

    aux1 = aux[:,1].astype('float64')

    tri = False




    return code