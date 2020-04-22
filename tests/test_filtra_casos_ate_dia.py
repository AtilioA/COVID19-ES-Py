from pathlib import Path
from COVID19_ES_Py import LeitorRelatorio


def test_22_04():
    leitor = LeitorRelatorio(Path("tests/relatorios_passados/22-04-2020.csv"))
    relatorio = leitor.filtra_casos_ate_dia("22/04/2020")

    assert(relatorio.busca_casos_municipio("Vitória").casosConfirmados == 291)
    assert(relatorio.busca_casos_municipio("Vitória").obitos == 9)

    assert(relatorio.busca_casos_municipio("  santa teresa ").casosConfirmados == 4)
    assert(relatorio.busca_casos_municipio("  santa teresa ").obitos == 0)

    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").casosConfirmados == 2)
    assert(relatorio.busca_casos_municipio("AFONSO CLAUDIO").obitos == 0)

    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)
    assert(relatorio.busca_casos_municipio("vILA pavao").obitos == 0)
