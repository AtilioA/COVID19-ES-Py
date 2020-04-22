from COVID19_ES_Py.utils import MUNICIPIOS
from COVID19_ES_Py.relatorio import Relatorio


def test_success():
    relatorio = Relatorio()
    for municipio in MUNICIPIOS:
        relatorio.casosMunicipios[municipio].nome == municipio
        relatorio.casosMunicipios[municipio].casosConfirmados == 0
        relatorio.casosMunicipios[municipio].obitos == 0
        relatorio.casosMunicipios[municipio].casos == []
