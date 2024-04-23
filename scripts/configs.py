import os

CERT="INEP.pem"
TMP_DIR="../tmp/"
DATA_DIR="../dados/csv/"
ZIP_PATH="../zips"

TIPO_INDICADOR = "indicadores"
TIPO_MICRODADOS = "microdados"
OUTROS_INDICADORES = "outros_indicadores" 


default_sourcers = [
    {"tipo": TIPO_MICRODADOS, "descricao": "censoescolar", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar", "diretorio_zip": os.path.join(ZIP_PATH, "censoescolar"), 'filtro': {'SG_UF': 'PR'}},
    {"tipo": TIPO_MICRODADOS, "descricao": "encceja", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/encceja", "diretorio_zip": os.path.join(ZIP_PATH, "encceja"), 'filtro': {'SG_UF_PROVA': 'PR'}},
    {"tipo": TIPO_MICRODADOS, "descricao": "saeb", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb", "diretorio_zip": os.path.join(ZIP_PATH, "saeb"), 'filtro': {'SG_UF_ESC': '41-PR'}},
    {"tipo": TIPO_MICRODADOS, "descricao": "enem", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem", "diretorio_zip": os.path.join(ZIP_PATH, "enem"), 'filtro': {'CO_UF': 'PR'}},
    
    {"tipo": TIPO_INDICADOR, "descricao": "adequacao-da-formacao-docente", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/adequacao-da-formacao-docente/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "adequacao-da-formacao-docente"), 'filtro': {}, 'header_line': 10},
    {"tipo": TIPO_INDICADOR, "descricao": "complexidade-de-gestao-da-escola", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/complexidade-de-gestao-da-escola/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "complexidade-de-gestao-da-escola"), 'filtro': {}, 'header_line': 8},
    {"tipo": TIPO_INDICADOR, "descricao": "esforco-docente", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/esforco-docente/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "esforco-docente"), 'filtro': {}, 'header_line': 10},
    {"tipo": TIPO_INDICADOR, "descricao": "media-de-alunos-por-turma", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/media-de-alunos-por-turma/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "media-de-alunos-por-turma"), 'filtro': {}, 'header_line': 10},
    {"tipo": TIPO_INDICADOR, "descricao": "media-de-horas-aula-diaria", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/media-de-horas-aula-diaria/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "media-de-horas-aula-diaria"), 'filtro': {}, 'header_line': 9},
    {"tipo": TIPO_INDICADOR, "descricao": "nivel-socioeconomico", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/nivel-socioeconomico/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "nivel-socioeconomico"), 'filtro': {}, 'header_line': 10},
    {"tipo": TIPO_INDICADOR, "descricao": "percentual-de-docentes-com-curso-superior", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/percentual-de-docentes-com-curso-superior/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "percentual-de-docentes-com-curso-superior"), 'filtro': {}, 'header_line': 10},
    {"tipo": TIPO_INDICADOR, "descricao": "regularidade-do-corpo-docente", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/regularidade-do-corpo-docente/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "regularidade-do-corpo-docente"), 'filtro': {}, 'header_line': 9},
    {"tipo": TIPO_INDICADOR, "descricao": "remuneracao-media-dos-docentes", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/remuneracao-media-dos-docentes/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "remuneracao-media-dos-docentes"), 'filtro': {}, 'header_line': 8},
    {"tipo": TIPO_INDICADOR, "descricao": "taxas-de-distorcao-idade-serie", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-distorcao-idade-serie/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "taxas-de-distorcao-idade-serie"), 'filtro': {}, 'header_line': 9},
    {"tipo": TIPO_INDICADOR, "descricao": "taxas-de-nao-resposta", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-nao-resposta/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "taxas-de-nao-resposta"), 'filtro': {}, 'header_line': 8},
    {"tipo": TIPO_INDICADOR, "descricao": "taxas-de-transicao", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-transicao/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "taxas-de-transicao"), 'filtro': {}, 'header_line': 8},
    {"tipo": TIPO_INDICADOR, "descricao": "taxas-de-rendimento-escolar", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "taxas-de-rendimento-escolar"), 'filtro': {}, 'header_line': 8},

]

base_header1 = ['Ano', 'Regiao', 'Localizacao', 'Rede', 'Tx_de_Nao_Resp_Fund8e9_Total',	'Tx_de_Nao_Resp_Fund8e9_Anos_Iniciais1_5', 'Tx_de_Nao_Resp_Fund8e9_Anos_Finais6_9', 'Tx_de_Nao_Resp_Fund8e9_1_Ano', 'Tx_de_Nao_Resp_Fund8e9_2_Ano', 'Tx_de_Nao_Resp_Fund8e9_3_Ano', 'Tx_de_Nao_Resp_Fund8e9_4_Ano', 'Tx_de_Nao_Resp_Fund8e9_5_Ano', 'Tx_de_Nao_Resp_Fund8e9_6_Ano', 'Tx_de_Nao_Resp_Fund8e9_7_Ano', 'Tx_de_Nao_Resp_Fund8e9_8_Ano', 'Tx_de_Nao_Resp_Fund8e9_9_Ano',
                'Tx_de_Nao_Resp_Medio_Total',	'Tx_de_Nao_Resp_Medio_1_Ano', 'Tx_de_Nao_Resp_Medio_2_Ano', 'Tx_de_Nao_Resp_Medio_3_Ano', 'Tx_de_Nao_Resp_Medio_4_Ano', 'Total_Medio_Nao_Seriado']

use_header = {
        'tnr_regioes': {'line': 10, 'header': base_header1},
        
        'tnr_ufs': {'line': 10, 'header': base_header1},
        
        'taxa no-resposta regies': {'line': 10, 'header': base_header1},
        
        'taxa no-resposta brasil': {'line': 10, 'header': base_header1},
        
        'tnr_brasil': {'line': 10, 'header': base_header1},
        
        'taxa no-resposta uf': {'line': 10, 'header': base_header1}
        
    }

WGET_EXE = '"c:\\Program Files (x86)\\GnuWin32\\bin\\wget.exe"'#
#WGET_EXE = '/usr/bin/wget'
