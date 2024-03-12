# IND-EDU-PR-META04
 Indicadores Educacionais do Paraná - Meta 4

 # Instalação

O scraper salva os arquivos zip em uma pasta configurada no arquivo **scrips/scraper.py**. Deve-se mudar a configuração ou criar as pastas no diretório do código. O diretório tmp é utilizando para baixar as páginas html que possuem os links para os zips.
 > mkdir -p zip/censoescolar
 > mkdir -p zip/encceja
 > mkdir -p zip/enem
 > mkdir -p zip/saeb
 > mkdir -p tmp
 > mkdir dados (configurável no arquivo configs.py)

# Uso

Depois pode-se executar de dentro do diretório scripts/

 > python -m scraper

 O script também permite passar um ano específico para os arquivos

 > python -m scraper 2021

Dentro do scraper.py existe uma lista com as fontes de microdados. Elas podem ser comentadas para não buscar a fonte específica, ou pode-se acrescentar mais fontes, desde que sigam o padrão das outras páginas de microdados (arquivo zip com o ano e classe css do link external-link)

Para Bolsa Família do Dados.Gov (https://dados.gov.br/dados/conjuntos-dados/bolsa-familia---mi-social). Pode-se utilizar o script **baixar_bolsa_familia.py** para todos os anos de 2004 pra frente,

 > python -m baixar_bolsa_familia

 Ou também para um ano específico:

 > python -m baixar_bolsa_familia YYYY

 Os arquivos serão salvos no diretório de dados. OBS: O ano de **2022** não consta disponível no site. O arquivo é baixado, mas sem informações de repasses.

Para extrair os dados pode-se utilizar o script **extrair_zips.py**

> python -m extrair_zips

Ele vai colocar os arquivos CSVs e TXT (que estão em diretórios DADOS nos .ZIPs) na pasta de dados. (Exceto para microdados saeb1999 pois os dados no zip também estão zipados)

O script datasets2db permite carregar dados dos csvs no postgresql local. Mas alguns arquivos possuem mais de 1600 colunas e não são possíveis de carregar. O processo pode ser um pouco demorado também.
