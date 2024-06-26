# Carregar bibliotecas
library (tidyverse)
library(dplyr)
library(readxl)
library(formattable)

#Estabelecer diretorios
setwd("D:/Profissional/RBCIP/Base de dados Indicadores INEP")

#Abrir todos os arquivo do diretório (alterar o conteúdo entre aspas pelo endereço no qual está salvo o arquivo)
# Defina o caminho da pasta
path <- "D:/Profissional/RBCIP/Base de dados Indicadores INEP"

# Lista todos os arquivos Excel da pasta
files <- list.files(path, pattern = "\\.(xlsx|xls)$", full.names = TRUE)

# Ler cada arquivo e atribuir a um dataframe separado
for (file in files) {
  # Extrair o nome base do arquivo (sem extensão)
  data_name <- tools::file_path_sans_ext(basename(file))
  
  # Garantir que o nome seja válido para um objeto em R (sem espaços, caracteres especiais, etc.)
  data_name <- make.names(data_name, unique = TRUE)
  
  # Ler o arquivo e atribuir ao dataframe com o nome base do arquivo
  assign(data_name, read_excel(file))
}

################################################################################
#Indicador Adequação da Formação Docente - AFD
################################################################################

# Unindo os três dataframes
afd_union <- rbind(AFD_MUNICIPIOS_2020, AFD_MUNICIPIOS_2021, AFD_MUNICIPIOS_2022)

# Tornando a linha 10 o cabeçalho
colnames(afd_union) <- afd_union[10, ]
afd_union <- afd_union[-(1:10), ]

# Filtrando as linhas conforme as condições especificadas
afd <- afd_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total", NO_DEPENDENCIA == "Total")



################################################################################
#Indicador Complexidade de Gestão da Escola - ICG
################################################################################

# Unindo os três dataframes
icg_union <- rbind(ICG_MUNICIPIOS_2020, ICG_MUNICIPIOS_2021, ICG_MUNICIPIOS_2022)

# Tornando a linha 8 o cabeçalho
colnames(icg_union) <- icg_union[8, ]
icg_union <- icg_union[-(1:8), ]

# Filtrando as linhas conforme as condições especificadas
icg <- icg_union %>%
  filter(SG_UF == "PR", NO_DEPENDENCIA == "Total", NO_CATEGORIA == "Total")



################################################################################
#Indicador Taxas de Distorção idade-série - TDI
################################################################################

#Defina o caminho da pasta e os nomes dos arquivos:
tdi_union <- rbind(TDI_MUNICIPIOS_2020, TDI_MUNICIPIOS_2021, TDI_MUNICIPIOS_2022)

# Tornar a linha 8 como cabeçalho
col_names <- tdi_union[8, ]
colnames(tdi_union) <- col_names
tdi_union <- tdi_union[-8, ] # Remover a linha 8, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
tdi <- tdi_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total", NO_DEPENDENCIA == "Total")



################################################################################
#Indicador Esforço Docente - IED
################################################################################

#Defina o caminho da pasta e os nomes dos arquivos:
ied_union <- rbind(IED_MUNICIPIOS_2020, IED_MUNICIPIOS_2021, IED_MUNICIPIOS_2022)

# Tornar a linha 8 como cabeçalho
col_names <- ied_union[10, ]
colnames(ied_union) <- col_names
ied_union <- ied_union[-10, ] # Remover a linha 10, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
ied <- ied_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total", NO_DEPENDENCIA == "Total")



################################################################################
#Indicador Média de alunos por turma - ATU
################################################################################

# Defina o caminho da pasta e os nomes dos arquivos:
atu_union <- rbind(ATU_MUNICIPIOS_2020, ATU_MUNICIPIOS_2021, ATU_MUNICIPIOS_2022)

# Tornar a linha 10 como cabeçalho
col_names <- atu_union[8, ]
colnames(atu_union) <- col_names
atu_union <- atu_union[-8, ] # Remover a linha, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
atu <- atu_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total", NO_DEPENDENCIA == "Total")


################################################################################
#Indicador Média de horas-aula diária - HAD
################################################################################

# Defina o caminho da pasta e os nomes dos arquivos:
had_union <- rbind(HAD_MUNICIPIOS_2020, HAD_MUNICIPIOS_2021, HAD_MUNICIPIOS_2022)

# Tornar a linha 8 como cabeçalho
col_names <- had_union[8, ]
colnames(had_union) <- col_names
had_union <- had_union[-8, ] # Remover a linha, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
had <- had_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total", NO_DEPENDENCIA == "Total")



################################################################################
#Indicador Nível socioeconômico - INSE
################################################################################

# Defina o caminho da pasta e os nomes dos arquivos:
inse_union <- bind_rows(INSE_2019_MUNICIPIOS, INSE_2021_municipios)

# Filtrando as linhas conforme as condições especificadas
inse <- inse_union %>%
  filter(CO_UF == "41")



################################################################################
#Indicador Percentual de docentes com curso superior - DSU
################################################################################

# Defina o caminho da pasta e os nomes dos arquivos:
dsu_union <- rbind(DSU_MUNICIPIOS_2020, DSU_MUNICIPIOS_2021, DSU_MUNICIPIOS_2022)

# Tornar a linha 8 como cabeçalho
col_names <- dsu_union[9, ]
colnames(dsu_union) <- col_names
dsu_union <- dsu_union[-9, ] # Remover a linha, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
dsu <- dsu_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total", NO_DEPENDENCIA == "Total")



################################################################################
#Indicador Regularidade do corpo docente - IRD
################################################################################

# Defina o caminho da pasta e os nomes dos arquivos:
ird_union <- rbind(IRD_MUNICIPIOS_2020, IRD_MUNICIPIOS_2021, IRD_MUNICIPIOS_2022)

# Tornar a linha 9 como cabeçalho
col_names <- ird_union[9, ]
colnames(ird_union) <- col_names
ird_union <- ird_union[-9, ] # Remover a linha, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
ird <- ird_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total", NO_DEPENDENCIA == "Total")



################################################################################
#Indicador Remuneração média dos docentes - RED
################################################################################

# Defina o caminho da pasta e os nomes dos arquivos:
red_union <- rbind(Remuneracao_docentes_Municipios_2018, Remuneracao_docentes_Municipios_2019, Remuneracao_docentes_Municipios_2020)

# Tornar a linha como cabeçalho
col_names <- red_union[8, ]
colnames(red_union) <- col_names
red_union <- red_union[-8, ] # Remover a linha, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
red <- red_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total")



################################################################################
#Taxas de não resposta - TNR
################################################################################

# Defina o caminho da pasta e os nomes dos arquivos:
tnr_union <- rbind(tnr_municipios_2020, tnr_municipios_2021, tnr_municipios_2022)

# Tornar a linha como cabeçalho
col_names <- tnr_union[8, ]
colnames(tnr_union) <- col_names
tnr_union <- tnr_union[-8, ] # Remover a linha, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
tnr <- tnr_union %>%
  filter(SG_UF == "PR", TIPOLOCA == "Total", DEPENDAD == "Total")



################################################################################
#Taxas de rendimento - ITR
################################################################################

# Defina o caminho da pasta e os nomes dos arquivos:
itr_union <- rbind(tx_rend_municipios_2020, tx_rend_municipios_2021, tx_rend_municipios_2022)

# Tornar a linha como cabeçalho
col_names <- itr_union[8, ]
colnames(itr_union) <- col_names
itr_union <- itr_union[-8, ] # Remover a linha, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
itr <- itr_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total", NO_DEPENDENCIA == "Total")



################################################################################
#Taxas de transição - ITT
################################################################################

# Defina o caminho da pasta e os nomes dos arquivos:
itt_union <- rbind(tx_rend_municipios_2020, tx_rend_municipios_2021, tx_rend_municipios_2022)

# Tornar a linha como cabeçalho
col_names <- itt_union[8, ]
colnames(itt_union) <- col_names
itt_union <- itt_union[-8, ] # Remover a linha, agora que ela se tornou o cabeçalho

# Filtrando as linhas conforme as condições especificadas
itt <- itt_union %>%
  filter(SG_UF == "PR", NO_CATEGORIA == "Total", NO_DEPENDENCIA == "Total")


################################################################################
#Incluindo as informações das regiões educacionais
################################################################################

# Convertendo a coluna CO_MUNICIPIO em regiões_mun para character
regiões_mun$CO_MUNICIPIO <- as.character(regiões_mun$CO_MUNICIPIO)

# Lista dos dataframes que você quer alterar
dataframes_nomes <- list(afd, icg, tdi, ied, atu, had, inse, dsu, ird, red, tnr, itr, itt)

# Função para converter CO_MUNICIPIO para character, adicionar a coluna e reordená-la
add_regiao <- function(df) {
  df$CO_MUNICIPIO <- as.character(df$CO_MUNICIPIO)
  
  df <- df %>%
    left_join(select(regiões_mun, CO_MUNICIPIO, Regiao_educacao), by = "CO_MUNICIPIO") %>%
    select(Regiao_educacao, everything())
  return(df)
}

# Aplicando a função a cada dataframe
dataframes_modificados <- lapply(dataframes_nomes, add_regiao)

# Atribuindo os dataframes modificados de volta aos seus nomes originais
list_of_vars <- c("afd", "icg", "tdi", "ied", "atu", "had", "inse", "dsu", "ird", "red", "tnr", "itr", "itt")

for (i in 1:length(dataframes_modificados)) {
  assign(list_of_vars[i], dataframes_modificados[[i]])
}


################################################################################
#Criando os arquivos .xlsx
################################################################################
write_xlsx(afd, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Adequação da Formação Docente.xlsx")
write_xlsx(icg, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Complexidade de Gestão da Escola.xlsx")
write_xlsx(tdi, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Taxas de Distorção idade-série.xlsx")
write_xlsx(ied, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Esforço Docente.xlsx")
write_xlsx(atu, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Média de alunos por turma.xlsx")
write_xlsx(had, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Média de horas-aula diária.xlsx")
write_xlsx(inse, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Nível socioeconômico.xlsx")
write_xlsx(dsu, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Percentual de docentes com curso superior.xlsx")
write_xlsx(ird, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Regularidade do corpo docente.xlsx")
write_xlsx(red, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Remuneração média dos docentes.xlsx")
write_xlsx(tnr, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Taxas de não resposta.xlsx")
write_xlsx(itr, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Taxas de rendimento.xlsx")
write_xlsx(itt, path = "D:/Profissional/RBCIP/Base tratada Indicadores INEP/Taxas de transição.xlsx")
