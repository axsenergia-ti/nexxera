from dotenv import load_dotenv
import os
import shutil
import funcao_diretorio as vd
import logging
# Carregar variáveis de ambiente do arquivo .env no mesmo diretório
load_dotenv()

# Configuração do logger
logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', encoding='utf-8')

DIRETORIO_ORIGEM = "C:\Senior\Sapiens\Arquivos\PE\REMESSA"
DIRETORIO_DESTINO_SKYLINE_RP = 'C:\skyline\REMESSA_PAGAMENTOS'
DIRETORIO_RETORNO = 'C:\skyline\RETORNO'
DIRETORIO_DESTINO_SKYLINE_RP_RETORNO = 'C:\Senior\Sapiens\Arquivos\PE\RETORNO'

arquivos = vd.verifica_diretorio(DIRETORIO_ORIGEM,DIRETORIO_DESTINO_SKYLINE_RP)

if not arquivos:
    logging.info('Não ha arquivos a serem movidos')
else:
    logging.info(f'Os arquivos', arquivos, 'foram movidos com sucesso')

arvivos_retorno = vd.retorno_pagamento(DIRETORIO_RETORNO,DIRETORIO_DESTINO_SKYLINE_RP_RETORNO)

if not arquivos:
    logging.info('Não ha arquivos a serem movidos')
else:
    logging.info(f'Os arquivos', arquivos, 'foram movidos com sucesso')