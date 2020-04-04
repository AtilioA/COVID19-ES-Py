from bs4 import BeautifulSoup

from COVID19_ES_Py import ScraperBoletim

scraper = ScraperBoletim()


def test_30_03():
    with open("tests/html/noticias_30_03.html", "r", encoding="utf-8") as htmlFile:
        html = BeautifulSoup(htmlFile, "html.parser")
        boletinsPagina = scraper.extrai_boletins_pagina(html=html)
        assert(boletinsPagina == [
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-31o-boletim-da-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-30o-boletim-da-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-28o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-26o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-25o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-24o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-23o-boletim-de-covid-19'
        ])


def test_31_03():
    with open("tests/html/noticias_31_03.html", "r", encoding="utf-8") as htmlFile:
        html = BeautifulSoup(htmlFile, "html.parser")
        boletinsPagina = scraper.extrai_boletins_pagina(html=html)
        assert(boletinsPagina == [
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-33o-boletim-da-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-31o-boletim-da-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-30o-boletim-da-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-28o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-26o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-25o-boletim-de-covid-19',
            'https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-24o-boletim-de-covid-19',
        ])
