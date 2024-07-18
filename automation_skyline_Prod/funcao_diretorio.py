import os
import logging
import shutil

#PE

DIRETORIO_ORIGEM = "C:\Senior\Sapiens\Arquivos\CE\REMESSA"
DIRETORIO_DESTINO_SKYLINE_RP = 'C:\skyline\REMESSA_PAGAMENTOS'
DIRETORIO_RETORNO = 'C:\skyline\RETORNO'
DIRETORIO_DESTINO_SKYLINE_RP_RETORNO = 'C:\Senior\Sapiens\Arquivos\PE\RETORNO'

def verifica_diretorio(DIRETORIO_ORIGEM,DIRETORIO_DESTINO_SKYLINE_RP):

    arquivos = []  # Lista para armazenar os nomes dos arquivos
    
    # Verifica se os diretórios de origem e destino estão definidos
    if not DIRETORIO_ORIGEM or not DIRETORIO_DESTINO_SKYLINE_RP:
        logging.error("As variáveis de ambiente DIRETORIO_ORIGEM, DIRETORIO_DESTINO_SKYLINE_RP devem ser definidas.")
        return

    diretorio_fim = "REMESSA"

    # Lista de pastas EMPx
    pastas_emp = [
        "EMP4", "EMP10", "EMP11", "EMP12", "EMP13", "EMP14", "EMP15", 
        "EMP16", "EMP17", "EMP18", "EMP19", "EMP20", "EMP21", "EMP22", 
        "EMP23", "EMP24", "EMP25", "EMP26", "EMP27", "EMP28", "EMP29", "EMP30"
    ]
 
    for pasta_emp in pastas_emp:
        diretorio_pasta_emp = os.path.join(DIRETORIO_ORIGEM, pasta_emp,diretorio_fim)

        # Verifica se a pasta EMPx existe
        if os.path.exists(diretorio_pasta_emp):
            # Lista os arquivos na pasta EMPx
            arquivos_na_pasta = os.listdir(diretorio_pasta_emp)

            if arquivos_na_pasta:
                # Move os arquivos para o diretório de destino

                # Adiciona os nomes dos arquivos à lista 'arquivos'
                arquivos.extend(arquivos_na_pasta)

                for arquivo in arquivos_na_pasta:
                    caminho_origem = os.path.join(diretorio_pasta_emp, arquivo)
                    caminho_destino = os.path.join(DIRETORIO_DESTINO_SKYLINE_RP, arquivo)
                    shutil.move(caminho_origem, DIRETORIO_DESTINO_SKYLINE_RP)
                    logging.info(f"Arquivo '{arquivo}' movido para '{DIRETORIO_DESTINO_SKYLINE_RP}'.")
            else:
                logging.info(f"A pasta '{pasta_emp}' está vazia.")
        else:
            logging.error(f"A pasta '{pasta_emp}' não existe.")

    
    return arquivos

def retorno_pagamento(DIRETORIO_RETORNO, DIRETORIO_DESTINO_SKYLINE_RP_RETORNO):

    pastas_emp = [
        "EMP4", "EMP10", "EMP11", "EMP12", "EMP13", "EMP14", "EMP15", 
        "EMP16", "EMP17", "EMP18", "EMP19", "EMP20", "EMP21", "EMP22", 
        "EMP23", "EMP24", "EMP25", "EMP26", "EMP27", "EMP28", "EMP29", "EMP30"
    ]

    dicionario_de_dados = {
            "NEE1": 4,
            "P8RC": 10,
            "NH0L": 11,
            "REZ7": 12,
            "REXP": 13,
            "STKL": 16,
            "GELM": 17,
            "UCIH": 18,
            "UU2Y": 19,
            "TI3A": 20,
            "WSMR": 21,
            "TF9Y": 22,
            "TT96": 23,
            "????": 24,
            "W9FW": 25
        }
    


#CE
DIRETORIO_ORIGEM = "C:\Senior\Sapiens\Arquivos\CE\REMESSA"
DIRETORIO_DESTINO_SKYLINE_RP = 'C:\skyline\REMESSA_PAGAMENTOS'
DIRETORIO_RETORNO = 'C:\skyline\RETORNO'
DIRETORIO_DESTINO_SKYLINE_RP_RETORNO_CE = 'C:\Senior\Sapiens\Arquivos\CE\RETORNO'
#EXT
DIRETORIO_DESTINO_SKYLINE_RP_RETORNO_IMPEXT = 'C:\Senior\Sapiens\Arquivos\IMPEXT\RETORNO'

def verifica_diretorio(DIRETORIO_ORIGEM,DIRETORIO_DESTINO_SKYLINE_RP):

    arquivos = []  # Lista para armazenar os nomes dos arquivos
    
    # Verifica se os diretórios de origem e destino estão definidos
    if not DIRETORIO_ORIGEM or not DIRETORIO_DESTINO_SKYLINE_RP:
        logging.error("As variáveis de ambiente DIRETORIO_ORIGEM, DIRETORIO_DESTINO_SKYLINE_RP devem ser definidas.")
        return

    diretorio_fim = "REMESSA"

    # Lista de pastas EMPx
    pastas_emp = [
        "EMP4", "EMP10", "EMP11", "EMP12", "EMP13", "EMP14", "EMP15", 
        "EMP16", "EMP17", "EMP18", "EMP19", "EMP20", "EMP21", "EMP22", 
        "EMP23", "EMP24", "EMP25", "EMP26", "EMP27", "EMP28", "EMP29", "EMP30"
    ]
 
    for pasta_emp in pastas_emp:
        diretorio_pasta_emp = os.path.join(DIRETORIO_ORIGEM, pasta_emp,diretorio_fim)

        # Verifica se a pasta EMPx existe
        if os.path.exists(diretorio_pasta_emp):
            # Lista os arquivos na pasta EMPx
            arquivos_na_pasta = os.listdir(diretorio_pasta_emp)

            if arquivos_na_pasta:
                # Move os arquivos para o diretório de destino

                # Adiciona os nomes dos arquivos à lista 'arquivos'
                arquivos.extend(arquivos_na_pasta)

                for arquivo in arquivos_na_pasta:
                    caminho_origem = os.path.join(diretorio_pasta_emp, arquivo)
                    caminho_destino = os.path.join(DIRETORIO_DESTINO_SKYLINE_RP, arquivo)
                    shutil.move(caminho_origem, DIRETORIO_DESTINO_SKYLINE_RP)
                    logging.info(f"Arquivo '{arquivo}' movido para '{DIRETORIO_DESTINO_SKYLINE_RP}'.")
            else:
                logging.info(f"A pasta '{pasta_emp}' está vazia.")
        else:
            logging.error(f"A pasta '{pasta_emp}' não existe.")

    
    return arquivos

def retorno_pagamento(DIRETORIO_RETORNO, DIRETORIO_DESTINO_SKYLINE_RP_RETORNO):

    pastas_emp = [
        "EMP4", "EMP10", "EMP11", "EMP12", "EMP13", "EMP14", "EMP15", 
        "EMP16", "EMP17", "EMP18", "EMP19", "EMP20", "EMP21", "EMP22", 
        "EMP23", "EMP24", "EMP25", "EMP26", "EMP27", "EMP28", "EMP29", "EMP30"
    ]

    dicionario_de_dados = {
            "NEE1": 4,
            "P8RC": 10,
            "NH0L": 11,
            "REZ7": 12,
            "REXP": 13,
            "STKL": 16,
            "GELM": 17,
            "UCIH": 18,
            "UU2Y": 19,
            "TI3A": 20,
            "WSMR": 21,
            "TF9Y": 22,
            "TT96": 23,
            "????": 24,
            "W9FW": 25
        }




# REOTORNO
    arquivos = []  # Lista para armazenar os nomes dos arquivos

    # Verifica se os diretórios de origem e destino estão definidos
    if not DIRETORIO_RETORNO or not DIRETORIO_DESTINO_SKYLINE_RP_RETORNO:
        logging.error("As variáveis de ambiente DIRETORIO_RETORNO, DIRETORIO_DESTINO_SKYLINE_RP_RETORNO devem ser definidas.")
        return
    
    if os.path.exists(DIRETORIO_RETORNO):
        # Lista os arquivos no diretório
        arquivos_na_pasta_retorno = os.listdir(DIRETORIO_RETORNO)

        if arquivos_na_pasta_retorno:
            # Adiciona os nomes dos arquivos à lista 'arquivos'
            arquivos.extend(arquivos_na_pasta_retorno)

            for arquivo in arquivos_na_pasta_retorno:
                
                if len(arquivo) == 29:

                    codigo_empresa = arquivo[4:8].upper()

                    if codigo_empresa in dicionario_de_dados:
                        numero_empresa = dicionario_de_dados[codigo_empresa]
                    else:
                        logging.error(f"Código de empresa desconhecido encontrado no arquivo '{arquivo}'.")
                        continue
                else:

                    codigo_empresa = arquivo[5:9].upper()

                    if codigo_empresa in dicionario_de_dados:
                        numero_empresa = dicionario_de_dados[codigo_empresa]
                    else:
                        logging.error(f"Código de empresa desconhecido encontrado no arquivo '{arquivo}'.")
                        continue

                # Determinar a pasta EMP correspondente ao número da empresa
                pasta_empresa = f"EMP{numero_empresa}"

                #Determina as três primeiras letras do arquivo

                primeirasLetras = arquivo[:3].upper()

                if primeirasLetras == "COB":
                    destino_final = os.path.join(DIRETORIO_DESTINO_SKYLINE_RP_RETORNO_CE, pasta_empresa, "COB_RETORNO RECEBIMENTOS")
                elif primeirasLetras == "PAG":
                    destino_final = os.path.join(DIRETORIO_DESTINO_SKYLINE_RP_RETORNO, pasta_empresa, "PAG_RETORNO")
                elif primeirasLetras == "FOR":
                    destino_final = os.path.join(DIRETORIO_DESTINO_SKYLINE_RP_RETORNO, pasta_empresa, "PAG_RETORNO")
                elif primeirasLetras == "EXT":
                    destino_final = os.path.join(DIRETORIO_DESTINO_SKYLINE_RP_RETORNO_IMPEXT, pasta_empresa, "EXT_RETORNO DE EXTRATO")
                else:
                    logging.error(f"Prefixo desconhecido encontrado no arquivo '{arquivo}'.")
                    continue

                caminho_origem = os.path.join(DIRETORIO_RETORNO, arquivo)
                caminho_destino = os.path.join(destino_final, arquivo)
                shutil.move(caminho_origem, caminho_destino)
                logging.info(f"Arquivo '{arquivo}' movido para '{destino_final}'.")
                print(f"Arquivo '{arquivo}' movido para '{destino_final}'.")
        else:
            logging.info(f"A pasta '{DIRETORIO_RETORNO}' está vazia.")
    else:
        logging.error(f"A pasta '{DIRETORIO_RETORNO}' não existe.")

    return arquivos