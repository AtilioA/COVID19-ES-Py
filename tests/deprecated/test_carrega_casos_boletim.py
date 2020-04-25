import pytest
from requests.exceptions import MissingSchema

from COVID19_ES_Py import Boletim, exceptions


# - TABELAS TIPO 1 (19/03/2020)
def test_boletim_21():
    boletim_21 = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-21o-boletim-de-covid-19")

    assert (
        boletim_21.casos["Vitória"]["casosConfirmados"]
        == "5"
    )

    assert (
        boletim_21.casos["Vila Velha"]["casosConfirmados"]
        == "7"
    )

    assert (
        boletim_21.casos["Linhares"]["casosConfirmados"]
        == "1"
    )

    assert (
        boletim_21.casos["Guarapari"]["casosConfirmados"]
        == "0"
    )


def test_boletim_22():
    boletim_22 = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-22o-boletim-de-covid-19")

    assert (
        boletim_22.casos["Vitória"]["casosConfirmados"]
        == "6"
    )

    assert (
        boletim_22.casos["Vila Velha"]["casosConfirmados"]
        == "7"
    )

    assert (
        boletim_22.casos["Linhares"]["casosConfirmados"]
        == "1"
    )

    assert (
        boletim_22.casos["Guarapari"]["casosConfirmados"]
        == "0"
    )


def test_boletim_23():
    boletim_23 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-23o-boletim-de-covid-19")

    assert (
        boletim_23.casos["Vitória"]["casosConfirmados"]
        == "11"
    )

    assert (
        boletim_23.casos["Vila Velha"]["casosConfirmados"]
        == "11"
    )

    assert (
        boletim_23.casos["Linhares"]["casosConfirmados"]
        == "2"
    )

    assert (
        boletim_23.casos["Guarapari"]["casosConfirmados"]
        == "0"
    )


# TABELA TIPO 2 (22/03/2020)
def test_boletim_24():
    boletim_24 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-24o-boletim-de-covid-19")

    assert (
        boletim_24.casos["Vitoria"]["casosConfirmados"]
        == "11"
    )

    assert (
        boletim_24.casos["Vila Velha"]["casosConfirmados"]
        == "11"
    )

    assert (
        boletim_24.casos["Linhares"]["casosConfirmados"]
        == "2"
    )

    assert (
        boletim_24.casos["Atílio Vivacqua"]["casosConfirmados"]
        == "0"
    )


# TABELA TIPO 3 (23/03/2020)
def test_boletim_25():
    boletim_25 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-25o-boletim-de-covid-19")

    assert (
        boletim_25.casos["Vitória"]["casosConfirmados"]
        == "13"
    )

    assert (
        boletim_25.casos["Vila Velha"]["casosConfirmados"]
        == "12"
    )

    assert (
        boletim_25.casos["Linhares"]["casosConfirmados"]
        == "2"
    )

    assert (
        boletim_25.casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_26():
    boletim_26 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-26o-boletim-de-covid-19")

    assert (
        boletim_26.casos["Vitória"]["casosConfirmados"]
        == "15"
    )

    assert (
        boletim_26.casos["Vila Velha"]["casosConfirmados"]
        == "17"
    )

    assert (
        boletim_26.casos["Linhares"]["casosConfirmados"]
        == "3"
    )

    assert (
        boletim_26.casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_27():
    boletim_27 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19")

    assert (
        boletim_27.casos["Vitória"]["casosConfirmados"]
        == "15"
    )

    assert (
        boletim_27.casos["Vila Velha"]["casosConfirmados"]
        == "17"
    )

    assert (
        boletim_27.casos["Linhares"]["casosConfirmados"]
        == "3"
    )

    assert (
        boletim_27.casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_28():
    boletim_28 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-28o-boletim-de-covid-19")

    assert (
        boletim_28.casos["Vitória"]["casosConfirmados"]
        == "17"
    )

    assert (
        boletim_28.casos["Vila Velha"]["casosConfirmados"]
        == "20"
    )

    assert (
        boletim_28.casos["Linhares"]["casosConfirmados"]
        == "3"
    )

    assert (
        boletim_28.casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_29():
    boletim_29 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19")

    assert (
        boletim_29.casos["Vitória"]["casosConfirmados"]
        == "18"
    )

    assert (
        boletim_29.casos["Vila Velha"]["casosConfirmados"]
        == "21"
    )

    assert (
        boletim_29.casos["Linhares"]["casosConfirmados"]
        == "4"
    )

    assert (
        boletim_29.casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_30():
    boletim_30 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-30o-boletim-da-covid-19")

    assert (
        boletim_30.casos["Vitória"]["casosConfirmados"]
        == "20"
    )

    assert (
        boletim_30.casos["Vila Velha"]["casosConfirmados"]
        == "24"
    )

    assert (
        boletim_30.casos["Linhares"]["casosConfirmados"]
        == "4"
    )

    assert (
        boletim_30.casos["Atílio Vivacqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_31():
    boletim_31 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-31o-boletim-da-covid-19")

    assert (
        boletim_31.casos["Vitória"]["casosConfirmados"]
        == "21"
    )

    assert (
        boletim_31.casos["Vila Velha"]["casosConfirmados"]
        == "28"
    )

    assert (
        boletim_31.casos["Linhares"]["casosConfirmados"]
        == "4"
    )

    assert (
        boletim_31.casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_32():
    boletim_32 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19")

    assert (
        boletim_32.casos["Vitória"]["casosConfirmados"]
        == "26"
    )

    assert (
        boletim_32.casos["Vila Velha"]["casosConfirmados"]
        == "31"
    )

    assert (
        boletim_32.casos["Linhares"]["casosConfirmados"]
        == "4"
    )

    assert (
        boletim_32.casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


# TABELA TIPO 4 (04/04/2020)
def test_boletim_37():
    boletim_37 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-37o-boletim-da-covid-19")

    assert (
        boletim_37.casos["Vitória"]["casosConfirmados"]
        == "43"
    )

    assert (
        boletim_37.casos["Vitória"]["obitos"]
        == "2"
    )

    assert (
        boletim_37.casos["Vila Velha"]["casosConfirmados"]
        == "50"
    )

    assert (
        boletim_37.casos["Vila Velha"]["obitos"]
        == "2"
    )

    assert (
        boletim_37.casos["Linhares"]["casosConfirmados"]
        == "8"
    )

    assert (
        boletim_37.casos["Atílio Vivacqua"]["casosConfirmados"]
        == "0"
    )

    assert (
        boletim_37.casos["São Mateus"]["obitos"]
        == "1"
    )


def test_boletim_38():
    boletim_38 = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-38o-boletim-da-covid-19")

    assert (
        boletim_38.casos["Vitória"]["casosConfirmados"]
        == "62"
    )

    assert (
        boletim_38.casos["Vitória"]["obitos"]
        == "2"
    )

    assert (
        boletim_38.casos["Vila Velha"]["casosConfirmados"]
        == "53"
    )

    assert (
        boletim_38.casos["Vila Velha"]["obitos"]
        == "2"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-38o-boletim-da-covid-19"
        ).casos["Linhares"]["casosConfirmados"]
        == "8"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-38o-boletim-da-covid-19"
        ).casos["Atílio Vivacqua"]["casosConfirmados"]
        == "0"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-38o-boletim-da-covid-19"
        ).casos["São Mateus"]["obitos"]
        == "1"
    )


def test_fail():
    with pytest.raises(TypeError):
        Boletim(37503003)

    with pytest.raises(MissingSchema):
        Boletim("")

    with pytest.raises(TypeError):
        Boletim(None)

    with pytest.raises(TypeError):
        Boletim(False)

    with pytest.raises(TypeError):
        Boletim(True)

    with pytest.raises(AttributeError):
        Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/")

    with pytest.raises(AttributeError):
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-de-covid-19"
        )

    with pytest.raises(AttributeError):
        Boletim("https://www.google.com.br")

    with pytest.raises(exceptions.BoletimError):
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-5o-boletim-de-covid-19")
