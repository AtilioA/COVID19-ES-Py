from COVID19_ES_Py import Boletim


def test_25_03():
    boletim = Boletim(
        "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-27o-boletim-de-covid-19"
    )

    assert boletim.conta_municipios_com_casos() == 62


# def test_31_03():
#     boletim = Boletim(
#         "https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-33o-boletim-da-covid-19"
#     )

#     assert boletim.conta_municipios_com_casos() == 62
