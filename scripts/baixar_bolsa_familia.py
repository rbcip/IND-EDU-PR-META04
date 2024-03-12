import requests
from fake_useragent import UserAgent
from datetime import date
import sys
from configs import DATA_DIR
import os
import time
import traceback

DIR_DADOS = os.path.join(DATA_DIR, 'bolsafamilia')
lst_anos = range(2004,date.today().year)
url_d2023 = "https://aplicacoes.mds.gov.br/sagi/servicos/misocial/?fq=anomes_s:{ano}*&fl=codigo_ibge%2Canomes_s%2Cqtd_familias_beneficiarias_bolsa_familia_s%2Cvalor_repassado_bolsa_familia_s%2Cpbf_vlr_medio_benef_f&fq=valor_repassado_bolsa_familia_s%3A*&q=*%3A*&rows=100000&sort=anomes_s%20desc%2C%20codigo_ibge%20asc&wt=csv"
url_a2023 = "https://aplicacoes.mds.gov.br/sagi/servicos/misocial?fq=anomes_s:{ano}*&fq=tipo_s:mes_mu&wt=csv&q=*&fl=ibge:codigo_ibge,anomes:anomes_s,qtd_familias_beneficiarias_bolsa_familia,valor_repassado_bolsa_familia&rows=10000000&sort=anomes_s%20asc,%20codigo_ibge%20asc"

class ObjectScraper():
    ua = UserAgent(browsers=['edge', 'chrome'])
    verify = True
    headers = {"User-Agent": ua.random}
    parser = 'html.parser'
        
    def __repr__(self):
        return str(self.__dict__)

def main(ano_busca=None):
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
        
                with open(os.path.join(DIR_DADOS, f"{ano}_quantidade_familias_beneficiarias_valor_repassado.csv"), 'wb') as f:
                    f.write(r.content)
            else:
                print(f"Erro baixando bolsa família para ano {ano}")
        except:
            print(traceback.format_exc())
            
        time.sleep(1)

if __name__ == '__main__':
    ano = None
    if len(sys.argv) == 2:
        ano = int(sys.argv[1])
    
    main(ano)