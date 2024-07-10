import requests
import re
from bs4 import BeautifulSoup
from utils import ObjectScraper
import os
import urllib
import time
from configs import DATA_DIR

select_post_data = {
    'ReportViewer2$ctl03$ctl00': "",
    'ReportViewer2$ctl03$ctl01': "",
    'ReportViewer2$ctl10': 'ltr',
    'ReportViewer2$ctl11': 'quirks',
    'ReportViewer2$AsyncWait$HiddenCancelField': 'False',
    'ReportViewer2$ctl04$ctl03$ddValue': '-1', #alterar valor option município
    'ReportViewer2$ctl04$ctl05$ddValue': '3',
    'ReportViewer2$ctl04$ctl07$ddValue': '1',
    'ReportViewer2$ctl04$ctl09$ddValue': '1',
    'ReportViewer2$ToggleParam$store': '',
    'ReportViewer2$ToggleParam$collapse': 'false',
    'ReportViewer2$ctl05$ctl00$CurrentPage': '1',
    'ReportViewer2$ctl05$ctl03$ctl00': "",
    'ReportViewer2$ctl08$ClientClickedId': "",
    'ReportViewer2$ctl07$store': '',
    'ReportViewer2$ctl07$collapse': 'false',
    'ReportViewer2$ctl09$VisibilityState$ctl00': 'ReportPage',
    'ReportViewer2$ctl09$ScrollPosition': '',
    'ReportViewer2$ctl09$ReportControl$ctl02': '',
    'ReportViewer2$ctl09$ReportControl$ctl03': '',
    'ReportViewer2$ctl09$ReportControl$ctl04': '100',
    '__EVENTTARGET': 'ReportViewer2$ctl04$ctl03$ddValue',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': '', #completar
    '__VIEWSTATEGENERATOR': '', #completar
    '__EVENTVALIDATION': '' #completar
}

save_dir = os.path.join(DATA_DIR, 'avaliacao_progov')

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

def extrair_sessao_post(content):
    soup = BeautifulSoup(content, ObjectScraper.parser)
    view_state = ''
    view_state_gen= ''
    event_val= ''
    
    view_state_tag = soup.find(id='__VIEWSTATE')
    if view_state_tag:
        #print('V:', view_state_tag.attrs['value'])
        view_state = view_state_tag.attrs['value']
        
    view_state_gen_tag = soup.find(id='__VIEWSTATEGENERATOR')
    if view_state_gen_tag:
        #print('\nVG:', view_state_gen_tag.attrs['value'])
        view_state_gen = view_state_gen_tag.attrs['value']
        
    event_val_tag = soup.find(id='__EVENTVALIDATION')
    if event_val_tag:
        #print('\nE:', event_val_tag.attrs['value'])
        event_val = event_val_tag.attrs['value']
        
    return {'__VIEWSTATE': view_state, '__VIEWSTATEGENERATOR': view_state_gen, '__EVENTVALIDATION': event_val}

#Utiliza o ExportUrlBase para as requisições de dados em vários formatos
#"ExportUrlBase":"/Reserved.ReportViewerWebControl.axd?ReportSession=rdqchg45e5rei4uw3hb3bm45\u0026Culture=1046\u0026CultureOverrides=True\u0026UICulture=1046\u0026UICultureOverrides=True\u0026ReportStack=1\u0026ControlID=bf01d81eed0a4d5186a797197e594dd4\u0026OpType=Export\u0026FileName=+Progov+Exporta%c3%a7%c3%a3o+Excel\u0026ContentDisposition=OnlyHtmlInline\u0026Format="
#https://servicos.tce.pr.gov.br/Reserved.ReportViewerWebControl.axd?ReportSession=g1askiasvy0rf1qlzr0sef45&Culture=1046&CultureOverrides=True&UICulture=1046&UICultureOverrides=True&ReportStack=1&ControlID=6937e5c2cb4041689cd7bc93a77f8d81&OpType=Export&FileName=+Progov+Exporta%c3%a7%c3%a3o+Excel&ContentDisposition=OnlyHtmlInline&Format=CSV

server = 'https://servicos.tce.pr.gov.br'
ExportUrlBase = ''
options = []
s_post = {}
url_inter = ''

#inicia e pega o cookie de sessão
def inicia_sessao():
    global s_post, options, url_inter, ExportUrlBase
    s = requests.Session()
    r = s.get("https://servicos.tce.pr.gov.br/Servicos/srv_ExibirRelatorios.aspx?T=progov_xls", allow_redirects=True, verify=True, headers=ObjectScraper.headers2)

    soup = BeautifulSoup(r.content, ObjectScraper.parser)

    s_post = extrair_sessao_post(r.content)

    # Lista de municípios
    select = soup.find(id='ReportViewer2_ctl04_ctl03_ddValue')
    if select:
        options = select.findAll('option')

    # ExportUrlBase e ControlID para manter a sessão (pode não ser necessário)
    url_base = re.search('{"ActionParamId":".*"ExportUrlBase":".*}', soup.prettify()).group().split(',')
    ControlID = re.search(r'ControlID=(\w+)', soup.prettify()).group(1) #.split(',')
    #print('ControlID: ', ControlID)

    url_inter = 'https://servicos.tce.pr.gov.br/Reserved.ReportViewerWebControl.axd?OpType=SessionKeepAlive&ControlID=' + ControlID

    for params in url_base:
        if 'ExportUrlBase' in params:
            ExportUrlBase = urllib.parse.unquote_plus(params.split(':')[1].replace('"', '') + 'CSV').replace('\\u0026', '&')
            break

    #SessionKeepAlive
    i = s.post(url_inter, allow_redirects=True, verify=True, headers=ObjectScraper.header_report)
    #print(i.status_code, " inter")
    return s

s = inicia_sessao()

# Baixa dados do primeiro relatório (padrão)
r = s.post(f'{server}{ExportUrlBase}', allow_redirects=True, verify=True, headers=ObjectScraper.headers2)

with open(os.path.join(save_dir, f'{options[1].attrs['value']}-{options[1].text}.csv'), 'bw') as municipio:
    print(f'Salvando {options[1].attrs['value']}-{options[1].text}.csv')
    municipio.write(r.content)

options = options[2:]

#SessionKeepAlive
i = s.post(url_inter, allow_redirects=True, verify=True, headers=ObjectScraper.header_report)

print('\n###########################\n')

select_post_data['__VIEWSTATE'] = s_post['__VIEWSTATE']
select_post_data['__VIEWSTATEGENERATOR'] = s_post['__VIEWSTATEGENERATOR']
select_post_data['__EVENTVALIDATION'] = s_post['__EVENTVALIDATION']

for option in options:
    time.sleep(2)
    
    select_post_data['ReportViewer2$ctl04$ctl03$ddValue'] = option.attrs['value']

    # post com id do muncípio
    r = s.post("https://servicos.tce.pr.gov.br/Servicos/srv_ExibirRelatorios.aspx?T=progov_xls", allow_redirects=True, verify=True, headers=ObjectScraper.header_report2, data=select_post_data)

    i = s.post(url_inter, allow_redirects=True, verify=True, headers=ObjectScraper.header_report)

    r = s.post(f'{server}{ExportUrlBase}', allow_redirects=True, verify=True, headers=ObjectScraper.headers2)

    print(r.status_code)
    if r.status_code >= 400:
        print('Erro, recriando sessão')
        s = inicia_sessao()
        select_post_data['__VIEWSTATE'] = s_post['__VIEWSTATE']
        select_post_data['__VIEWSTATEGENERATOR'] = s_post['__VIEWSTATEGENERATOR']
        select_post_data['__EVENTVALIDATION'] = s_post['__EVENTVALIDATION']
        r = s.post("https://servicos.tce.pr.gov.br/Servicos/srv_ExibirRelatorios.aspx?T=progov_xls", allow_redirects=True, verify=True, headers=ObjectScraper.header_report2, data=select_post_data)
        i = s.post(url_inter, allow_redirects=True, verify=True, headers=ObjectScraper.header_report)
        r = s.post(f'{server}{ExportUrlBase}', allow_redirects=True, verify=True, headers=ObjectScraper.headers2)
        if r.status_code >= 400:
            error = f"Erro baixando {option.attrs['value']}-{option.text}.csv. Status Code: {r.status_code}"
            print(error)
            exit()
    
    with open(os.path.join(save_dir, f'{option.attrs['value']}-{option.text}.csv'), 'bw') as municipio:
        print(f'Salvando {option.attrs['value']}-{option.text}.csv')
        municipio.write(r.content)

    