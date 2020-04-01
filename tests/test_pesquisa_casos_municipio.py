import pytest
from COVID19_ES_Py import Boletim, exceptions


def test_27_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
    )

    assert(boletim.pesquisa_casos_municipio("Vitória") == {
        'casosConfirmados': '18',
        'casosDescartados': '96',
        'casosSuspeitos': '142',
        'totalCasos': '256'
    })

    assert(boletim.pesquisa_casos_municipio("  santa teresa ") == {
           'casosConfirmados': '1',
           'casosDescartados': '1',
           'casosSuspeitos': '0',
           'totalCasos': '2'
           })
    assert(boletim.pesquisa_casos_municipio("AFONSO CLAUDIO") == {
           'casosConfirmados': '0',
           'casosDescartados': '1',
           'casosSuspeitos': '00',
           'totalCasos': '1'
           })


def test_fail():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
    )
    with pytest.raises(exceptions.BoletimError):
        boletim.pesquisa_casos_municipio("arapiraca")
