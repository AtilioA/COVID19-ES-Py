"""O módulo `utils.py` contém funções auxiliares."""

import unicodedata


def remove_caracteres_especiais(stringEntrada):
    """Remove caracteres especiais (acentos, etc) de uma string."""

    formaNFKD = unicodedata.normalize('NFKD', stringEntrada)
    return u"".join([c for c in formaNFKD if not unicodedata.combining(c)])
