from configs import DATA_DIR, default_sourcers, TIPO_MICRODADOS, filters
import os
import zipfile
import re
import pandas as pd
import traceback
from datasets2db import identifica_separador

def extrair_csvs(sourcers):
    for source in sourcers:
        if source['tipo'] == TIPO_MICRODADOS:
            print(source['descricao'])
            if not os.path.exists(os.path.join(DATA_DIR, source['descricao'])):
                os.mkdir(os.path.join(DATA_DIR, source['descricao']))
                
            list_dir = os.listdir(source['diretorio_zip'])
            for file in list_dir:
                if file[-4: ].lower() == '.zip':
                    with zipfile.ZipFile(os.path.join(source['diretorio_zip'], file), 'r') as zip_ref:
                        infiles = zip_ref.namelist()
                        for infile in infiles:
                            if infile[-4:].lower() == '.csv' or ( infile[-4:].lower() == '.txt' and '_saeb' in file ):
                                fin = zip_ref.open(infile)
                                content = fin.read()
                                name_file = infile.split('/')[-1].lower()
                                name_file = name_file[:-4] + '.csv'
                                if not re.search(r'[0-9]{4}\.[a-z]{3}', name_file):
                                    r = re.search(r'[0-9]{4}', file)
                                    if r:
                                        ano = r.group()
                                    else:
                                        ano = "SANO"
                                    name_file = name_file[:-4] + '_' + ano + name_file[-4:]
                                with open(os.path.join(DATA_DIR, source['descricao'], name_file), 'wb') as f:
                                    f.write(content)


def agrupa_arquivos(sourcers):
    for source in sourcers:
        if source['tipo'] == TIPO_MICRODADOS:
            print(source['descricao'])
            pcsv = re.compile(r'(?:[_|\ ][0-9]{4}|[0-9]{4}_[0-9]{4}[_|\ ])(.*)(?:\.csv)')
            dir = os.path.join(DATA_DIR, source['descricao'])
            files = []
            dfs = {}
            
            for file in os.listdir(dir):
                if file[:2] != '~$' and ('.xls' in file or '.xlsx' in file or '.csv' in file):
                    files.append(file)
            
            files.sort()

            for file in files:
                sep, n_cols, temHeader = identifica_separador(os.path.join(dir, file))
                
                filename = re.sub(pcsv, r'\1', file)
                df = pd.read_csv(os.path.join(dir, file), encoding='ISO-8859-1', sep=sep, engine='c', low_memory=False).dropna()
                if filename in filters:
                    for filtro in filters[filename]:
                        df = df.query(f"{filtro} == '{filters[filename][filtro]}'")
                
                if filename not in dfs:
                    dfs[filename] = df
                else:
                    dfs[filename] = pd.concat((dfs[filename], df))
                    
            for filename in dfs:
                    try:
                        dfs[filename].to_csv(os.path.join(dir, f"{filename}.csv"), index=False)
                    except:
                        error = f"Erro ao agrupar arquivo {filename}"
                        print(traceback.format_exc())
                        print(error)
                    

if __name__ == "__main__":
    #extrair_csvs(default_sourcers)
    agrupa_arquivos(default_sourcers)
            


