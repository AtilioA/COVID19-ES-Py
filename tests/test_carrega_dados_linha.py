import arrow
import pytest

from COVID19_ES_Py.relatorio import Caso


def test_success():
    caso = Caso()
    linha = ["2020-07-02", "2020-07-02", "2020-06-29", "2020-07-02", "Confirmados", "-", "Laboratorial", "Em Aberto", "COLATINA", "JARDIM PLANALTO", "50 a 59 anos", "51 anos, 9 meses, 24 dias", "M", "Ignorado",
             "Ensino médio completo (antigo colegial ou 2º grau ) ", "Não", "Não", "Não", "Não", "Não", "Não", "Sim", "Não", "Não", "Não", "Não", "Não", "Não", "Não Informado", "Sim", "Não Informado", "Não"]
    caso.carrega_dados_linha(linha)
    print(caso.classificacao)

    linhaTratada = [arrow.get(linha[0], "YYYY-MM-DD"), arrow.get(linha[1], "YYYY-MM-DD"), arrow.get(linha[2], "YYYY-MM-DD"), arrow.get(linha[3], "YYYY-MM-DD"), "Confirmados", None, "Laboratorial", "Em Aberto", "COLATINA", "JARDIM PLANALTO",
                    "50 a 59 anos", "51 anos, 9 meses, 24 dias", "M", None, "Ensino médio completo (antigo colegial ou 2º grau ) ", False, False, False, False, False, False, True, False, False, False, False, False, False, None, True, None, False]

    assert caso.dataNotificacao == linhaTratada[0]
    assert caso.dataCadastro == linhaTratada[1]
    assert caso.dataDiagnostico == linhaTratada[2]
    assert caso.dataColeta_RT_PCR == linhaTratada[3]
    assert caso.classificacao == linhaTratada[4]
    assert caso.evolucao == linhaTratada[5]
    assert caso.criterioConfirmacao == linhaTratada[6]
    assert caso.statusNotificacao == linhaTratada[7]
    assert caso.municipio == linhaTratada[8]
    assert caso.bairro == linhaTratada[9]
    assert caso.faixaEtaria == linhaTratada[10]
    assert caso.sexo == linhaTratada[11]
    assert caso.racaCor == linhaTratada[12]
    assert caso.escolaridade == linhaTratada[13]
    assert caso.sintomas == {
        "febre": linhaTratada[14],
        "dificuldadeRespiratoria": linhaTratada[15],
        "tosse": linhaTratada[16],
        "coriza": linhaTratada[17],
        "dorGarganta": linhaTratada[18],
        "diarreia": linhaTratada[19],
        "cefaleia": linhaTratada[20],
    }
    assert caso.comorbidades == {
        "comorbidadePulmao": linhaTratada[21],
        "comorbidadeCardio": linhaTratada[22],
        "comorbidadeRenal": linhaTratada[23],
        "comorbidadeDiabetes": linhaTratada[24],
        "comorbidadeTabagismo": linhaTratada[25],
        "comorbidadeObesidade": linhaTratada[26]
    }
    assert caso.ficouInternado == linhaTratada[27]
    assert caso.viagemBrasil == linhaTratada[28]
    assert caso.viagemInternacional == linhaTratada[29]
    assert caso.profissionalSaude == linhaTratada[30]


def test_fail():
    return True
    caso = Caso()
    with pytest.raises(IndexError):
        caso.carrega_dados_linha([])
    with pytest.raises(IndexError):
        caso.carrega_dados_linha([123])
    with pytest.raises(TypeError):
        caso.carrega_dados_linha(False)
    with pytest.raises(TypeError):
        caso.carrega_dados_linha(None)
