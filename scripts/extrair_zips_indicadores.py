from configs import DATA_DIR, default_sourcers, TIPO_INDICADOR, use_header
import os
import zipfile
import re
import pandas as pd
import unicodedata
import traceback

def extrair_zip_indicadores(sourcers):
    for source in sourcers:
        if source['tipo'] == TIPO_INDICADOR:
            print(source['descricao'])
            if not os.path.exists(os.path.join(DATA_DIR, source['descricao'])):
                os.mkdir(os.path.join(DATA_DIR, source['descricao']))
                
            list_dir = os.listdir(source['diretorio_zip'])

            for file in list_dir:
                if file[-4: ].lower() == '.zip':
                    with zipfile.ZipFile(os.path.join(source['diretorio_zip'], file), 'r') as zip_ref:
                        infiles = zip_ref.namelist()
                        for infile in infiles:
                            if infile[-5:].lower() == '.xlsx' or infile[-4:].lower() == '.xls' or infile[-4:].lower() == '.csv':
                                fin = zip_ref.open(infile)
                                content = fin.read()
                                name_file = infile.split('/')[-1].lower()
                                name_file = unicodedata.normalize('NFKD', name_file.encode('ascii', 'ignore').decode('utf8'))
                                with open(os.path.join(DATA_DIR, source['descricao'], name_file), 'wb') as f:
                                    f.write(content)


def agrupa_arquivos(sourcers):
    for source in sourcers:
        if source['tipo'] == TIPO_INDICADOR:
            print(source['descricao'])
            pxls = re.compile(r'(?:_|\ )[0-9]{4}\.xls[x]{0,}')
            pcsv = re.compile(r'(?:_|\ )[0-9]{4}\.csv')
            dir = os.path.join(DATA_DIR, source['descricao'])
            files = os.listdir(dir)
            files.sort()
            dfs = {}
            for file in files:
                if '.csv' in file:
                    filename = re.sub(pcsv, '', file)
                else:
                    filename = re.sub(pxls, '', file)
                
                try:                    
                    if filename in use_header:
                        header_line = use_header[filename]['line']
                        columns = use_header[filename]['header']
                    else:
                        header_line = source['header_line']
                        columns = None
                        
                    if '.csv' in file:
                        df = pd.read_csv(os.path.join(dir, file)).dropna()
                    else:
                        df = pd.read_excel(os.path.join(dir, file), header=header_line, names=columns).dropna()
                        
                                     
                    if filename not in dfs:
                        dfs[filename] = df
                    else:
                        dfs[filename] = pd.concat((dfs[filename], df))
                except:
                    error = f"Erro ao agrupar arquivo {file}"
                    print(traceback.format_exc())
                    print(error)

            for filename in dfs:
                try:
                    dfs[filename].to_csv(os.path.join(dir, f"{filename}.csv"), index=False)
                except:
                    error = f"Erro ao agrupar arquivo {filename}"
                    print(traceback.format_exc())
                    print(error)
        

if __name__ == "__main__":
    extrair_zip_indicadores(default_sourcers)
    
    agrupa_arquivos(default_sourcers)
                
            
      

