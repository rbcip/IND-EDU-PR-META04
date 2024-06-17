import requests
from fake_useragent import UserAgent
from configs import DATA_DIR
import os
from utils import ObjectScraper
import traceback
import pandas as pd

from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.poolmanager import PoolManager
import ssl

from requests.packages.urllib3.util.ssl_ import create_urllib3_context

CIPHERS = (
    'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
    'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:AES256+EECDH:AES256+EDH'
    '!eNULL:!MD5'
)

# AES256+EECDH:AES256+EDH
class SSLAdapter(HTTPAdapter):
    """
    A TransportAdapter that re-enables 3DES support in Requests.
    """
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS, cert_reqs=False)
        kwargs['ssl_context'] = context
        return super(SSLAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(SSLAdapter, self).proxy_manager_for(*args, **kwargs)

url_br_uf = "https://download.inep.gov.br/avaliacao_da_alfabetizacao/resultados_e_metas_ufs.xlsx"
url_municipios = "https://download.inep.gov.br/avaliacao_da_alfabetizacao/resultados_e_metas_municipios.xlsx"

DIR_DADOS = os.path.join(DATA_DIR, 'avaliacao_alfabetizacao')

def baixar_avaliacao_alfabetizacao(url, nome_arquivo, header_pos, filtro=None, dropna=False):
    try:
            s = requests.Session()
            s.mount('https://download.inep.gov.br', SSLAdapter())
            #r = s.get(url, allow_redirects=True, verify=ObjectScraper.verify, headers=ObjectScraper.headers, stream=True)
            r = s.get(url, allow_redirects=True, verify="INEP_all.pem", headers=ObjectScraper.headers, stream=True)

            if(r.status_code) < 400:
                if not os.path.exists(DIR_DADOS):
                    os.mkdir(DIR_DADOS)
                nm_file = os.path.join(DIR_DADOS, nome_arquivo)
                with open(nm_file, 'wb') as f:
                    f.write(r.content)
                
                df = pd.read_excel(nm_file, header=header_pos)
                
                if dropna:
                    df.dropna(inplace=True)
                    
                if filtro != None:
                    for campo in filtro:
                        df = df.query(f"{campo}=='{filtro[campo]}'")
                    
                df.to_csv(nm_file.replace('.xlsx', '.csv'), index=False, sep='|')
                    
            else:
                print(f"Erro baixando arquivo {nome_arquivo}")
                
                
    except:
        print(traceback.format_exc())
            



if __name__ == "__main__":
    baixar_avaliacao_alfabetizacao(url_br_uf, 'resultados_e_metas_ufs.xlsx', 1)
    baixar_avaliacao_alfabetizacao(url_municipios, 'resultados_e_metas_municipios.xlsx', 1, filtro={'SG_UF': 'PR'}, dropna=True)