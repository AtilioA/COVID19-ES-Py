from pathlib import Path
from COVID19_ES_Py import LeitorRelatorio


def test_02_05():
    leitor = LeitorRelatorio(Path("tests/relatorios_passados/02-05-2020.csv"))
    relatorio = leitor.filtra_casos_ate_dia("02052020")

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 621)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 18)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 16)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 11)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 2)

    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)
    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)


def test_03_05():
    leitor = LeitorRelatorio(Path("tests/relatorios_passados/03-05-2020.csv"))
    relatorio = leitor.filtra_casos_ate_dia("03.05.2020")

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 628)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 20)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 16)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 13)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 2)

    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)
    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)
