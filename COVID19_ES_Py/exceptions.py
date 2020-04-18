"""O módulo `exceptions.py` apenas declara as exceções `BoletimError` (descontinuada) e `RelatorioError`."""

from deprecated import deprecated


@deprecated(version='2.0.0', reason="BoletimError foi descontinuado no COVID19-ES-Py 2.0.0, e será substituído por `RelatorioError` na versão 3.0.0 uma vez que a SESA não emitirá mais boletins de COVID19.")
class BoletimError(Exception):
    pass


class RelatorioError(Exception):
    pass
