import pytest
import arrow
from COVID19_ES_Py import ScraperBoletim, Boletim


scraper = ScraperBoletim()


def test_27_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
    )

    boletimPesquisa = scraper.pesquisa_boletim_data("27/03/2020")
    assert(boletimPesquisa.n == boletim.n)

    boletimPesquisa = scraper.pesquisa_boletim_data("27-03-2020")
    assert(boletimPesquisa.n == boletim.n)

    boletimPesquisa = scraper.pesquisa_boletim_data("27.03.2020")
    assert(boletimPesquisa.n == boletim.n)

    boletimPesquisa = scraper.pesquisa_boletim_data("27_03_2020")
    assert(boletimPesquisa.n == boletim.n)

    boletimPesquisa = scraper.pesquisa_boletim_data("27032020")
    assert(boletimPesquisa.n == boletim.n)


def test_28_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-30o-boletim-da-covid-19"
    )

    boletimPesquisa = scraper.pesquisa_boletim_data("28-03-2020")
    assert(boletimPesquisa.n == boletim.n)


def test_29_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-31o-boletim-da-covid-19"
    )

    boletimPesquisa = scraper.pesquisa_boletim_data("29.03.2020")
    assert(boletimPesquisa.n == boletim.n)


def test_30_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19"
    )

    boletimPesquisa = scraper.pesquisa_boletim_data("30_03_2020")
    assert(boletimPesquisa.n == boletim.n)


def test_31_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-33o-boletim-da-covid-19"
    )

    boletimPesquisa = scraper.pesquisa_boletim_data("31_03_2020")
    assert(boletimPesquisa.n == boletim.n)


def test_01_04():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-34o-boletim-da-covid-19"
    )

    boletimPesquisa = scraper.pesquisa_boletim_data("01_04_2020")
    assert(boletimPesquisa.n == boletim.n)


def test_too_soon():
    boletimPesquisa = scraper.pesquisa_boletim_data("01_03_2020")
    assert(boletimPesquisa is None)


def test_too_late():
    boletimPesquisa = scraper.pesquisa_boletim_data("01_03_2077")
    assert(boletimPesquisa is None)


def test_fail():
    with pytest.raises(TypeError):
        scraper.pesquisa_boletim_data(None)
    with pytest.raises(TypeError):
        scraper.pesquisa_boletim_data(True)
    with pytest.raises(TypeError):
        scraper.pesquisa_boletim_data(False)
    with pytest.raises(TypeError):
        scraper.pesquisa_boletim_data(None)
    with pytest.raises(TypeError):
        scraper.pesquisa_boletim_data(10)

    with pytest.raises(arrow.parser.ParserError):
        scraper.pesquisa_boletim_data("10")
    with pytest.raises(arrow.parser.ParserError):
        scraper.pesquisa_boletim_data("20/03")
    with pytest.raises(arrow.parser.ParserError):
        scraper.pesquisa_boletim_data("03/20")
