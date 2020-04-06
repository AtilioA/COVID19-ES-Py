"""Scraper de boletins de casos de COVID-19 no Espírito Santo.
    >>> import COVID19_ES_Py
    >>> scraper = COVID19_ES_Py.ScraperBoletim()
    >>> boletim = scraper.carrega_ultimo_boletim()

Veja https://github.com/AtilioA/COVID19-ES-Py ou https://covid19-es-py.readthedocs.io/ para mais informações.
"""

# flake8: noqa
from .boletim import (ScraperBoletim, Boletim)

__all__ = [
    'ScraperBoletim',
    'Boletim',
]

__version__ = "1.2.0"
