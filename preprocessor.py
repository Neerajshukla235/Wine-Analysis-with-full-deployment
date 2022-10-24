import pandas as pd
df=pd.read_csv('Californa_Wine_Production_1980_2020.csv')

def preprocess():
    global df
    #select the data from df
    df = df[['Year', 'County', 'HarvestedAcres', 'Yield(Unit/Acre)', 'Production', 'Price(Dollars/Unit)', 'Value(Dollars)']]
    df.isnull().sum()
    #drop the null values from Data
    df.dropna(inplace=True)

    return df

