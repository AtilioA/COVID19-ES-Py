import pytest
from requests.exceptions import MissingSchema

from COVID19_ES_Py import Boletim


# - TABELAS TIPO 1 | TODO: tabelas ainda não suportadas
# def test_boletim_21():
#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-21o-boletim-de-covid-19"
#         ).casos["Vitória"]["casosConfirmados"]
#         == "5"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-21o-boletim-de-covid-19"
#         ).casos["Vila Velha"]["casosConfirmados"]
#         == "7"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-21o-boletim-de-covid-19"
#         ).casos["Linhares"]["casosConfirmados"]
#         == "1"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-21o-boletim-de-covid-19"
#         ).casos["Guarapari"]["casosConfirmados"]
#         == "0"
#     )


# def test_boletim_22():
#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-22o-boletim-de-covid-19"
#         ).casos["Vitória"]["casosConfirmados"]
#         == "6"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-22o-boletim-de-covid-19"
#         ).casos["Vila Velha"]["casosConfirmados"]
#         == "7"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-22o-boletim-de-covid-19"
#         ).casos["Linhares"]["casosConfirmados"]
#         == "1"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-22o-boletim-de-covid-19"
#         ).casos["Guarapari"]["casosConfirmados"]
#         == "0"
#     )


# def test_boletim_23():
#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-23o-boletim-de-covid-19"
#         ).casos["Vitória"]["casosConfirmados"]
#         == "11"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-23o-boletim-de-covid-19"
#         ).casos["Vila Velha"]["casosConfirmados"]
#         == "11"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-23o-boletim-de-covid-19"
#         ).casos["Linhares"]["casosConfirmados"]
#         == "2"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-23o-boletim-de-covid-19"
#         ).casos["Guarapari"]["casosConfirmados"]
#         == "0"
#     )


# def test_boletim_24():
#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-24o-boletim-de-covid-19"
#         ).casos["Vitória"]["casosConfirmados"]
#         == "11"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-24o-boletim-de-covid-19"
#         ).casos["Vila Velha"]["casosConfirmados"]
#         == "11"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-24o-boletim-de-covid-19"
#         ).casos["Linhares"]["casosConfirmados"]
#         == "2"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-24o-boletim-de-covid-19"
#         ).casos["Atílio Vivácqua"]["casosConfirmados"]
#         == "0"
#     )


# # TABELA TIPO 2 | TODO: tabela ainda não suportada
# def test_boletim_25():
#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-25o-boletim-de-covid-19"
#         ).casos["Vitória"]["casosConfirmados"]
#         == "13"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-25o-boletim-de-covid-19"
#         ).casos["Vila Velha"]["casosConfirmados"]
#         == "12"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-25o-boletim-de-covid-19"
#         ).casos["Linhares"]["casosConfirmados"]
#         == "2"
#     )

#     assert (
#         Boletim(
#             "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-25o-boletim-de-covid-19"
#         ).casos["Atílio Vivácqua"]["casosConfirmados"]
#         == "0"
#     )


# TABELAS TIPO 3
def test_boletim_26():
    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-26o-boletim-de-covid-19"
        ).casos["Vitória"]["casosConfirmados"]
        == "15"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-26o-boletim-de-covid-19"
        ).casos["Vila Velha"]["casosConfirmados"]
        == "17"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-26o-boletim-de-covid-19"
        ).casos["Linhares"]["casosConfirmados"]
        == "3"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-26o-boletim-de-covid-19"
        ).casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_27():
    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19"
        ).casos["Vitória"]["casosConfirmados"]
        == "15"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19"
        ).casos["Vila Velha"]["casosConfirmados"]
        == "17"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19"
        ).casos["Linhares"]["casosConfirmados"]
        == "3"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19"
        ).casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_28():
    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-28o-boletim-de-covid-19"
        ).casos["Vitória"]["casosConfirmados"]
        == "17"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-28o-boletim-de-covid-19"
        ).casos["Vila Velha"]["casosConfirmados"]
        == "20"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-28o-boletim-de-covid-19"
        ).casos["Linhares"]["casosConfirmados"]
        == "3"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-28o-boletim-de-covid-19"
        ).casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_29():
    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
        ).casos["Vitória"]["casosConfirmados"]
        == "18"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
        ).casos["Vila Velha"]["casosConfirmados"]
        == "21"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
        ).casos["Linhares"]["casosConfirmados"]
        == "4"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
        ).casos["Atílio Vivácqua"]["casosConfirmados"]
        == "00"
    )


def test_boletim_30():
    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-30o-boletim-da-covid-19"
        ).casos["Vitória"]["casosConfirmados"]
        == "20"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-30o-boletim-da-covid-19"
        ).casos["Vila Velha"]["casosConfirmados"]
        == "24"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-30o-boletim-da-covid-19"
        ).casos["Linhares"]["casosConfirmados"]
        == "4"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-30o-boletim-da-covid-19"
        ).casos["Atílio Vivacqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_31():
    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-31o-boletim-da-covid-19"
        ).casos["Vitória"]["casosConfirmados"]
        == "21"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-31o-boletim-da-covid-19"
        ).casos["Vila Velha"]["casosConfirmados"]
        == "28"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-31o-boletim-da-covid-19"
        ).casos["Linhares"]["casosConfirmados"]
        == "4"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-31o-boletim-da-covid-19"
        ).casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
    )


def test_boletim_32():
    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19"
        ).casos["Vitória"]["casosConfirmados"]
        == "26"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19"
        ).casos["Vila Velha"]["casosConfirmados"]
        == "31"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19"
        ).casos["Linhares"]["casosConfirmados"]
        == "4"
    )

    assert (
        Boletim(
            "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19"
        ).casos["Atílio Vivácqua"]["casosConfirmados"]
        == "0"
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
