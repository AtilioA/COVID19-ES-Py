from COVID19_ES_Py import Boletim


def test_25_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19"
    )

    municipiosComCasos = {
        'Cachoeiro de Itapemirim': '1', 'Cariacica': '1', 'Linhares':
        '3', 'Santa Teresa': '1', 'Serra': '1', 'Vila Velha': '17', 'Vitória': '15'
    }
    assert boletim.filtra_municipios_com_casos() == municipiosComCasos


def test_27_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
    )

    municipiosComCasos = {
        'Cachoeiro de Itapemirim': '1', 'Cariacica': '1', 'Castelo': '1', 'Linhares': '4',
        'Santa Teresa': '1', 'São Roque do Canaã': '1', 'Serra': '5', 'Vila Velha': '21', 'Vitória': '18'
    }
    assert boletim.filtra_municipios_com_casos() == municipiosComCasos


def test_31_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-33o-boletim-da-covid-19"
    )

    municipiosComCasos = {
        'Alto Rio Novo': '1', 'Cachoeiro de Itapemirim': '1', 'Cariacica': '5', 'Castelo': '1', 'Guarapari': '2', 'Itapemirim': '1',
        'Linhares': '4', 'Santa Teresa': '1', 'São Mateus': '1', 'São Roque do Canaã': '1', 'Serra': '14', 'Viana': '1', 'Vila Velha': '35', 'Vitória': '28'
    }
    assert boletim.filtra_municipios_com_casos() == municipiosComCasos


def test_01_04():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-34o-boletim-da-covid-19"
    )

    municipiosComCasos = {
        'Afonso Cláudio': '1', 'Aracruz': '1', 'Cachoeiro de Itapemirim': '1', 'Cariacica': '7', 'Castelo': '2', 'Guarapari': '2', 'Itapemirim': '1', 'Linhares': '7', 'Santa Teresa': '1', 'São Mateus': '3', 'São Roque do Canaã': '1', 'Serra': '22', 'Viana': '1', 'Vila Velha': '36', 'Vitória': '34'
    }
    assert boletim.filtra_municipios_com_casos() == municipiosComCasos


def test_02_04():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-35o-boletim-da-covid-19"
    )

    municipiosComCasos = {
        'Afonso Cláudio': '1', 'Aracruz': '1', 'Cachoeiro de Itapemirim': '1', 'Cariacica': '11', 'Castelo': '2', 'Fundão': '1', 'Guarapari': '3', 'Itapemirim': '1', 'Linhares': '7', 'Santa Teresa': '1', 'São Mateus': '3', 'São Roque do Canaã': '1', 'Serra':
        '23', 'Sooretama': '2', 'Viana': '1', 'Vila Velha': '44', 'Vitória': '36'
    }
    assert boletim.filtra_municipios_com_casos() == municipiosComCasos
