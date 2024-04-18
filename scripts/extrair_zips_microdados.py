from configs import DATA_DIR, default_sourcers, TIPO_MICRODADOS
import os
import zipfile
import re

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
                                if not re.search('[0-9]{4}\.[a-z]{3}', name_file):
                                    r = re.search('[0-9]{4}', file)
                                    if r:
                                        ano = r.group()
                                    else:
                                        ano = "SANO"
                                    name_file = name_file[:-4] + '_' + ano + name_file[-4:]
                                with open(os.path.join(DATA_DIR, source['descricao'], name_file), 'wb') as f:
                                    f.write(content)


if __name__ == "__main__":
    extrair_csvs(default_sourcers)
                
            
      

