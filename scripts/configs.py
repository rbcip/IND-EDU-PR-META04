import os

CERT="INEP.pem"
TMP_DIR="../tmp/"
DATA_DIR="../dados/csv/"
ZIP_PATH="../zips"

TIPO_INDICADOR = "indicadores"
TIPO_MICRODADOS = "microdados"
OUTROS_INDICADORES = "outros_indicadores" 


default_sourcers = [
    #{"tipo": TIPO_MICRODADOS, "descricao": "censoescolar", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar", "diretorio_zip": os.path.join(ZIP_PATH, "censoescolar"), 'filtro': {'SG_UF': 'PR'}},
    #{"tipo": TIPO_MICRODADOS, "descricao": "encceja", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/encceja", "diretorio_zip": os.path.join(ZIP_PATH, "encceja"), 'filtro': {'SG_UF_PROVA': 'PR'}},
    {"tipo": TIPO_MICRODADOS, "descricao": "saeb", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb", "diretorio_zip": os.path.join(ZIP_PATH, "saeb"), 'filtro': {'SG_UF_ESC': '41-PR'}},
    #{"tipo": TIPO_MICRODADOS, "descricao": "enem", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem", "diretorio_zip": os.path.join(ZIP_PATH, "enem"), 'filtro': {'CO_UF': 'PR'}},
    
    #{"tipo": TIPO_INDICADOR, "descricao": "adequacao-da-formacao-docente", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/adequacao-da-formacao-docente/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "adequacao-da-formacao-docente"), 'filtro': {}, 'header_line': 10},
    #{"tipo": TIPO_INDICADOR, "descricao": "complexidade-de-gestao-da-escola", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/complexidade-de-gestao-da-escola/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "complexidade-de-gestao-da-escola"), 'filtro': {}, 'header_line': 8},
    #{"tipo": TIPO_INDICADOR, "descricao": "esforco-docente", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/esforco-docente/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "esforco-docente"), 'filtro': {}, 'header_line': 10},
    #{"tipo": TIPO_INDICADOR, "descricao": "media-de-alunos-por-turma", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/media-de-alunos-por-turma/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "media-de-alunos-por-turma"), 'filtro': {}, 'header_line': 10},
    #{"tipo": TIPO_INDICADOR, "descricao": "media-de-horas-aula-diaria", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/media-de-horas-aula-diaria/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "media-de-horas-aula-diaria"), 'filtro': {}, 'header_line': 9},
    #{"tipo": TIPO_INDICADOR, "descricao": "nivel-socioeconomico", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/nivel-socioeconomico/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "nivel-socioeconomico"), 'filtro': {}, 'header_line': 1},
    #{"tipo": TIPO_INDICADOR, "descricao": "percentual-de-docentes-com-curso-superior", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/percentual-de-docentes-com-curso-superior/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "percentual-de-docentes-com-curso-superior"), 'filtro': {}, 'header_line': 10},
    #{"tipo": TIPO_INDICADOR, "descricao": "regularidade-do-corpo-docente", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/regularidade-do-corpo-docente/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "regularidade-do-corpo-docente"), 'filtro': {}, 'header_line': 9},
    #{"tipo": TIPO_INDICADOR, "descricao": "remuneracao-media-dos-docentes", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/remuneracao-media-dos-docentes/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "remuneracao-media-dos-docentes"), 'filtro': {}, 'header_line': 8},
    #{"tipo": TIPO_INDICADOR, "descricao": "taxas-de-distorcao-idade-serie", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-distorcao-idade-serie/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "taxas-de-distorcao-idade-serie"), 'filtro': {}, 'header_line': 8},
    #{"tipo": TIPO_INDICADOR, "descricao": "taxas-de-nao-resposta", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-nao-resposta/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "taxas-de-nao-resposta"), 'filtro': {}, 'header_line': 8},
    {"tipo": TIPO_INDICADOR, "descricao": "taxas-de-transicao", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-transicao/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "taxas-de-transicao"), 'filtro': {}, 'header_line': 8},
    #{"tipo": TIPO_INDICADOR, "descricao": "taxas-de-rendimento-escolar", "url": "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar/{ano}", "diretorio_zip": os.path.join(ZIP_PATH, "taxas-de-rendimento-escolar"), 'filtro': {}, 'header_line': 8},

]

filters = {
    'microdados_ed_basica': {'SG_UF': 'PR'},
    'suplemento_cursos_tecnicos': {'SG_UF': 'PR'},
    'ts_aluno_2ef': {'ID_UF': '41'},
    'ts_aluno_3em': {'ID_UF': '41'},
    'ts_aluno_3em_ag': {'ID_UF': '41'},
    'ts_aluno_3em_esc': {'ID_UF': '41'},
    'ts_aluno_5ef': {'ID_UF': '41'},
    'ts_aluno_9ef': {'ID_UF': '41'},
    'ts_aluno_34em': {'ID_UF': '41'},
    'ts_diretor': {'ID_UF': '41'},
    'ts_educacao_infantil': {'ID_UF': '41'},
    'ts_escola': {'ID_UF': '41'},
    'ts_item': {'ID_UF': '41'},
    'ts_professor': {'ID_UF': '41'},
    'ts_secretario_municipal': {'ID_UF': '41'},
}

agrupar_arquivos_consolidados = {
    'tx_transicao_brasil_regioes_ufs_2014': 'tx_transicao_brasil_regioes_ufs',
    'tx_transicao_brasil_regioes_ufs_2015': 'tx_transicao_brasil_regioes_ufs',
    'tx_transicao_brasil_regioes_ufs_2016': 'tx_transicao_brasil_regioes_ufs',
    'tx_transicao_brasil_regioes_ufs_2017': 'tx_transicao_brasil_regioes_ufs',
    'tx_transicao_brasil_regioes_ufs_2018': 'tx_transicao_brasil_regioes_ufs',
    'tx_transicao_brasil_regioes_ufs_2019': 'tx_transicao_brasil_regioes_ufs',
    'tx_transicao_brasil_regioes_ufs_2020': 'tx_transicao_brasil_regioes_ufs',
    'tx_transicao_brasil_regioes_ufs_2021': 'tx_transicao_brasil_regioes_ufs',
}

base_header1 = ['Ano', 'Regiao', 'Localizacao', 'Rede', 'Tx_de_Nao_Resp_Fund8e9_Total',	'Tx_de_Nao_Resp_Fund8e9_Anos_Iniciais1_5', 'Tx_de_Nao_Resp_Fund8e9_Anos_Finais6_9', 'Tx_de_Nao_Resp_Fund8e9_1_Ano', 'Tx_de_Nao_Resp_Fund8e9_2_Ano', 'Tx_de_Nao_Resp_Fund8e9_3_Ano', 'Tx_de_Nao_Resp_Fund8e9_4_Ano', 'Tx_de_Nao_Resp_Fund8e9_5_Ano', 'Tx_de_Nao_Resp_Fund8e9_6_Ano', 'Tx_de_Nao_Resp_Fund8e9_7_Ano', 'Tx_de_Nao_Resp_Fund8e9_8_Ano', 'Tx_de_Nao_Resp_Fund8e9_9_Ano',
                'Tx_de_Nao_Resp_Medio_Total',	'Tx_de_Nao_Resp_Medio_1_Ano', 'Tx_de_Nao_Resp_Medio_2_Ano', 'Tx_de_Nao_Resp_Medio_3_Ano', 'Tx_de_Nao_Resp_Medio_4_Ano', 'Total_Medio_Nao_Seriado']

base_header2 = ['Ano', 'Abrangencia_Regiao', 'Dependencia', 'EscolaridadeDocente', 'NrDocentesCenso', 'PorcLocalizadoRAIS', 'quartil1', 'Mediana', 'Média', 'quartil3', 'DesvioPadrao', 'CHSemanalMedia', 'RemuneracaoMedia40H']

base_header3 = ['Ano', 'Regiao', 'Localizacao', 'Rede', 'Tx_de_distorcao8e9_Total',	'Tx_de_distorcao8e9_Anos_1_5', 'Tx_de_distorcao8e9_Anos_6_9', 'Tx_de_distorcao8e9_1_Ano', 'Tx_de_distorcao8e9_2_Ano', 'Tx_de_distorcao8e9_3_Ano', 'Tx_de_distorcao8e9_4_Ano', 'Tx_de_distorcao8e9_5_Ano', 'Tx_de_distorcao8e9_6_Ano', 'Tx_de_distorcao8e9_7_Ano', 'Tx_de_distorcao8e9_8_Ano', 'Tx_de_distorcao8e9_9_Ano',
                'Tx_de_distorcao_Medio_Total',	'Tx_de_distorcao_Medio_1_Serie', 'Tx_de_distorcao_Medio_2_Serie', 'Tx_de_distorcao_Medio_3_Serie', 'Tx_de_distorcao_Medio_4_Serie']

base_header4 = ['Ano', 'Regiao', 'Localizacao', 'Rede', 
                'Tx_promocao_Total',	'Tx_promocao_Anos_1_5', 'Tx_promocao_Anos_6_9', 'Tx_promocao_1_Ano', 'Tx_promocao_2_Ano', 'Tx_promocao_3_Ano', 'Tx_promocao_4_Ano', 'Tx_promocao_5_Ano', 'Tx_promocao_6_Ano', 'Tx_promocao_7_Ano', 'Tx_promocao_8_Ano', 'Tx_promocao_9_Ano',
                'Tx_promocao_Medio_Total',	'Tx_promocao_Medio_1_Serie', 'Tx_promocao_Medio_2_Serie', 'Tx_promocao_Medio_3_Serie',
                
                'Tx_repetencia_Total',	'Tx_repetencia_Anos_1_5', 'Tx_repetencia_Anos_6_9', 'Tx_repetencia_1_Ano', 'Tx_repetencia_2_Ano', 'Tx_repetencia_3_Ano', 'Tx_repetencia_4_Ano', 'Tx_repetencia_5_Ano', 'Tx_repetencia_6_Ano', 'Tx_repetencia_7_Ano', 'Tx_repetencia_8_Ano', 'Tx_repetencia_9_Ano',
                'Tx_repetencia_Medio_Total',	'Tx_repetencia_Medio_1_Serie', 'Tx_repetencia_Medio_2_Serie', 'Tx_repetencia_Medio_3_Serie',
                
                'Tx_evasao_Total',	'Tx_evasao_Anos_1_5', 'Tx_evasao_Anos_6_9', 'Tx_evasao_1_Ano', 'Tx_evasao_2_Ano', 'Tx_evasao_3_Ano', 'Tx_evasao_4_Ano', 'Tx_evasao_5_Ano', 'Tx_evasao_6_Ano', 'Tx_evasao_7_Ano', 'Tx_evasao_8_Ano', 'Tx_evasao_9_Ano',
                'Tx_evasao_Medio_Total',	'Tx_evasao_Medio_1_Serie', 'Tx_evasao_Medio_2_Serie', 'Tx_evasao_Medio_3_Serie',
                
                'Migracao_EJA_Total',	'Migracao_EJA_Anos_1_5', 'Migracao_EJA_Anos_6_9', 'Migracao_EJA_1_Ano', 'Migracao_EJA_2_Ano', 'Migracao_EJA_3_Ano', 'Migracao_EJA_4_Ano', 'Migracao_EJA_5_Ano', 'Migracao_EJA_6_Ano', 'Migracao_EJA_7_Ano', 'Migracao_EJA_8_Ano', 'Migracao_EJA_9_Ano',
                'Migracao_EJA_Medio_Total',	'Migracao_EJA_Medio_1_Serie', 'Migracao_EJA_Medio_2_Serie', 'Migracao_EJA_Medio_3_Serie',
                ]

base_header5 = ['Ano', 'Regiao_UF_Abrangencia', 'Localizacao', 'Rede', 
                'Tx_aprovacao_Total',	'Tx_aprovacao_Anos_1_5', 'Tx_aprovacao_Anos_6_9', 'Tx_aprovacao_1_Ano', 'Tx_aprovacao_2_Ano', 'Tx_aprovacao_3_Ano', 'Tx_aprovacao_4_Ano', 'Tx_aprovacao_5_Ano', 'Tx_aprovacao_6_Ano', 'Tx_aprovacao_7_Ano', 'Tx_aprovacao_8_Ano', 'Tx_aprovacao_9_Ano',
                'Tx_aprovacao_Medio_Total',	'Tx_aprovacao_Medio_1_Serie', 'Tx_aprovacao_Medio_2_Serie', 'Tx_aprovacao_Medio_3_Serie', 'Tx_aprovacao_Medio_4_Serie', 'Tx_aprovacao_Medio_Nao_Seriado',
                
                'Tx_reprovacao_Total',	'Tx_reprovacao_Anos_1_5', 'Tx_reprovacao_Anos_6_9', 'Tx_reprovacao_1_Ano', 'Tx_reprovacao_2_Ano', 'Tx_reprovacao_3_Ano', 'Tx_reprovacao_4_Ano', 'Tx_reprovacao_5_Ano', 'Tx_reprovacao_6_Ano', 'Tx_reprovacao_7_Ano', 'Tx_reprovacao_8_Ano', 'Tx_reprovacao_9_Ano',
                'Tx_reprovacao_Medio_Total',	'Tx_reprovacao_Medio_1_Serie', 'Tx_reprovacao_Medio_2_Serie', 'Tx_reprovacao_Medio_3_Serie', 'Tx_reprovacao_Medio_4_Serie', 'Tx_reprovacao_Medio_Nao_Seriado',
                
                'Tx_abandono_Total',	'Tx_abandono_Anos_1_5', 'Tx_abandono_Anos_6_9', 'Tx_abandono_1_Ano', 'Tx_abandono_2_Ano', 'Tx_abandono_3_Ano', 'Tx_abandono_4_Ano', 'Tx_abandono_5_Ano', 'Tx_abandono_6_Ano', 'Tx_abandono_7_Ano', 'Tx_abandono_8_Ano', 'Tx_abandono_9_Ano',
                'Tx_abandono_Medio_Total',	'Tx_abandono_Medio_1_Serie', 'Tx_abandono_Medio_2_Serie', 'Tx_abandono_Medio_3_Serie', 'Tx_abandono_Medio_4_Serie', 'Tx_abandono_Medio_Nao_Seriado',
                ]

base_header6 = ['Ano', 'Regiao_Abrangencia', 'Localizacao', 'Rede', 
                'PercEscSegNvlIndCmplxGestaoN1', 'PercEscSegNvlIndCmplxGestaoN2', 'PercEscSegNvlIndCmplxGestaoN3', 'PercEscSegNvlIndCmplxGestaoN4', 'PercEscSegNvlIndCmplxGestaoN5', 'PercEscSegNvlIndCmplxGestaoN6'
                ]

base_header7 = ['Ano', 'Regiao_Abrangencia', 'Localizacao', 'Rede', 
                'Media_Alunos_Turma_infantil_total', 'Media_Alunos_Turma_infantil_creche', 'Media_Alunos_Turma_infantil_preescola',
                'Media_Alunos_Turma_fund_Total',	'Media_Alunos_Turma_fund_Anos_1_5', 'Media_Alunos_Turma_fund_Anos_6_9', 'Media_Alunos_Turma_fund_1_Ano', 'Media_Alunos_Turma_fund_2_Ano', 'Media_Alunos_Turma_fund_3_Ano', 'Media_Alunos_Turma_fund_4_Ano', 'Media_Alunos_Turma_fund_5_Ano', 'Media_Alunos_Turma_fund_6_Ano', 'Media_Alunos_Turma_fund_7_Ano', 'Media_Alunos_Turma_fund_8_Ano', 'Media_Alunos_Turma_fund_9_Ano', 'Media_Alunos_Turma_fund_MultietapaUnificada',
                'Media_Alunos_Turma_medio_Total',	'Media_Alunos_Turma_medio_1_Serie', 'Media_Alunos_Turma_medio_2_Serie', 'Media_Alunos_Turma_medio_3_Serie', 'Media_Alunos_Turma_medio_4_Serie', 'Media_Alunos_Turma_medio_4_NSeriado']

base_header8 = ['Ano', 'Regiao_Abrangencia', 'Localizacao', 'Rede', 
                'Media_HoraAula_Diaria_infantil_total', 'Media_HoraAula_Diaria_infantil_creche', 'Media_HoraAula_Diaria_infantil_preescola',
                'Media_HoraAula_Diaria_fund_Total',	'Media_HoraAula_Diaria_fund_Anos_1_5', 'Media_HoraAula_Diaria_fund_Anos_6_9', 'Media_HoraAula_Diaria_fund_1_Ano', 'Media_HoraAula_Diaria_fund_2_Ano', 'Media_HoraAula_Diaria_fund_3_Ano', 'Media_HoraAula_Diaria_fund_4_Ano', 'Media_HoraAula_Diaria_fund_5_Ano', 'Media_HoraAula_Diaria_fund_6_Ano', 'Media_HoraAula_Diaria_fund_7_Ano', 'Media_HoraAula_Diaria_fund_8_Ano', 'Media_HoraAula_Diaria_fund_9_Ano',
                'Media_HoraAula_Diaria_medio_Total',	'Media_HoraAula_Diaria_medio_1_Serie', 'Media_HoraAula_Diaria_medio_2_Serie', 'Media_HoraAula_Diaria_medio_3_Serie', 'Media_HoraAula_Diaria_medio_4_Serie', 'Media_HoraAula_Diaria_medio_NSeriado']

base_header9 = ['CO_UF', 'SIGLA_UF', 'NOME_UF', 'TP_TIPO_REDE', 'TP_LOCALIZACAO', 'TP_CAPITAL', 'QTD_ALUNOS_INSE', 'MEDIA_INSE', 'PC_NIVEL_1', 'PC_NIVEL_2', 'PC_NIVEL_3', 'PC_NIVEL_4', 'PC_NIVEL_5', 'PC_NIVEL_6', 'PC_NIVEL_7', 'PC_NIVEL_8']

base_header10 = ['Ano', 'Regiao_Abrangencia', 'Localizacao', 'Rede', 
                'Perc_Doc_Curso_Sup_infantil_total', 'Perc_Doc_Curso_Sup_infantil_creche', 'Perc_Doc_Curso_Sup_infantil_preescola',
                'Perc_Doc_Curso_Sup_fund_Total',	'Perc_Doc_Curso_Sup_fund_Anos_1_5', 'Perc_Doc_Curso_Sup_fund_Anos_6_9',
                'Perc_Doc_Curso_Sup_medio',	'Perc_Doc_Curso_Sup_profissionalizante', 'Perc_Doc_Curso_Sup_eja', 'Perc_Doc_Curso_Sup_especial']

base_header11 = ['Ano', 'Regiao_UF_Abrangencia', 'Localizacao', 'Rede', 
                'Tx_promocao_Total',	'Tx_promocao_Anos_1_5', 'Tx_promocao_Anos_6_9', 'Tx_promocao_1_Ano', 'Tx_promocao_2_Ano', 'Tx_promocao_3_Ano', 'Tx_promocao_4_Ano', 'Tx_promocao_5_Ano', 'Tx_promocao_6_Ano', 'Tx_promocao_7_Ano', 'Tx_promocao_8_Ano', 'Tx_promocao_9_Ano',
                'Tx_promocao_Medio_Total',	'Tx_promocao_Medio_1_Serie', 'Tx_promocao_Medio_2_Serie', 'Tx_promocao_Medio_3_Serie',
                
                'Tx_repetencia_Total',	'Tx_repetencia_Anos_1_5', 'Tx_repetencia_Anos_6_9', 'Tx_repetencia_1_Ano', 'Tx_repetencia_2_Ano', 'Tx_repetencia_3_Ano', 'Tx_repetencia_4_Ano', 'Tx_repetencia_5_Ano', 'Tx_repetencia_6_Ano', 'Tx_repetencia_7_Ano', 'Tx_repetencia_8_Ano', 'Tx_repetencia_9_Ano',
                'Tx_repetencia_Medio_Total',	'Tx_repetencia_Medio_1_Serie', 'Tx_repetencia_Medio_2_Serie', 'Tx_repetencia_Medio_3_Serie',
                
                'Tx_evasao_Total',	'Tx_evasao_Anos_1_5', 'Tx_evasao_Anos_6_9', 'Tx_evasao_1_Ano', 'Tx_evasao_2_Ano', 'Tx_evasao_3_Ano', 'Tx_evasao_4_Ano', 'Tx_evasao_5_Ano', 'Tx_evasao_6_Ano', 'Tx_evasao_7_Ano', 'Tx_evasao_8_Ano', 'Tx_evasao_9_Ano',
                'Tx_evasao_Medio_Total', 'Tx_evasao_Medio_1_Serie', 'Tx_evasao_Medio_2_Serie', 'Tx_evasao_Medio_3_Serie',
                
                'Tx_eja_Total',	'Tx_eja_Anos_1_5', 'Tx_eja_Anos_6_9', 'Tx_eja_1_Ano', 'Tx_eja_2_Ano', 'Tx_eja_3_Ano', 'Tx_eja_4_Ano', 'Tx_eja_5_Ano', 'Tx_eja_6_Ano', 'Tx_eja_7_Ano', 'Tx_eja_8_Ano', 'Tx_eja_9_Ano',
                'Tx_eja_Medio_Total',	'Tx_eja_Medio_1_Serie', 'Tx_eja_Medio_2_Serie', 'Tx_eja_Medio_3_Serie'
                ]


use_header = {
        'tnr_regioes': {'line': 9, 'header': base_header1},
        
        'tnr_ufs': {'line': 9, 'header': base_header1},
        
        'taxa no-resposta regies': {'line': 8, 'header': base_header1},
        
        'taxa no-resposta brasil': {'line': 8, 'header': base_header1},
        
        'tnr_brasil': {'line': 9, 'header': base_header1},
        
        'taxa no-resposta uf': {'line': 8, 'header': base_header1},
        
        'tnr_brasil_regioes_ufs': {'line': 8, 'header': base_header1},
        
        ##############################
        
        'remuneracao_docentes_brasil': {'line':8, 'header': base_header2},
        
        'remuneracao_docentes_uf': {'line':8, 'header': base_header2[:2] + ['UF'] + base_header2[2:]},
        
        ##############################
        
        'tdi brasil -': {'line': 8, 'header': base_header3},
        
        'tdi regies -': {'line': 8, 'header': base_header3},
        
        'tdi uf -': {'line': 8, 'header': base_header3[:2] + ['UF'] + base_header3[2:]},
        
        'tdi_brasil': {'line': 8, 'header': base_header3},
        
        'tdi_brasil_regioes_ufs': {'line': 8, 'header': base_header3},
        
        'tdi_regioes': {'line': 8, 'header': base_header3},
        
        'tdi_ufs': {'line': 8, 'header': base_header3[:2] + ['UF'] + base_header3[2:]},
        
        ##############################
        
        'tx_transicao_brasil_regioes_ufs': {'line': 8, 'header': base_header4},
        
        ##############################
        
        'taxas rendimento regies': {'line': 8, 'header': base_header5},
        
        'taxas rendimentos brasil': {'line': 8, 'header': base_header5},
        
        'taxas rendimentos regies': {'line': 8, 'header': base_header5},
        
        'taxas rendimentos uf': {'line': 8, 'header': base_header5},
        
        'tx_rend_brasil': {'line': 8, 'header': base_header5},
        
        'tx_rend_brasil_regioes_ufs': {'line': 8, 'header': base_header5},
        
        'tx_rend_reg': {'line': 9, 'header': base_header5},
        
        'tx_rend_ufs': {'line': 9, 'header': base_header5},
        
        'tx_rend_regioes': {'line': 8, 'header': base_header5},
        
        ##############################
        
        'icg_brasil': {'line': 8, 'header': base_header6},
        
        'icg_brasil_regioes_ufs': {'line': 8, 'header': base_header6},
        
        'icg_regioes': {'line': 8, 'header': base_header6},
        
        'icg_ufs': {'line': 8, 'header': base_header6[:2] + ['UF'] + base_header6[2:]},
        
        ##############################
        
        'atu_brasil': {'line': 9, 'header': base_header7},
        
        'atu_brasil_regioes_ufs': {'line': 8, 'header': base_header7},
        
        'atu_regioes': {'line': 9, 'header': base_header7},
        
        'mdia alunos turma brasil': {'line': 9, 'header': base_header7},
        
        'mdia alunos turma regies': {'line': 9, 'header': base_header7},
        
        'atu_uf': {'line': 9, 'header': base_header7[:2] + ['UF'] + base_header7[2:]},
        
        'atu_ufs': {'line': 8, 'header': base_header7[:2] + ['UF'] + base_header7[2:]},
        
        'mdia alunos turma ufs': {'line': 9, 'header': base_header7[:2] + ['UF'] + base_header7[2:]},
        
        ##############################
        
        'had_brasil': {'line': 8, 'header': base_header8},
        
        'had_brasil_regioes_ufs': {'line': 8, 'header': base_header8},
        
        'mdia horas-aula regies': {'line': 8, 'header': base_header8},
        
        'mdia horas-aula brasil': {'line': 8, 'header': base_header8},
        
        'had_regioes': {'line': 8, 'header': base_header8},
        
        'had_uf': {'line': 8, 'header': base_header8[:2] + ['UF'] + base_header8[2:]},
        
        'had_ufs': {'line': 8, 'header': base_header8[:2] + ['UF'] + base_header8[2:]},
     
        'mdia horas-aula ufs': {'line': 8, 'header': base_header8[:2] + ['UF'] + base_header8[2:]},
        
        ##############################
        
        'inse_estados': {'line': 0, 'header': base_header9},
        
        'inse__brasil': {'line': 0, 'header': ['NU_ANO_SAEB', 'TP_TIPO_REDE', 'TP_LOCALIZACAO', 'TP_CAPITAL', 'QTD_ALUNOS_INSE', 'MEDIA_INSE', 'PC_NIVEL_1', 'PC_NIVEL_2', 'PC_NIVEL_3', 'PC_NIVEL_4', 'PC_NIVEL_5', 'PC_NIVEL_6', 'PC_NIVEL_7', 'PC_NIVEL_8']},
        
        ##############################
        
        'dsu - brasil': {'line': 9, 'header': base_header10},
        
        'dsu - estados': {'line': 9, 'header': base_header10},
        
        'dsu - regies': {'line': 9, 'header': base_header10},
        
        'dsu_brasil': {'line': 9, 'header': base_header10},
        
        'dsu_brasil_regioes_ufs': {'line': 9, 'header': base_header10},
        
        'dsu_brasil_regioes_ufs_atualizado': {'line': 9, 'header': base_header10},
        
        'dsu_regioes': {'line': 9, 'header': base_header10},
        
        'dsu_ufs': {'line': 9, 'header': base_header10[:2] + ['UF'] + base_header10[2:]},
        
        'dsu - ufs': {'line': 9, 'header': base_header10[:2] + ['UF', 'COD_UF'] + base_header10[2:]},        
        
        'dsu_uf': {'line': 9, 'header': base_header10[:2] + ['UF', 'COD_UF'] + base_header10[2:]},        
        
        ##############################
        
        'tx_transicao_brasil_regioes_ufs_2014': {'line': 8, 'header': base_header11},
        
        'tx_transicao_brasil_regioes_ufs_2015': {'line': 8, 'header': base_header11},
        
        'tx_transicao_brasil_regioes_ufs_2016': {'line': 8, 'header': base_header11},
        
        'tx_transicao_brasil_regioes_ufs_2017': {'line': 8, 'header': base_header11},
        
        'tx_transicao_brasil_regioes_ufs_2018': {'line': 8, 'header': base_header11},
        
        'tx_transicao_brasil_regioes_ufs_2019': {'line': 8, 'header': base_header11},
        
        'tx_transicao_brasil_regioes_ufs_2020': {'line': 8, 'header': base_header11},
        
        'tx_transicao_brasil_regioes_ufs_2021': {'line': 8, 'header': base_header11}
        
    }

include_head_for_file = {
        'tdi_ufs_2015.xlsx': {2: 'COD_UF'},
        'inse_2021_estados.xlsx': {0: 'NU_ANO_SAEB'},
    }

start_head_for_file = {
        'inse_2019_estados.xlsx': 1,
    }

pre_add_head_file = {
    'inse_2019_estados.xlsx': {'NU_ANO_SAEB': '2019'}
}

pos_add_head = {
        'remuneracao_docentes_brasil': {'UF': '--'},
        
        'tdi brasil -': {'COD_UF': -1, 'UF': '--'},
        
        'tdi regies -': {'COD_UF': -1, 'UF': '--'},
        
        'tdi_brasil': {'COD_UF': -1, 'UF': '--'},
        
        'tdi_brasil_regioes_ufs': {'COD_UF': -1, 'UF': '--'},
        
        'tdi_regioes': {'COD_UF': -1, 'UF': '--'},
        
        'tdi_ufs': {'COD_UF': -1},
        
        'icg_brasil': {'UF': '--'},
        
        'icg_brasil_regioes_ufs': {'UF': '--'},
        
        'icg_regioes': {'UF': '--'},
        
        'atu_brasil': {'UF': '--'},
        
        'atu_brasil_regioes_ufs': {'UF': '--'},
        
        'atu_regioes': {'UF': '--'},
        
        'mdia alunos turma brasil': {'UF': '--'},
        
        'mdia alunos turma regies': {'UF': '--'},
        
        'had_brasil': {'UF': '--'},
        
        'had_brasil_regioes_ufs': {'UF': '--'},
        
        'mdia horas-aula regies': {'UF': '--'},
        
        'mdia horas-aula brasil': {'UF': '--'},
        
        'had_regioes': {'UF': '--'},
        
        'dsu - brasil': {'COD_UF': -1, 'UF': '--'},
        
        'dsu - estados': {'COD_UF': -1, 'UF': '--'},
        
        'dsu - regies': {'COD_UF': -1, 'UF': '--'},
        
        'dsu_brasil': {'COD_UF': -1, 'UF': '--'},
        
        'dsu_brasil_regioes_ufs': {'COD_UF': -1, 'UF': '--'},
        
        'dsu_brasil_regioes_ufs_atualizado': {'COD_UF': -1, 'UF': '--'},
        
        'dsu_regioes': {'COD_UF': -1, 'UF': '--'},
        
        'dsu_ufs': {'COD_UF': -1},
    }

WGET_EXE = '"c:\\Program Files (x86)\\GnuWin32\\bin\\wget.exe"'
#WGET_EXE = '/usr/bin/wget'
