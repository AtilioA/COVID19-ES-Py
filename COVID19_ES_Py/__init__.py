"""Leitor de relatórios de casos de COVID-19 no Espírito Santo.
    >>> import COVID19_ES_Py
    >>> leitor = COVID19_ES_Py.LeitorRelatorio()
    >>> relatorio = leitor.carrega_ultimo_relatorio()

Veja https://github.com/AtilioA/COVID19-ES-Py ou https://covid19-es-py.readthedocs.io/ para mais informações.
"""

# flake8: noqa
from .boletim import (ScraperBoletim, Boletim)  # Descontinuado
from .relatorio import (LeitorRelatorio, Relatorio)

__all__ = [
    'ScraperBoletim',
    'Boletim',
    'Relatorio',
]

__version__ = "2.0.0"
