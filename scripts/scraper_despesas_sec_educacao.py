import pandas as pd
import requests
import time
import os
from configs import DATA_DIR

def baixa_despesas(dir_data, anos, meses):
    url = "https://www.transparencia.pr.gov.br/pte/ws/despesas/listardespesa?exercicio={exercicio}&mes={mes}&orgao=41"
    
    if not os.path.exists(dir_data):
        os.mkdir(dir_data)

    for ano in anos:
        print(f"Ano: {ano}")
        df = pd.DataFrame()
        for mes in meses:
            r = requests.get(url.format(exercicio=ano, mes=mes))
            if r.status_code < 400:
                df = pd.concat([df, pd.DataFrame(r.json()['listaDespesa'])])
            time.sleep(3)
        df.to_csv(os.path.join(dir_data, f'listaDespesa_PR_{ano}.csv'), index=False)
    

def agrupar_df(dir_data):
    df = pd.DataFrame()
    for file in os.listdir(dir_data):
        if 'listaDespesa_PR' in file and file[-4:].lower() == '.csv':
            df = pd.concat((df, pd.read_csv(os.path.join(dir_data, file))))    
    return df

if __name__ == "__main__":
    anos = range(2013, 2024)
    meses = range(1, 13)
    dir_despesas = os.path.join(DATA_DIR, 'despesas_portal_pr')
    
    baixa_despesas(dir_despesas, anos, meses)
    df = agrupar_df(dir_despesas)
    df.to_excel(os.path.join(dir_despesas, 'despesas_consolidadas_pr.xlsx'))
    
