import pandas as pd


def preprocess(df,df_country):
    
    df = df[df['Season'] == 'Summer']
    df = df.merge(df_country, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
