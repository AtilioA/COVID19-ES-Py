#!/usr/bin/python3.8

import os
from pathlib import Path
import argparse
import shutil
import webbrowser
import wget

import arrow
import pyperclip

from relatorio_para_csv import relatorio_para_tabela

AGORA = arrow.now("America/Sao_Paulo")
MICRODADOS_URL = "https://bi.static.es.gov.br/covid19/MICRODADOS.csv"
MICRODADOS_PATH = "/home/atilioa/Downloads"
MICRODADOS_FILENAME = f"MICRODADOS_ES_{AGORA.format('DD_MM_YYYY')}"
OUTPUT_PATH = "output/"


# Parse cli arguments
parser = argparse.ArgumentParser(description="Process args.")


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


parser.add_argument(
    "--download",
    "-d",
    type=str2bool,
    nargs="?",
    const=True,
    default=True,
    help="download covid-19 data.",
)


def automatiza_subida(download=False):

    print(
        f"""Criando arquivo {Path(f"{MICRODADOS_FILENAME}.csv")} (cópia dos microdados)...\n"""
    )

    downloadFilePath = f"{MICRODADOS_PATH}/{MICRODADOS_FILENAME}.csv"
    if download:
        print(f"Baixando {MICRODADOS_FILENAME}.csv...")
        wget.download(
            MICRODADOS_URL, downloadFilePath,
        )

    outputPath = os.path.abspath(OUTPUT_PATH)

    filename = str(Path(f"{MICRODADOS_FILENAME}.csv"))
    newFilenameAndPath = os.path.join("MICRODADOS/", filename)

    try:
        shutil.copy(downloadFilePath, newFilenameAndPath)
    except FileNotFoundError:
        try:
            shutil.copy(downloadFilePath, f"{MICRODADOS_PATH}/MICRODADOS.csv")
        except FileNotFoundError:
            print(f"Baixando {MICRODADOS_FILENAME}.csv...")
            wget.download(
                MICRODADOS_URL, MICRODADOS_PATH,
            )
            shutil.copy(downloadFilePath, newFilenameAndPath)

    print("Planilha da SESA copiada. Gerando relatório...")

    relatorio = relatorio_para_tabela(".", data=AGORA, caminhoCSV=newFilenameAndPath)

    relatorioFile = os.path.abspath(f"ES_{AGORA.format('DD_MM_YYYY')}.csv")

    os.remove(downloadFilePath)
    print("Copiando resultado para pasta de output...")
    shutil.copy(relatorioFile, outputPath)

    pyperclip.copy("https://coronavirus.es.gov.br/painel-covid-19-es")
    print(f"'{pyperclip.paste()}' copiado para a área de transferência.")

    addSpreadsheetURL = "https://brasil.io/admin/covid19/statespreadsheet/add/"

    webbrowser.open_new(addSpreadsheetURL)

    return relatorio


if __name__ == "__main__":
    args = parser.parse_args()
    shouldDownload = args.download

    ultimoRelatorio = automatiza_subida(download=shouldDownload)
