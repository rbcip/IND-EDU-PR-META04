if not exist "zips" mkdir zips
if not exist "tmp" mkdir tmp
if not exist "dados" mkdir dados
if not exist "dados\csv" mkdir dados\csv

cd .\scripts

python -m scraper_indicadores

python -m extrair_zips_indicadores

cd ..