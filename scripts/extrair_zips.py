from configs import DATA_DIR, default_sourcers
import os
import zipfile


def extrair_csvs(sourcers):
    for source in sourcers:
        print(source['descricao'])
        if not os.path.exists(os.path.join(DATA_DIR, source['descricao'])):
            os.mkdir(os.path.join(DATA_DIR, source['descricao']))
            
        list_dir = os.listdir(source['diretorio_zip'])
        for file in list_dir:
            if file[-4: ] == '.zip':
                with zipfile.ZipFile(os.path.join(source['diretorio_zip'], file), 'r') as zip_ref:
                    infiles = zip_ref.namelist()
                    for infile in infiles:
                        if infile[-4:] == '.csv':
                            fin = zip_ref.open(infile)
                            content = fin.read()
                            with open(os.path.join(DATA_DIR, source['descricao'], infile.split('/')[-1].lower()), 'wb') as f:
                                f.write(content)


if __name__ == "__main__":
    extrair_csvs(default_sourcers)
                
            
      

