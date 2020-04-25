from pathlib import Path
import pytest
from COVID19_ES_Py import Relatorio, exceptions


def test_18_04():
    relatorio = Relatorio(
        Path("tests/relatorios_passados/18-04-2020.csv"))
    relatorio.popula_relatorio()

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 244)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 9)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 4)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 2)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 0)

    assert(relatorio.busca_casos_municipio("vILA pavao").casosConfirmados == 0)
    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)


def test_20_04():
    pass
    relatorio = Relatorio(
        Path("tests/relatorios_passados/20-04-2020.csv"))
    relatorio.popula_relatorio()

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 265)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 9)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 4)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 2)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 0)

    assert(relatorio.busca_casos_municipio("vILA pavao").casosConfirmados == 0)
    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)


def test_21_04():
    relatorio = Relatorio(
        Path("tests/relatorios_passados/21-04-2020.csv"))
    relatorio.popula_relatorio()

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 290)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 9)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 4)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 2)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 0)

    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)
    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)


def test_22_04():
    relatorio = Relatorio(
        Path("tests/relatorios_passados/22-04-2020.csv"))
    relatorio.popula_relatorio()

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 291)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 9)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 4)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 2)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 0)

    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)
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
