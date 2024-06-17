# Datalake do Observatório de Dados da Educação do Estado do Paraná
 
O Observatório de Dados da Educação do Paraná é uma iniciativa da Secretaria de Educação do Governo do Estado do Paraná, que visa criar um ambiente integrado entre a Gestão Pública e a Sociedade. Este projeto tem como objetivo proporcionar transparência às ações do governo estadual e oferecer dados e indicadores educacionais que são fundamentais para a tomada de decisão informada. A base de dados do Observatório é um recurso essencial para pesquisadores, gestores públicos, e cidadãos interessados em acompanhar e entender os indicadores de desempenho educacional no estado.

O repositório GitHub funciona como um Data Lake, onde dados brutos, estruturados e não estruturados são armazenados em seu formato nativo. Este repositório é projetado para permitir a coleta e manutenção de grandes volumes de dados, promovendo transparência e acessibilidade.


 # Instalação

 > Instalar o WGET para windows disponível em **http://downloads.sourceforge.net/gnuwin32/wget-1.11.4-1-setup.exe**.

Instalar o python com a opção "Add Python to environment variables" marcada.

Opcionalmente, se desejar um virtualenv executar:
 > pip install virtualenv
 > virtualenv indicadores
 > .\indicadores\Scripts\activate

Instalar as dependências:

 > pip install -r requirements.txt



O scraper salva os arquivos zip em uma pasta configurada no arquivo **scrips/scraper.py**. Deve-se mudar a configuração ou criar as pastas no diretório do código. O diretório tmp é utilizando para baixar as páginas html que possuem os links para os zips.
 
 > mkdir -p zips/censoescolar
 > mkdir -p zips/encceja
 > mkdir -p zips/enem
 > mkdir -p zips/saeb
 > mkdir -p tmp
 > mkdir -p dados/csv (configurável no arquivo configs.py)

# Microdados do INEP

Depois pode-se executar de dentro do diretório scripts/

 > .\indicadores\Scripts\activate
 > python -m scraper_microdados

 O script também permite passar um ano específico para os arquivos

 > python -m scraper_microdados 2021

Dentro do scraper.py existe uma lista com as fontes de microdados. Elas podem ser comentadas para não buscar a fonte específica, ou pode-se acrescentar mais fontes, desde que sigam o padrão das outras páginas de microdados (arquivo zip com o ano e classe css do link external-link)

Para Bolsa Família do Dados.Gov (https://dados.gov.br/dados/conjuntos-dados/bolsa-familia---mi-social). Pode-se utilizar o script **baixar_bolsa_familia.py** para todos os anos de 2004 pra frente,

 > python -m baixar_bolsa_familia

 Ou também para um ano específico:

 > python -m baixar_bolsa_familia YYYY

 Os arquivos serão salvos no diretório de dados. OBS: O ano de **2022** não consta disponível no site. O arquivo é baixado, mas sem informações de repasses.

Para extrair os dados pode-se utilizar o script **extrair_zips.py**

> python -m extrair_zips_microdados

Ele vai colocar os arquivos CSVs e TXT (que estão em diretórios DADOS nos .ZIPs) na pasta de dados. (Exceto para microdados saeb1999 pois os dados no zip também estão zipados)

O script **datasets2db** permite carregar dados dos csvs no postgresql local. Mas alguns arquivos possuem mais de 1600 colunas e não são possíveis de carregar. O processo pode ser um pouco demorado também.

***OBS:** O arquivo de configuração da pasta script (configs.py) inclui uma informação de filtro para os microdados no momento de tentar salvar no banco através do script **datasets2db**.

# Indicadores do INEP

De forma similar, pode-se baixar os dados de indicadores pelo script:

> python -m scraper_indicadores

E extrair para o diretório de dados com o comando:

> python -m extrair_zips_indicadores

Apesar de serem similares, optou-se por manter scripts separados para microdados e indicadores devido às diferenças entre eles no aspecto de scraper e formato dos arquivos de dados.

# Dados do Portal da Transparência do Paraná

Através do script:

> python -m scraper_despesas_sec_educacao

É possível baixar os dados de despesas na secretatia de educação via API. O script baixa os dados por ano, mantendo os CSVs, e também consolida em um xlsx.
