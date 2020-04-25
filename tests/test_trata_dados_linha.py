from datetime import datetime
import pytest
import arrow

from COVID19_ES_Py.utils import trata_dados_linha


def test_success():
    linha = ["27/04/2020", "Confirmados", "-", "Laboratorial", "Em Aberto", "SERRA", "PARQUE DAS GAIVOTAS", "60 a 69 anos", "M",
             "Branca", "Analfabeto", "Não", "Sim", "Não", "Não", "Não", "Não", "Não", "Não", "Sim", "Não", "Sim", "Sim", "Não", "-", "-", "-"]

    linhaTratada = [arrow.get(linha[0], "DD/MM/YYYY"), "Confirmados", None, "Laboratorial", "Em Aberto", "SERRA", "PARQUE DAS GAIVOTAS", "60 a 69 anos",
                    "M", "Branca", "Analfabeto", False, True, False, False, False, False, False, False, True, False, True, True, False, None, None, None]

    assert(trata_dados_linha(linha) == linhaTratada)

    linha = ["25/04/2020", "Confirmados", "Óbito pelo COVID-19", "Laboratorial", "Encerrado", "PRESIDENTE KENNEDY", "FAZENDA CAETES", "60 a 69 anos",
             "F", "Preta", "Ignorado", "Sim", "Sim", "Não", "Não", "Não", "Não", "Não", "Não", "Sim", "Não", "Sim", "Não", "Não", "Sim", "Não", "Não"]

    linhaTratada = [arrow.get(linha[0], "DD/MM/YYYY"), "Confirmados", "Óbito pelo COVID-19", "Laboratorial", "Encerrado", "PRESIDENTE KENNEDY", "FAZENDA CAETES",
                    "60 a 69 anos", "F", "Preta", None, True, True, False, False, False, False, False, False, True, False, True, False, False, True, False, False]

    assert(trata_dados_linha(linha) == linhaTratada)

    linha = [datetime.strptime("25/04/2020", "%d/%m/%Y"), "Confirmados", "Óbito pelo COVID-19", "Laboratorial", "Encerrado", "PRESIDENTE KENNEDY", "FAZENDA CAETES", "60 a 69 anos",
             "F", "Preta", "Ignorado", "Sim", "Sim", "Não", "Não", "Não", "Não", "Não", "Não", "Sim", "Não", "Sim", "Não", "Não", "Sim", "Não", "Não"]

    linhaTratada = [arrow.get(linha[0]), "Confirmados", "Óbito pelo COVID-19", "Laboratorial", "Encerrado", "PRESIDENTE KENNEDY", "FAZENDA CAETES",
                    "60 a 69 anos", "F", "Preta", None, True, True, False, False, False, False, False, False, True, False, True, False, False, True, False, False]

    assert(trata_dados_linha(linha) == linhaTratada)


def test_fail():
    with pytest.raises(IndexError):
        linha = []
        trata_dados_linha(linha)

    with pytest.raises(IndexError):
        linha = ["25/04/2020"]
        trata_dados_linha(linha)

    with pytest.raises(TypeError):
        linha = [
            "15/04/2020", "Confirmados", "Óbito pelo COVID-19", "Laboratorial", "Encerrado", "PRESIDENTE KENNEDY", "FAZENDA CAETES",
            "60 a 69 anos", "F", "Preta", None, True, True, False, False, False, False, False, False, True, False, True, False, False, True, False, False
        ]
        trata_dados_linha(linha)

    with pytest.raises(TypeError):
        linha = [
            datetime.strptime(
                "15/04/2020", "%d/%m/%Y"), "Confirmados", "Óbito pelo COVID-19", "Laboratorial", "Encerrado", "PRESIDENTE KENNEDY", "FAZENDA CAETES",
            "60 a 69 anos", "F", "Preta", None, True, True, False, False, False, False, False, False, True, False, True, False, False, True, False, False
        ]
        trata_dados_linha(linha)
