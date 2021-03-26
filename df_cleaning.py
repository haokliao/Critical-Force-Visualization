import pandas as pd

def clean (csv):
    dataframe = pd.read_csv(csv)
    dataframe = dataframe.dropna(axis=1, how='all')
    #drop all columns filled with only na values
    dataframe = dataframe.dropna(axis=0, how='all')
    #drop all rows with na values
    return dataframe