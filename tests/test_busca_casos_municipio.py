from pathlib import Path
import pytest
from COVID19_ES_Py import Relatorio, exceptions


def test_30_04():
    relatorio = Relatorio(
        Path("tests/relatorios_passados/30-04-2020.csv"))
    relatorio.popula_relatorio()

    print(relatorio)

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 554)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 16)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 14)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 10)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 2)

    assert(relatorio.busca_casos_municipio("vILA pavao").casosConfirmados == 0)
    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)


def test_02_04():
    relatorio = Relatorio(
        Path("tests/relatorios_passados/02-05-2020.csv"))
    relatorio.popula_relatorio()

    print(relatorio)

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 621)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 18)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 17)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 11)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 2)

    assert(relatorio.busca_casos_municipio("vILA pavao").casosConfirmados == 0)
    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)


def test_03_04():
    relatorio = Relatorio(
        Path("tests/relatorios_passados/03-05-2020.csv"))
    relatorio.popula_relatorio()

    print(relatorio)

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 628)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 20)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 17)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 13)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 2)

    assert(relatorio.busca_casos_municipio("vILA pavao").casosConfirmados == 0)
    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)


def test_fail_21_04():
    relatorio = Relatorio(Path("tests/relatorios_passados/21-04-2020.csv"))

    # Município não é do ES
    with pytest.raises(exceptions.RelatorioError):
        relatorio.busca_casos_municipio("arapiraca")

    # Nome de município incompleto ou errado
    with pytest.raises(exceptions.RelatorioError):
        relatorio.busca_casos_municipio("vi")

    # Tipo incorreto de parâmetro
    with pytest.raises(TypeError):
        relatorio.busca_casos_municipio(1)
