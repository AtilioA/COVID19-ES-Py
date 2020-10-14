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


def relatorio_para_csv(path, data=None, caminhoCSV=None):
    if data and caminhoCSV:
        leitor = LeitorRelatorio(caminhoCSV)
        relatorio = leitor.filtra_casos_ate_dia(data)
        dataRelatorio = arrow.get(data, "DD/MM/YYYY").format("DD_MM")
    elif data:
        dataRelatorio = NOW.format("DD_MM")
        relatorio = leitor.filtra_casos_ate_dia(dataRelatorio)

    if caminhoCSV:
        print(f"Lendo arquivo {os.path.basename(caminhoCSV)}")
        leitor = LeitorRelatorio(caminhoCSV)
        relatorio = leitor.relatorio
        arquivoCriado = Path(f"{path}/ES_{os.path.basename(caminhoCSV)[:5]}.csv")
    else:
        leitor = LeitorRelatorio()
        relatorio = leitor.carrega_ultimo_relatorio()
        arquivoCriado = Path(f"{path}/ES_{dataRelatorio}.csv")

    relatorio.popula_relatorio()

    totalGeral = relatorio.totalGeral
    print(f"Municípios infectados: {relatorio.nMunicipiosInfectados}")
    print(f"Total geral: {totalGeral}")

    with open(arquivoCriado, "w+", encoding="utf-8") as f:
        f.write(f"municipio|confirmados|mortes\n")
        f.write(
            f"TOTAL NO ESTADO|{totalGeral['casosConfirmados']}|{totalGeral['obitos']}\n"
        )
        f.write(
            f"Importados/Indefinidos|{relatorio.importadosOuIndefinidos['casosConfirmados']}|{relatorio.importadosOuIndefinidos['obitos']}\n"
        )
        for i, (municipio, objMunicipio) in enumerate(
            sorted(relatorio.casosMunicipios.items())
        ):
            casosConfirmados = objMunicipio.casosConfirmados
            obitos = objMunicipio.obitos
            f.write(f"{MUNICIPIOS_SEM_TRATAMENTO[i]}|{casosConfirmados}|{obitos}\n")
        print(f"Tabela do relatório salva em {arquivoCriado}.")

    return relatorio


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
