import requests
import re
from bs4 import BeautifulSoup
from utils import ObjectScraper
import json
import urllib

#"ExportUrlBase":"/Reserved.ReportViewerWebControl.axd?ReportSession=rdqchg45e5rei4uw3hb3bm45\u0026Culture=1046\u0026CultureOverrides=True\u0026UICulture=1046\u0026UICultureOverrides=True\u0026ReportStack=1\u0026ControlID=bf01d81eed0a4d5186a797197e594dd4\u0026OpType=Export\u0026FileName=+Progov+Exporta%c3%a7%c3%a3o+Excel\u0026ContentDisposition=OnlyHtmlInline\u0026Format="
#https://servicos.tce.pr.gov.br/Reserved.ReportViewerWebControl.axd?ReportSession=g1askiasvy0rf1qlzr0sef45&Culture=1046&CultureOverrides=True&UICulture=1046&UICultureOverrides=True&ReportStack=1&ControlID=6937e5c2cb4041689cd7bc93a77f8d81&OpType=Export&FileName=+Progov+Exporta%c3%a7%c3%a3o+Excel&ContentDisposition=OnlyHtmlInline&Format=CSV

server = 'https://servicos.tce.pr.gov.br'

s = requests.Session()

r = s.get("https://servicos.tce.pr.gov.br/Servicos/srv_ExibirRelatorios.aspx?T=progov_xls", allow_redirects=True, verify=True, headers=ObjectScraper.headers)
cookies = r.cookies

soup = BeautifulSoup(r.content, ObjectScraper.parser)

url_base = re.search('{"ActionParamId":".*"ExportUrlBase":".*}', soup.prettify()).group().split(',')

ExportUrlBase = ''

for params in url_base:
    if 'ExportUrlBase' in params:
        ExportUrlBase = urllib.parse.unquote_plus(params.split(':')[1].replace('"', '') + 'CSV').replace('\\u0026', '&')
        break

#r = s.post('https://servicos.tce.pr.gov.br/Reserved.ReportViewerWebControl.axd?OpType=SessionKeepAlive&ControlID=8b88d1dae7104c08a55b51f43c01df53', allow_redirects=True, verify=True, headers=ObjectScraper.header_script_resourcers, cookies=cookies)

print(f'{server}{ExportUrlBase}')
urllib.parse

r = s.post(f'{server}{ExportUrlBase}', allow_redirects=True, verify=True, headers=ObjectScraper.headers, cookies=cookies)

print(r.status_code)
with open('teste.csv', 'bw') as teste:
    teste.write(r.content)

print(r.content)
