import pandas as pd
import os


os.chdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")
#arquivos=os.listdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")

#lista = []
#for i in range(len(arquivos)):
#    lista.append(str.split(arquivos[i], sep=".csv")[0])


#list the files
filelist = os.listdir("C:/Users/fernando.teixeira/PycharmProjects/BETS-beta-python/data")
#read them into pandas
df_list = [pd.read_table(file, sep=',', index_col=0) for file in filelist]
#concatenate them together
#big_df = pd.concat(df_list)

#print(df_list[2].head())