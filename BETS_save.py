import os
import pandas as pd
from get_data_frame import get_data_frame
from msg import msg

def bets_save(code, data=None, file_name="series"):
    local = os.getcwd()

    if data is None:
        y = get_data_frame(code)

    elif type(data) == pd.core.frame.DataFrame:
        y = data

    else:
        return msg("The parameter 'data' must be a DataFrame.")

    # TODO This code doesn't work, columns have not the same length
    y.iloc[:, 0] = str(y.iloc[:, 0]).split()


    y.to_csv(local+file_name)