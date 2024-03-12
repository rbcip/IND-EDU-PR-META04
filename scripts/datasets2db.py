import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.engine import URL
from configs import DATA_DIR, default_sourcers
import re

def extrair_nm_base(txt):
    aux = txt.split('.')[0]
    if re.search('[0-9]{4}', aux.split('_')[-1]):
        return '_'.join(aux.split('_')[0:-1])
    else:
        return aux

def inicia_engine():
    USER = os.getenv('DB_USER_IND', 'postgres')
    PASSWORD = os.environ.get('DB_PASSWORD_IND', '')
    HOST = os.environ.get('DB_HOST_IND', 'localhost')
    DB = os.environ.get('DB_INST_IND', 'indicadores')
    url_object = URL.create(
    "postgresql+psycopg2",
    username=USER,
    password=PASSWORD,  # plain (unescaped) text
    host=HOST,
    database=DB)
    engine = create_engine(url_object)
    return engine

def agrupa_arquivos(df1, df2):
    for col in df1.columns:
        if col not in df2.columns:
            df2[col] = None
            
    for col in df2.columns:
        if col not in df1.columns:
            df1[col] = None

    return pd.concat([df1, df2])

def concat_arquivos(dir_base: str, sourcers):
    dfs = {}
    for sourcer in sourcers:
        print('####')
        print("Origem: ", sourcer['descricao'])
        list_dir = os.listdir(os.path.join(dir_base, sourcer['descricao']))
        list_dir.sort()
        nm_base = 'NONENONENONE'

        for filename in list_dir:
            arquivo = os.path.join(dir_base, sourcer['descricao'], filename)
            if os.path.isfile(arquivo) and '.csv' in filename:
                nm_base_aux = extrair_nm_base(filename)
                if nm_base != nm_base_aux:
                    nm_base = nm_base_aux
                    dfs[nm_base] = pd.read_csv(arquivo, encoding='ISO-8859-1', sep=';', engine='c', low_memory=False)
                    dfs[nm_base]['origem_registro'] = filename
                    print(f"Iniciando para: {nm_base} e adicionando {filename} com shape {dfs[nm_base].shape}")
                else:
                    print(f"Adicionando: {filename}")
                    df_aux = pd.read_csv(arquivo, encoding='ISO-8859-1', sep=';', engine='c', low_memory=False)
                    df_aux['origem_registro'] = filename
                    dfs[nm_base] = agrupa_arquivos(dfs[nm_base], df_aux)
                    print(f"Adicionado: {filename} com shape {df_aux.shape} resultando em {dfs[nm_base].shape}")
                    del df_aux
                    print('####')
        
                    
    return dfs
            

def identifica_separador(arquivo, encoding='ISO-8859-1'):
    seps = [',', '|', ';']
    sep = ';'
    n_cols = 0
    first_line = ""
    temHeader = True
    with open(arquivo, 'r', encoding=encoding) as f:
        lines = 0
        line = f.readline()
        first_line = line
        chars = {}
                                            
        while line and lines < 5:
            for sep in seps:
                nsep = len(line.split(sep))
                if nsep > 1:
                    if sep not in chars:
                        chars[sep] = nsep
                    else:
                        if chars[sep] != nsep:
                            del chars[sep]
                            
            lines += 1 
            line = f.readline()        
                        
            dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
            for k in chars:
                sep, n_cols = k, chars[k]

    hd = first_line.split(sep)

    for field in hd:
        if field == None or len(field) == 0 or ' ' in field.strip():
            temHeader = False
    
    return sep, n_cols, temHeader
      
def salva_por_arquivo_banco(dir_base: str, sourcers, engine):
    for sourcer in sourcers:
        print('####')
        print("Origem: ", sourcer['descricao'])
        list_dir = os.listdir(os.path.join(dir_base, sourcer['descricao']))
        list_dir.sort()
        schema = sourcer['descricao']
        
        for filename in list_dir:
            
            
            arquivo = os.path.join(dir_base, sourcer['descricao'], filename)
            if os.path.isfile(arquivo) and '.csv' in filename:
                sep, n_cols, temHeader = identifica_separador(arquivo)
                tab_name = '_'.join(filename.split('.')[:-1])
                
                copy = f"""
                            COPY {schema}.{tab_name}
                            FROM '/mnt/{sourcer['descricao']}/{filename}'
                            DELIMITER '{sep}'
                            ENCODING 'ISO-8859-1'
                            CSV HEADER;
                        """
                params = {}
                
                if not temHeader:
                    header = []
                    for i in range(n_cols):
                        header.append(f"h_{i}")
                    params['header'] = None
                    params['names'] = header
                
                if n_cols <= 1600:
                    df = pd.read_csv(arquivo, encoding='ISO-8859-1', sep=sep, engine='c', low_memory=False, nrows=2000, **params)
                    #df = pd.read_csv(arquivo, encoding='ISO-8859-1', sep=sep, engine='pyarrow')
                    print(f"Adicionando estrutura: {filename} com shape {df.shape}")
                    #df.iloc[0:1,:].to_sql(tab_name, schema=schema, con=engine, chunksize = 5000, index=False, method=None, if_exists='replace')
                    df.iloc[0:1,:].to_sql(tab_name, schema=schema, con=engine, chunksize = 5000, index=False, method=None)
                    del df
                    print(f"Adicionando dados: {schema}.{tab_name}")
                    with engine.connect() as connection:
                        connection.execute(text(f"truncate table {schema}.{tab_name}"))
                        connection.commit()
                        connection.execute(text(copy))
                        connection.commit()
                else:
                    print(f"{schema}.{tab_name} não adicionado por ter mais de 1600 colunas: {n_cols} colunas")
    
    
    
if __name__ == "__main__":
    engine = inicia_engine()
    salva_por_arquivo_banco(DATA_DIR, default_sourcers, engine)
    