import pandas as pd
import get_data_frame
import os


def bets_get(code, data_frame=False):

    #filelist = os.listdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")
    os.chdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")

    df = pd.read_table('bacen_v7.csv', sep=',', index_col=0, low_memory=False)


    if data_frame != False:
        return get_data_frame(code)

    data = df








    return code