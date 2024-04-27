import pandas as pd

def agrupa_dataframe(df1, df2):
    for col in df1.columns:
        if col not in df2.columns:
            df2[col] = None
            
    for col in df2.columns:
        if col not in df1.columns:
            df1[col] = None

    return pd.concat([df1, df2])