import pandas as pd
df = pd.read_csv('http://winterolympicsmedals.com/medals.csv')

df_filt = df[['Year', 'City', 'Sport', 'Event gender', 'Medal']]

def base_data():
    df = pd.read_csv('http://winterolympicsmedals.com/medals.csv')
    return df[['Year', 'City', 'Sport', 'Event gender', 'Medal']]

def test_create_dataframe(dataf):
    if set([i for i in dataf.columns]) == set([i for i in df_filt.columns]):
        if dataf['City'].dtype == df_filt['City'].dtype and dataf['Year'].dtype == df_filt['Year'].dtype and dataf['Sport'].dtype == df_filt['Sport'].dtype and dataf['Event gender'].dtype == df_filt['Event gender'].dtype and dataf['Medal'].dtype == df_filt['Medal'].dtype:
            if len(dataf) >= 10:
                return True
    return False

df2 = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Auto.csv')
df2.rename(columns={'mpg':'City',
                          'cylinders':'Year',
                          'displacement':'Sport', 'horsepower':'Event gender', 'weight':'Medal'}, 
                 inplace=True)
df2 = df2.iloc[:,:5]
test_create_dataframe(df_filt)
