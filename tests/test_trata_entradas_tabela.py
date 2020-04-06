import pytest

from COVID19_ES_Py.utils import trata_entradas_tabela


def test_success():
    # Trata caracteres "vazios" ou traços
    assert trata_entradas_tabela([""]) == ["0"]
    assert trata_entradas_tabela([" "]) == ["0"]
    assert trata_entradas_tabela(["  "]) == ["0"]
    assert trata_entradas_tabela(["   "]) == ["0"]
    assert trata_entradas_tabela(["&nbsp;"]) == ["0"]
    assert trata_entradas_tabela([u"\xa0"]) == ["0"]
    assert trata_entradas_tabela(["-"]) == ["0"]
    assert trata_entradas_tabela([" -"]) == ["0"]
    assert trata_entradas_tabela(["- "]) == ["0"]
    assert trata_entradas_tabela([" - "]) == ["0"]

    # Nenhuma mudança
    assert trata_entradas_tabela([]) == []
    assert trata_entradas_tabela(["A"]) == ["A"]
    assert trata_entradas_tabela(["Santa Teresa"]) == ["Santa Teresa"]
    assert trata_entradas_tabela(["1"]) == ["1"]
    assert trata_entradas_tabela(["0"]) == ["0"]
    assert trata_entradas_tabela(["A"]) == ["A"]
    assert trata_entradas_tabela(["Santa Teresa"]) == ["Santa Teresa"]
    assert trata_entradas_tabela(["1"]) == ["1"]
    assert trata_entradas_tabela(["0"]) == ["0"]
    assert trata_entradas_tabela(["00"]) == ["00"]
    assert trata_entradas_tabela(["Não muda"]) == ["Não muda"]
    assert trata_entradas_tabela([" Não muda"]) == [" Não muda"]
    assert trata_entradas_tabela([" Não muda "]) == [" Não muda "]


def test_fail():
    with pytest.raises(TypeError):
        trata_entradas_tabela(123)
    with pytest.raises(TypeError):
        trata_entradas_tabela(False)
    with pytest.raises(TypeError):
        trata_entradas_tabela(True)
    with pytest.raises(TypeError):
        trata_entradas_tabela(None)
