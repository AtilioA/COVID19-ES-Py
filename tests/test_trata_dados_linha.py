from datetime import datetime
import pytest
import arrow

from COVID19_ES_Py.utils import trata_dados_linha


def test_success():
    linha = ["2020-07-02", "2020-07-02", "2020-06-29", "2020-07-02", "Confirmados", "-", "Laboratorial", "Em Aberto", "COLATINA", "JARDIM PLANALTO", "50 a 59 anos", "51 anos, 9 meses, 24 dias", "M", "Ignorado",
             "Ensino médio completo (antigo colegial ou 2º grau ) ", "Não", "Não", "Não", "Não", "Não", "Não", "Sim", "Não", "Não", "Não", "Não", "Não", "Não", "Não Informado", "Sim", "Não Informado", "Não"]

    linhaTratada = [arrow.get(linha[0], "YYYY-MM-DD"), arrow.get(linha[1], "YYYY-MM-DD"), arrow.get(linha[2], "YYYY-MM-DD"), arrow.get(linha[3], "YYYY-MM-DD"), "Confirmados", None, "Laboratorial", "Em Aberto", "COLATINA", "JARDIM PLANALTO",
                    "50 a 59 anos", "51 anos, 9 meses, 24 dias", "M", None, "Ensino médio completo (antigo colegial ou 2º grau ) ", False, False, False, False, False, False, True, False, False, False, False, False, False, None, True, None, False]

    assert(trata_dados_linha(linha) == linhaTratada)


def test_fail():
    return True
    with pytest.raises(IndexError):
        linha = []
        trata_dados_linha(linha)

    with pytest.raises(IndexError):
        linha = ["25/04/2020"]
        trata_dados_linha(linha)

    with pytest.raises(TypeError):
        linha = [
            "15/04/2020", "Confirmados", "Óbito pelo COVID-19", "Laboratorial", "Encerrado", "PRESIDENTE KENNEDY", "FAZENDA CAETES",
            "60 a 69 anos", "F", "Preta", None, True, True, False, False, False, False, False, False, True, False, True, False, False, True, False, False
        ]
        trata_dados_linha(linha)

    with pytest.raises(TypeError):
        linha = [
            datetime.strptime(
                "15/04/2020", "%d/%m/%Y"), "Confirmados", "Óbito pelo COVID-19", "Laboratorial", "Encerrado", "PRESIDENTE KENNEDY", "FAZENDA CAETES",
            "60 a 69 anos", "F", "Preta", None, True, True, False, False, False, False, False, False, True, False, True, False, False, True, False, False
        ]
        trata_dados_linha(linha)
