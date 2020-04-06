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
           'casosSuspeitos': '0',
           'totalCasos': '1'
           })


def test_29_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-31o-boletim-da-covid-19"
    )

    assert(boletim.pesquisa_casos_municipio("Vitória") == {
        'casosConfirmados': '21',
        'casosDescartados': '133',
        'casosSuspeitos': '117',
        'totalCasos': '271'
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
           'casosSuspeitos': '0',
           'totalCasos': '1'
           })


def test_30_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-32o-boletim-da-covid-19"
    )

    assert(boletim.pesquisa_casos_municipio("Vitória") == {
        'casosConfirmados': '26',
        'casosDescartados': '139',
        'casosSuspeitos': '118',
        'totalCasos': '283'
    })
    assert(boletim.pesquisa_casos_municipio("  santa teresa ") == {
           'casosConfirmados': '1',
           'casosDescartados': '1',
           'casosSuspeitos': '0',
           'totalCasos': '2'
           })
    assert(boletim.pesquisa_casos_municipio(" SAO JOSE DO CALCADO") == {
           'casosConfirmados': '0',
           'casosDescartados': '0',
           'casosSuspeitos': '1',
           'totalCasos': '1'
           })


def test_31_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-33o-boletim-da-covid-19"
    )

    assert(boletim.pesquisa_casos_municipio("Vitória") == {
        'casosConfirmados': '28',
        'casosDescartados': '155',
        'casosSuspeitos': '121',
        'totalCasos': '304'
    })

    assert(boletim.pesquisa_casos_municipio("  santa teresa ") == {
           'casosConfirmados': '1',
           'casosDescartados': '1',
           'casosSuspeitos': '0',
           'totalCasos': '2'
           })
    assert(boletim.pesquisa_casos_municipio(" AFONSO CLAUDIO") == {
           'casosConfirmados': '0',
           'casosDescartados': '1',
           'casosSuspeitos': '3',
           'totalCasos': '4'
           })


def test_fail_24_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-26o-boletim-de-covid-19"
    )

    # Município não é do ES
    with pytest.raises(exceptions.BoletimError):
        boletim.pesquisa_casos_municipio("arapiraca")

    # Nome de município incompleto
    with pytest.raises(exceptions.BoletimError):
        boletim.pesquisa_casos_municipio("vi")

    # Município ainda não havia caso registrado
    with pytest.raises(exceptions.BoletimError):
        boletim.pesquisa_casos_municipio("Pedro Canário")
