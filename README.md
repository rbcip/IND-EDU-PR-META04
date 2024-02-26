# IND-EDU-PR-META04
 Indicadores Educacionais do Paraná - Meta 4

 # Instalação

O scraper salva os arquivos zip em uma pasta configurada no arquivo **scrips/scraper.py**. Deve-se mudar a configuração ou criar as pastas no diretório do código. O diretório tmp é utilizando para baixar as páginas html que possuem os links para os zips.
 > mkdir -p zip/censoescolar
 > mkdir -p zip/encceja
 > mkdir -p zip/enem
 > mkdir -p zip/saeb
 > mkdir -p tmp

 depois pode-se executar de dentro do diretório scripts/

 > python -m scraper

 O script também permite passar um ano específico para os arquivos

 > python -m scraper 2021

Dentro do scraper.py existe uma lista com as fontes de microdados. Elas podem ser comentadas para não buscar a fonte específica, ou pode-se acrescentar mais fontes, desde que sigam o padrão das outras páginas de microdados (arquivo zip com o ano e classe css do link external-link)