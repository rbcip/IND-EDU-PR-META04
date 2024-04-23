import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import traceback
import os
import time
import sys
import subprocess
from configs import CERT, TMP_DIR, default_sourcers, TIPO_MICRODADOS, WGET_EXE
from datetime import date

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
    header2= {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
            }
    
    
    def __repr__(self):
        return str(self.__dict__)


def baixa_zips(fontes, anos=None, reload_links=False):
    if anos == None:
        anos_lista = list(range(2013, date.today().year)) #Um ano antes do PNE
    else:
        anos_lista = anos
        
    for fonte in fontes:
        if fonte['tipo'] == TIPO_MICRODADOS:
            if not os.path.exists(fonte["diretorio_zip"]):
                os.mkdir(fonte["diretorio_zip"])
                
            try:
                s = requests.Session()
                file_html = os.path.join(TMP_DIR, f"{fonte['descricao']}.html")
                
                busca = re.compile('https.*\.zip', re.IGNORECASE) 
                
                if not os.path.exists(file_html) or reload_links:
                    reponse_http = s.get(fonte["url"], allow_redirects=True, verify=ObjectScraper.verify, headers=ObjectScraper.headers)
                    if(reponse_http.status_code < 400):
                        with open(file_html, "w", encoding='utf8') as html:
                            html.write(reponse_http.text)
                    else:
                        error = f"Erro baixando página: {fonte['descricao']}, código: {reponse_http.status_code}"
                        print(traceback.format_exc())
                        print(error)
                
                
                with open(file_html, "r", encoding='utf8') as html:
                    soup = BeautifulSoup(html.read(), ObjectScraper.parser)
                    
                ext_links_zip = soup.find_all("a", {'class': "external-link", 'href': busca})
                for link in ext_links_zip:
                    i = 0
                    while i < len(anos_lista):
                        ano_busca = re.compile(f'https.*{anos_lista[i]}.*\.zip')
                        if re.search(ano_busca, link["href"]):
                            file_name_aux = os.path.join(fonte["diretorio_zip"], link["href"].split("/")[-1])
                            print(f'Baixando {link["href"]} para {file_name_aux}')
                            cmd = f"{WGET_EXE} -c --ca-certificate={CERT} --no-check-certificate {link['href']} -O {file_name_aux}"
                            runcmd(cmd, verbose = False)
                            #verify=ObjectScraper.verify ".\INEP.pem"
                            #r = s.get(link["href"], allow_redirects=True, verify=".\INEP.pem", headers=ObjectScraper.header2, stream=True)
                            #with open(file_name_aux, mode='wb') as file:
                            #    file.write(r.content)
                                
                            time.sleep(1)
                            i = len(anos_lista) #Sai do laço
                        i += 1
                    
            except Exception:
                print(traceback.format_exc())



if __name__ == "__main__":
    ano=None
    if len(sys.argv) > 1:
        ano = [str(sys.argv[1])]
    
    baixa_zips(default_sourcers, anos=ano, reload_links=True)
    