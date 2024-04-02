CERT="INEP.pem"
TMP_DIR="../tmp/"
DATA_DIR="../dados/csv/"

default_sourcers = [
    {"descricao": "censoescolar", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar", "diretorio_zip": "../zips/censoescolar", 'filtro': {'SG_UF': 'PR'}},
    {"descricao": "encceja", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/encceja", "diretorio_zip": "../zips/encceja", 'filtro': {'SG_UF_PROVA': 'PR'}},
    {"descricao": "saeb", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb", "diretorio_zip": "../zips/saeb", 'filtro': {'SG_UF_ESC': '41-PR'}},
    {"descricao": "enem", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem", "diretorio_zip": "../zips/enem", 'filtro': {'CO_UF': 'PR'}}
]

