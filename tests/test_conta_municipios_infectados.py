from COVID19_ES_Py import Boletim


def test_25_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19"
    )

    assert boletim.conta_municipios_infectados() == 7


def test_27_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
    )

    assert boletim.conta_municipios_infectados() == 9


def test_31_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-33o-boletim-da-covid-19"
    )

    assert boletim.conta_municipios_infectados() == 14


def test_01_04():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-34o-boletim-da-covid-19"
    )

    assert boletim.conta_municipios_infectados() == 15


def test_02_04():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-35o-boletim-da-covid-19"
    )

    assert boletim.conta_municipios_infectados() == 17
