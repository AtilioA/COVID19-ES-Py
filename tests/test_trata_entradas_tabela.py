import pytest

from COVID19_ES_Py.utils import trata_dados_tabela


def test_success():
    # Trata caracteres "vazios" ou traços
    assert trata_dados_tabela([""]) == ["0"]
    assert trata_dados_tabela([" "]) == ["0"]
    assert trata_dados_tabela(["  "]) == ["0"]
    assert trata_dados_tabela(["   "]) == ["0"]
    assert trata_dados_tabela(["&nbsp;"]) == ["0"]
    assert trata_dados_tabela([u"\xa0"]) == ["0"]
    assert trata_dados_tabela(["-"]) == ["0"]
    assert trata_dados_tabela([" -"]) == ["0"]
    assert trata_dados_tabela(["- "]) == ["0"]
    assert trata_dados_tabela([" - "]) == ["0"]

    # Nenhuma mudança
    assert trata_dados_tabela([]) == []
    assert trata_dados_tabela(["A"]) == ["A"]
    assert trata_dados_tabela(["Santa Teresa"]) == ["Santa Teresa"]
    assert trata_dados_tabela(["1"]) == ["1"]
    assert trata_dados_tabela(["0"]) == ["0"]
    assert trata_dados_tabela(["A"]) == ["A"]
    assert trata_dados_tabela(["Santa Teresa"]) == ["Santa Teresa"]
    assert trata_dados_tabela(["1"]) == ["1"]
    assert trata_dados_tabela(["0"]) == ["0"]
    assert trata_dados_tabela(["00"]) == ["00"]
    assert trata_dados_tabela(["Não muda"]) == ["Não muda"]
    assert trata_dados_tabela([" Não muda"]) == [" Não muda"]
    assert trata_dados_tabela([" Não muda "]) == [" Não muda "]


def test_fail():
    with pytest.raises(TypeError):
        trata_dados_tabela(123)
    with pytest.raises(TypeError):
        trata_dados_tabela(False)
    with pytest.raises(TypeError):
        trata_dados_tabela(True)
    with pytest.raises(TypeError):
        trata_dados_tabela(None)
