import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import traceback
import os
import time
import sys
import subprocess
from configs import CERT, TMP_DIR, default_sourcers, TIPO_INDICADOR, WGET_EXE
from datetime import date

# Apenas indicadores de BR e UF pelo regex

def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

class ObjectScraper():
    ua = UserAgent(browsers=['edge', 'chrome'])
    verify = False
    headers = {"User-Agent": ua.random}
    parser = 'html.parser'
        
    def __repr__(self):
        return str(self.__dict__)


def baixa_zips(fontes, anos=None, reload_links=False):
    if anos == None:
        anos_lista = list(range(2013, date.today().year)) #Um ano antes do PNE
    else:
        anos_lista = anos
        
    for fonte in fontes:
        if fonte['tipo'] == TIPO_INDICADOR:
            if not os.path.exists(fonte["diretorio_zip"]):
                os.mkdir(fonte["diretorio_zip"])

            for ano in anos_lista:
                try:
                    s = requests.Session()
                    file_html = os.path.join(TMP_DIR, f"{fonte['descricao']}_{ano}.html")
                    
                    busca = re.compile('https.*(?:(?:estados)|(?:regioes)|(?:brasil)){1,}.*(?:\.zip|\.xls)', re.IGNORECASE)
                    
                    if not os.path.exists(file_html) or reload_links:
                        url = fonte["url"].format(ano=ano)
                        if fonte['descricao'] == 'esforco-docente' and ano == 2014:
                            url = f'{url}-1'
                        elif fonte['descricao'] == 'taxas-de-transicao':
                            url = f'{url}-{ano+1}'

                        
                        reponse_http = s.get(url, allow_redirects=True, verify=ObjectScraper.verify, headers=ObjectScraper.headers)
                        if(reponse_http.status_code < 400):
                            with open(file_html, "w", encoding='utf8') as html:
                                html.write(reponse_http.text)
                        else:
                            error = f"Erro baixando página: {fonte['descricao']}_{ano}, código: {reponse_http.status_code}"
                            print(traceback.format_exc())
                            print(error)                            
                    
                    
                    with open(file_html, "r", encoding='utf8') as html:
                        soup = BeautifulSoup(html.read(), ObjectScraper.parser)
                        
                    ext_links_zip = soup.find_all("a", {'href': busca})
                    for link in ext_links_zip:
                        file_name_aux = os.path.join(fonte["diretorio_zip"], link["href"].split("/")[-1])
                        print(f'Baixando {link["href"]} para {file_name_aux}')
                        if os.name == 'nt':
                            file_name_aux = file_name_aux.replace('/', '\\')
                        cmd = f"{WGET_EXE} -c --ca-certificate={CERT} --no-check-certificate {link['href']} -O {file_name_aux}"
                        print(cmd)
                        runcmd(cmd, verbose = False)
                        time.sleep(1)
                        
                except Exception:
                    print(traceback.format_exc())



if __name__ == "__main__":
    ano=None
    if len(sys.argv) > 1:
        ano = [str(sys.argv[1])]
    
    baixa_zips(default_sourcers, anos=ano, reload_links=True)
    