import requests
from fake_useragent import UserAgent
import sys
from configs import DATA_DIR
import os
import time
import traceback
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
from utils import ObjectScraper

DIR_DADOS = os.path.join(DATA_DIR, 'bolsafamilia')
lst_anos = list(range(2013, 2022)) + [2023]  #Um ano antes de PNE
url_d2023 = "https://aplicacoes.mds.gov.br/sagi/servicos/misocial/?fq=anomes_s:{ano}*&fl=codigo_ibge%2Canomes_s%2Cqtd_familias_beneficiarias_bolsa_familia_s%2Cvalor_repassado_bolsa_familia_s%2Cpbf_vlr_medio_benef_f&fq=valor_repassado_bolsa_familia_s%3A*&q=*%3A*&rows=100000&sort=anomes_s%20desc%2C%20codigo_ibge%20asc&wt=csv"
url_a2023 = "https://aplicacoes.mds.gov.br/sagi/servicos/misocial?fq=anomes_s:{ano}*&fq=tipo_s:mes_mu&wt=csv&q=*&fl=ibge:codigo_ibge,anomes:anomes_s,qtd_familias_beneficiarias_bolsa_familia,valor_repassado_bolsa_familia&rows=10000000&sort=anomes_s%20asc,%20codigo_ibge%20asc"


def inicia_engine():
    USER = os.getenv('DB_USER_IND', 'postgres')
    PASSWORD = os.environ.get('DB_PASSWORD_IND', '')
    HOST = os.environ.get('DB_HOST_IND', 'localhost')
    DB = os.environ.get('DB_INST_IND', 'indicadores')
    url_object = URL.create(
    "postgresql+psycopg2",
    username=USER,
    password=PASSWORD,  # plain (unescaped) text
    host=HOST,
    database=DB)
    engine = create_engine(url_object)
    return engine


def main(ano_busca=None, salvar_postgres=False):
    if ano_busca != None:
        anos = [ano_busca]
    else:
        anos = lst_anos

    for ano in anos:
        if ano >= 2023:
            url = url_d2023.format(ano=ano)
        else:
            url = url_a2023.format(ano=ano)
        
        try:
            print(f"Baixando ano {ano}")
            r = requests.get(url, allow_redirects=True, verify=ObjectScraper.verify, headers=ObjectScraper.headers)

            if(r.status_code) < 400:
                if not os.path.exists(DIR_DADOS):
                    os.mkdir(DIR_DADOS)
                nm_file = os.path.join(DIR_DADOS, f"{ano}_quantidade_familias_beneficiarias_valor_repassado.csv")
                with open(nm_file, 'wb') as f:
                    f.write(r.content)
                    
                if salvar_postgres:
                    engine = inicia_engine()
                    df = pd.read_csv(nm_file, sep=',', engine='c', low_memory=False)
                    df.to_sql(f'{ano}_qtd_familias_ben_vl_repassado', schema='bolsafamilia', con=engine, chunksize = 5000, index=False, method=None, if_exists='replace')
                    
            else:
                print(f"Erro baixando bolsa família para ano {ano}")
        except:
            print(traceback.format_exc())
            
        time.sleep(1)

if __name__ == '__main__':
    ano = None
    if len(sys.argv) == 2:
        ano = int(sys.argv[1])
    
    main(ano, salvar_postgres=True)