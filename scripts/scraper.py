import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import traceback
import os
import time
import shutil
import subprocess

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

CERT="INEP.pem"
TMP_DIR="../tmp/"

default_sourcers = [
    {"descricao": "censoescolar", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar", "diretorio_zip": "../zips/censoescolar"},
    {"descricao": "encceja", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/encceja", "diretorio_zip": "../zips/encceja"},
    {"descricao": "saeb", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb", "diretorio_zip": "../zips/saeb"}
]


def baixa_zips(fontes, ano=None, reload_links=False):
    for fonte in fontes:
        try:
            s = requests.Session()
            file_html = os.path.join(TMP_DIR, f"{fonte['descricao']}.html")
            if ano != None:
                busca = re.compile(f'https.*{ano}.*\.zip')
            else:
                busca = re.compile('https.*\.zip') 
            
            if not os.path.exists(file_html) or reload_links:
                reponse_http = s.get(fonte["url"], allow_redirects=True, verify=ObjectScraper.verify, headers=ObjectScraper.headers)
                if(reponse_http.status_code < 400):
                    with open(file_html, "w", encoding='utf8') as html:
                        html.write(reponse_http.text)
                else:
                    raise Exception(f"Erro baixando página: {fonte['descricao']}, código: {reponse_http.status_code}")
            
            
            with open(file_html, "r", encoding='utf8') as html:
                soup = BeautifulSoup(html.read(), ObjectScraper.parser)
                
            ext_links_zip = soup.find_all("a", {'class': "external-link", 'href': busca})
            for link in ext_links_zip:
                file_name_aux = os.path.join(fonte["diretorio_zip"], link["href"].split("/")[-1])
                print(f'Baixando {link["href"]} para {file_name_aux}')
                cmd = f"wget -c --ca-certificate={CERT}  {link['href']} -O {file_name_aux}"
                runcmd(cmd, verbose = False)
                time.sleep(5)
                
        except Exception:
            print(traceback.format_exc())



if __name__ == "__main__":
    baixa_zips(default_sourcers, reload_links=False)
    