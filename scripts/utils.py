import pandas as pd
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

CIPHERS = (
    'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
    'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:AES256+EECDH:AES256+EDH'
    '!eNULL:!MD5'
)

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
    verify = True
    headers = {"User-Agent": ua.random}
    parser = 'html.parser'
    headers2 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',

            }
    header_script_resourcers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': '*/*',
        'Accept-Language': 'pt-BR,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Content-Length': '0',
        'Origin': 'https://servicos.tce.pr.gov.br',
        'Connection': 'keep-alive',
        'Referer': 'https://servicos.tce.pr.gov.br/Servicos/srv_ExibirRelatorios.aspx?T=progov_xls',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers',

    }
        
    
    header_report = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': '*/*',
        'Accept-Language': 'pt-BR,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Content-Length': '0',
        'Origin': 'https://servicos.tce.pr.gov.br',
        'Connection': 'keep-alive',
        'Referer': 'https://servicos.tce.pr.gov.br/Servicos/srv_ExibirRelatorios.aspx?T=progov_xls',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers',

    }
        
    header_report2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "pt-BR,en-US;q=0.7,en;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        'Referer': 'https://servicos.tce.pr.gov.br/Servicos/srv_ExibirRelatorios.aspx?T=progov_xls',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Priority": "u=1",
        "Host": 'servicos.tce.pr.gov.br',
        'Origin': 'https://servicos.tce.pr.gov.br',

    }
    
    header_reserved = {
        'Host': 'servicos.tce.pr.gov.br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': '*/*',
        'Accept-Language': 'pt-BR,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
        'Referer': 'https://servicos.tce.pr.gov.br/Servicos/srv_ExibirRelatorios.aspx?T=progov_xls',
        'Cookie': 'ASP.NET_SessionId=ygdbwnls23oskqfbpx1stedd',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',

    }
    
    def __repr__(self):
        return str(self.__dict__)
    
    
class SSLAdapter(HTTPAdapter):
    """
    A TransportAdapter that re-enables 3DES support in Requests.
    """
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS, cert_reqs=True)
        kwargs['ssl_context'] = context
        return super(SSLAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(SSLAdapter, self).proxy_manager_for(*args, **kwargs)