import pytest
from bs4 import BeautifulSoup

from COVID19_ES_Py import ScraperBoletim

scraper = ScraperBoletim()


def test_30_03():
    with open("tests/html/noticias_30_03.html", "r", encoding="utf-8") as htmlFile:
        html = BeautifulSoup(htmlFile, "html.parser")
        URLUltimoBoletim = scraper.url_ultimo_boletim(html)
        assert(URLUltimoBoletim ==
               "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19")


def test_31_03():
    with open("tests/html/noticias_31_03.html", "r", encoding="utf-8") as htmlFile:
        html = BeautifulSoup(htmlFile, "html.parser")
        URLUltimoBoletim = scraper.url_ultimo_boletim(html)
        assert(URLUltimoBoletim ==
               "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-33o-boletim-da-covid-19")


def test_fail():
    with pytest.raises(TypeError):
        with open("tests/html/noticias_31_03_fail.html", "r", encoding="utf-8") as htmlFile:
            html = BeautifulSoup(htmlFile, "html.parser")
            URLUltimoBoletim = scraper.url_ultimo_boletim(html)
            print(URLUltimoBoletim)
