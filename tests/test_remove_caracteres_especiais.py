import pytest

from COVID19_ES_Py.utils import remove_caracteres_especiais


def test_success():
    assert remove_caracteres_especiais("Afonso Cláudio") == "Afonso Claudio"
    assert remove_caracteres_especiais("Sooretama") == "Sooretama"
    assert remove_caracteres_especiais("Ibiraçu") == "Ibiracu"
    assert remove_caracteres_especiais(
        " Sao Gabriel da Palha") == " Sao Gabriel da Palha"
    assert remove_caracteres_especiais(
        "São Jose do Calçado") == "Sao Jose do Calcado"
    assert remove_caracteres_especiais("PIÚMA") == "PIUMA"
    assert remove_caracteres_especiais(
        "JERÔNIMO MONTEIRO ") == "JERONIMO MONTEIRO "
    assert remove_caracteres_especiais("GUAÇUÍ") == "GUACUI"
    assert remove_caracteres_especiais("") == ""
    assert remove_caracteres_especiais("1") == "1"
    assert remove_caracteres_especiais("_") == "_"


def test_fail():
    with pytest.raises(TypeError):
        remove_caracteres_especiais(123)
    with pytest.raises(TypeError):
        remove_caracteres_especiais(False)
    with pytest.raises(TypeError):
        remove_caracteres_especiais(True)
    with pytest.raises(TypeError):
        remove_caracteres_especiais(None)
    with pytest.raises(TypeError):
        remove_caracteres_especiais(["A"])
    with pytest.raises(TypeError):
        remove_caracteres_especiais(("A",))
    with pytest.raises(TypeError):
        remove_caracteres_especiais({"A"})
