import pandas as pd
import get_data_frame
import os
from pandasql import PandaSQL
from msg import msg

def bets_get(code, data_frame=False):

    #filelist = os.listdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")
    os.chdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")

    df = pd.read_table('bacen_v7.csv', sep=',', index_col=0, low_memory=False)

    code = str(code)
#    df['Periodicity']
    pdsql = PandaSQL()
    query = "SELECT Periodicity FROM df WHERE Codes LIKE" + "\'" + code + "\'" + ";"

    freq = pdsql(query).iloc[0]
    freq = freq[0].strip()

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
        return msg("Malformed metadata. The value" + freq + "is not valid for 'Periodicity'")

    database2 = database + ".csv"
    outros = pd.read_table(database2, sep=',', index_col=0, low_memory=False)


    query = "SELECT data, valor FROM outros WHERE serie LIKE" + "\'" + code + "\'" + ";"
    aux = pdsql(query)

    if len(aux.iloc[0,:]) == 0:
        return msg("Series is empty in database" + outros)

    aux = aux.dropna()

    aux1 = aux.iloc[:,1].astype('float64')

    try:
        aux2 = aux.iloc[:,0].astype('M')
        #TODO Create a lambda function HERE
        error = err
        return True

    tri = False




    return code


bets_get(code = 1, data_frame=False)