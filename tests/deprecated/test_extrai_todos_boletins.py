import pytest
from bs4 import BeautifulSoup

from COVID19_ES_Py import ScraperBoletim

scraper = ScraperBoletim()


def test_success():
    URLstodosBoletins = scraper.extrai_todos_boletins()
    ultimoBoletim = scraper.carrega_ultimo_boletim()

    assert len(URLstodosBoletins) == ultimoBoletim.n
