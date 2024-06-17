import pandas as pd
from fake_useragent import UserAgent

def agrupa_dataframe(df1, df2):
    for col in df1.columns:
        if col not in df2.columns:
            df2[col] = None
            
    for col in df2.columns:
        if col not in df1.columns:
            df1[col] = None

    return pd.concat([df1, df2])

class ObjectScraper():
    ua = UserAgent(browsers=['edge', 'chrome'])
    verify = False
    headers = {"User-Agent": ua.random}
    parser = 'html.parser'
        
    def __repr__(self):
        return str(self.__dict__)