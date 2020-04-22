from COVID19_ES_Py import Boletim


def test_25_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19"
    )

    municipiosComCasos = {
        'Cachoeiro de Itapemirim': '1', 'Cariacica': '1', 'Linhares':
        '3', 'Santa Teresa': '1', 'Serra': '1', 'Vila Velha': '17', 'Vitória': '15'
    }

    dicionarioFiltrado = boletim.filtra_municipios_com_casos_confirmados()
    dicionarioFiltrado = {
        municipio: casos['casosConfirmados'] for (municipio, casos) in dicionarioFiltrado.items()
    }

    assert dicionarioFiltrado == municipiosComCasos


def test_27_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-29o-boletim-de-covid-19"
    )

    municipiosComCasos = {
        'Cachoeiro de Itapemirim': '1', 'Cariacica': '1', 'Castelo': '1', 'Linhares': '4',
        'Santa Teresa': '1', 'São Roque do Canaã': '1', 'Serra': '5', 'Vila Velha': '21', 'Vitória': '18'
    }
    
    dicionarioFiltrado = boletim.filtra_municipios_com_casos_confirmados()
    dicionarioFiltrado = {
        municipio: casos['casosConfirmados'] for (municipio, casos) in dicionarioFiltrado.items()
    }

    assert dicionarioFiltrado == municipiosComCasos


def test_31_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-33o-boletim-da-covid-19"
    )

    municipiosComCasos = {
        'Alto Rio Novo': '1', 'Cachoeiro de Itapemirim': '1', 'Cariacica': '5', 'Castelo': '1', 'Guarapari': '2', 'Itapemirim': '1',
        'Linhares': '4', 'Santa Teresa': '1', 'São Mateus': '1', 'São Roque do Canaã': '1', 'Serra': '14', 'Viana': '1', 'Vila Velha': '35', 'Vitória': '28'
    }
    
    dicionarioFiltrado = boletim.filtra_municipios_com_casos_confirmados()
    dicionarioFiltrado = {
        municipio: casos['casosConfirmados'] for (municipio, casos) in dicionarioFiltrado.items()
    }

    assert dicionarioFiltrado == municipiosComCasos


def test_01_04():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-34o-boletim-da-covid-19"
    )

    municipiosComCasos = {
        'Afonso Cláudio': '1', 'Aracruz': '1', 'Cachoeiro de Itapemirim': '1', 'Cariacica': '7', 'Castelo': '2', 'Guarapari': '2', 'Itapemirim': '1', 'Linhares': '7', 'Santa Teresa': '1', 'São Mateus': '3', 'São Roque do Canaã': '1', 'Serra': '22', 'Viana': '1', 'Vila Velha': '36', 'Vitória': '34'
    }
    
    dicionarioFiltrado = boletim.filtra_municipios_com_casos_confirmados()
    dicionarioFiltrado = {
        municipio: casos['casosConfirmados'] for (municipio, casos) in dicionarioFiltrado.items()
    }

    assert dicionarioFiltrado == municipiosComCasos


def test_02_04():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-35o-boletim-da-covid-19"
    )

    municipiosComCasos = {
        'Afonso Cláudio': '1', 'Aracruz': '1', 'Cachoeiro de Itapemirim': '1', 'Cariacica': '11', 'Castelo': '2', 'Fundão': '1', 'Guarapari': '3', 'Itapemirim': '1', 'Linhares': '7', 'Santa Teresa': '1', 'São Mateus': '3', 'São Roque do Canaã': '1', 'Serra':
        '23', 'Sooretama': '2', 'Viana': '1', 'Vila Velha': '44', 'Vitória': '36'
    }
    
    dicionarioFiltrado = boletim.filtra_municipios_com_casos_confirmados()
    dicionarioFiltrado = {
        municipio: casos['casosConfirmados'] for (municipio, casos) in dicionarioFiltrado.items()
    }

    assert dicionarioFiltrado == municipiosComCasos


def test_05_04():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-38o-boletim-da-covid-19"
    )

    municipiosComCasos = {
        'Afonso Cláudio': {"casosConfirmados": '1', "casosDescartados": "3", "casosSuspeitos": "3", "totalCasos": "7", "obitos": "0"},
        'Aracruz': {'casosConfirmados': '4', 'casosDescartados': '29', 'casosSuspeitos': '6', 'totalCasos': '39', 'obitos': '0'},
        'Cachoeiro de Itapemirim': {'casosConfirmados': '1', 'casosDescartados': '35', 'casosSuspeitos': '7', 'totalCasos': '43', 'obitos': '0'},
        'Cariacica': {'casosConfirmados': '16', 'casosDescartados': '119', 'casosSuspeitos': '37', 'totalCasos': '172', 'obitos': '0'},
        'Castelo': {'casosConfirmados': '2', 'casosDescartados': '9', 'casosSuspeitos': '1', 'totalCasos': '12', 'obitos': '0'},
        'Colatina': {'casosConfirmados': '2', 'casosDescartados': '21', 'casosSuspeitos': '5', 'totalCasos': '28', 'obitos': '0'},
        'Fundão': {'casosConfirmados': '1', 'casosDescartados': '3', 'casosSuspeitos': '5', 'totalCasos': '9', 'obitos': '0'},
        'Guarapari': {'casosConfirmados': '3', 'casosDescartados': '25', 'casosSuspeitos': '2', 'totalCasos': '30', 'obitos': '0'},
        'Itapemirim': {'casosConfirmados': '1', 'casosDescartados': '5', 'casosSuspeitos': '0', 'totalCasos': '6', 'obitos': '0'},
        'Linhares': {'casosConfirmados': '8', 'casosDescartados': '89', 'casosSuspeitos': '91', 'totalCasos': '188', 'obitos': '0'},
        'Santa Teresa': {'casosConfirmados': '1', 'casosDescartados': '2', 'casosSuspeitos': '3', 'totalCasos': '6', 'obitos': '0'},
        'São Mateus': {'casosConfirmados': '4', 'casosDescartados': '24', 'casosSuspeitos': '6', 'totalCasos': '34', 'obitos': '1'},
        'São Roque do Canaã': {'casosConfirmados': '1', 'casosDescartados': '3', 'casosSuspeitos': '0', 'totalCasos': '4', 'obitos': '0'},
        'Serra': {'casosConfirmados': '31', 'casosDescartados': '176', 'casosSuspeitos': '276', 'totalCasos': '483', 'obitos': '1'},
        'Sooretama': {'casosConfirmados': '2', 'casosDescartados': '5', 'casosSuspeitos': '4', 'totalCasos': '11', 'obitos': '0'},
        'Viana': {'casosConfirmados': '1', 'casosDescartados': '17', 'casosSuspeitos': '34', 'totalCasos': '52', 'obitos': '0'},
        'Vila Velha': {'casosConfirmados': '53', 'casosDescartados': '341', 'casosSuspeitos': '161', 'totalCasos': '555', 'obitos': '2'},
        'Vitória': {'casosConfirmados': '62', 'casosDescartados': '252', 'casosSuspeitos': '58', 'totalCasos': '372', 'obitos': '2'}
    }

    assert boletim.filtra_municipios_com_casos_confirmados(
    ) == municipiosComCasos
