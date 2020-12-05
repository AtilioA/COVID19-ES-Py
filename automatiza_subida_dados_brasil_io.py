#!/usr/bin/python3.8

from relatorio_para_csv import relatorio_para_tabela
from COVID19_ES_Py import LeitorRelatorio
import os
from pathlib import Path
import shutil
import webbrowser
import wget

import arrow
import pyperclip


NOW = arrow.now("America/Sao_Paulo")


def automatiza_subida(download=False):
    AGORA = arrow.now("America/Sao_Paulo")

    print(f"""Criando arquivo {Path(f"ES_{AGORA.format('DD-MM-YYYY')}.csv")} ...\n""")

    if download:
        print("Baixando MICRODADOS.csv...")
        wget.download(
            "https://bi.static.es.gov.br/covid19/MICRODADOS.csv",
            "/home/atilioa/Downloads",
        )

    fileOriginalPath = os.path.abspath("/home/atilioa/Downloads/MICRODADOS.csv")
    desktopPath = os.path.abspath("/home/atilioa/Área de Trabalho/")

    filename = str(Path(f"{AGORA.format('DD-MM-YYYY')}.csv"))
    newFilenameAndPath = os.path.join(os.getcwd(), filename)

    try:
        shutil.copy(fileOriginalPath, newFilenameAndPath)
    except FileNotFoundError:
        print("Baixando MICRODADOS.csv...")
        wget.download(
            "https://bi.static.es.gov.br/covid19/MICRODADOS.csv",
            "/home/atilioa/Downloads",
        )
        shutil.copy(fileOriginalPath, newFilenameAndPath)

    print("Planilha da SESA copiada. Gerando relatório...")

    relatorio = relatorio_para_tabela(
        ".", caminhoCSV=f"{AGORA.format('DD-MM-YYYY')}.csv"
    )

    relatorioFile = os.path.abspath(f"ES_{AGORA.format('DD-MM')}.csv")

    os.remove(fileOriginalPath)
    print("Copiando resultado para o Desktop...")
    shutil.copy(relatorioFile, desktopPath)

    pyperclip.copy("https://coronavirus.es.gov.br/painel-covid-19-es")
    print(f"'{pyperclip.paste()}' copiado para a área de transferência.")

    addSpreadsheetURL = "https://brasil.io/admin/covid19/statespreadsheet/add/"

    webbrowser.open_new(addSpreadsheetURL)

    return relatorio
