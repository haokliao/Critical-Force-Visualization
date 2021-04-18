import pandas as pd

def clean (csv):
    #read CSV file using pandas
    dataframe = pd.read_csv(csv)

    #drop all columns filled with only na values
    dataframe = dataframe.dropna(axis=1, how='all')
    
    #drop all rows with na values
    dataframe = dataframe.dropna(axis=0, how='all')
    
    return dataframe

def percentage_fix (dataframe):

    #convert all %'s into non string values? something about the way pandas reads csvs turns values into strings?

    dataframe['PEAK FORCE % BODY MASS'] = dataframe['PEAK FORCE % BODY MASS'].str.rstrip('%').astype('float')/100
    dataframe['CF % BODY MASS'] = dataframe['CF % BODY MASS'].str.rstrip('%').astype('float')/100
    dataframe['CF % PEAK FORCE'] = dataframe['CF % PEAK FORCE'].str.rstrip('%').astype('float')/100
    