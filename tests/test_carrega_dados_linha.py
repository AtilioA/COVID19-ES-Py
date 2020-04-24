import arrow
import pytest

from COVID19_ES_Py.relatorio import Caso


def test_success():
    caso = Caso()
    caso.carrega_dados_linha(["24/04/2020", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                              "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"])
    assert caso.data == arrow.get("24/04/2020", "DD/MM/YYYY")
    assert caso.classificacao == "2"
    assert caso.evolucao == "3"
    assert caso.criterioConfirmacao == "4"
    assert caso.statusNotificacao == "5"
    assert caso.municipio == "6"
    assert caso.bairro == "7"
    assert caso.faixaEtaria == "8"
    assert caso.sexo == "9"
    assert caso.racaCor == "10"
    assert caso.escolaridade == "11"
    assert caso.sintomas == {
        "febre": None,
        "dificuldadeRespiratoria": None,
        "tosse": None,
        "coriza": None,
        "dorGarganta": None,
        "diarreia": None,
        "cefaleia": None
    }
    assert caso.comorbidades == {
        "comorbidadePulmao": None,
        "comorbidadeCardio": None,
        "comorbidadeRenal": None,
        "comorbidadeDiabetes": None,
        "comorbidadeTabagismo": None,
        "comorbidadeObesidade": None
    }
    assert caso.ficouInternado == None
    assert caso.viagemBrasil == None
    assert caso.viagemInternacional == None

    caso = Caso()
    linha = ["27/04/2020", "Confirmados", "-", "Laboratorial", "Em Aberto", "SERRA", "PARQUE DAS GAIVOTAS", "60 a 69 anos", "M",
             "Branca", "Analfabeto", "Não", "Sim", "Não", "Não", "Não", "Não", "Não", "Não", "Sim", "Não", "Sim", "Sim", "Não", "-", "-", "-"]
    caso.carrega_dados_linha(linha)

    linhaTratada = [arrow.get(linha[0], "DD/MM/YYYY"), "Confirmados", None, "Laboratorial", "Em Aberto", "SERRA", "PARQUE DAS GAIVOTAS", "60 a 69 anos",
                    "M", "Branca", "Analfabeto", False, True, False, False, False, False, False, False, True, False, True, True, False, None, None, None]

    assert caso.data == linhaTratada[0]
    assert caso.classificacao == linhaTratada[1]
    assert caso.evolucao == linhaTratada[2]
    assert caso.criterioConfirmacao == linhaTratada[3]
    assert caso.statusNotificacao == linhaTratada[4]
    assert caso.municipio == linhaTratada[5]
    assert caso.bairro == linhaTratada[6]
    assert caso.faixaEtaria == linhaTratada[7]
    assert caso.sexo == linhaTratada[8]
    assert caso.racaCor == linhaTratada[9]
    assert caso.escolaridade == linhaTratada[10]
    assert caso.sintomas == {
        "febre": linhaTratada[11],
        "dificuldadeRespiratoria": linhaTratada[12],
        "tosse": linhaTratada[13],
        "coriza": linhaTratada[14],
        "dorGarganta": linhaTratada[15],
        "diarreia": linhaTratada[16],
        "cefaleia": linhaTratada[17]
    }
    assert caso.comorbidades == {
        "comorbidadePulmao": linhaTratada[18],
        "comorbidadeCardio": linhaTratada[19],
        "comorbidadeRenal": linhaTratada[20],
        "comorbidadeDiabetes": linhaTratada[21],
        "comorbidadeTabagismo": linhaTratada[22],
        "comorbidadeObesidade": linhaTratada[23]
    }
    assert caso.ficouInternado == linhaTratada[24]
    assert caso.viagemBrasil == linhaTratada[25]
    assert caso.viagemInternacional == linhaTratada[26]


def test_fail():
    caso = Caso()
    with pytest.raises(IndexError):
        caso.carrega_dados_linha([])
    with pytest.raises(IndexError):
        caso.carrega_dados_linha([123])
    with pytest.raises(TypeError):
        caso.carrega_dados_linha(False)
    with pytest.raises(TypeError):
        caso.carrega_dados_linha(None)
