import pytest
from primo import es_primo

def test_numeros_menores_a_2():
    assert es_primo(0) == False
    assert es_primo(1) == False
    assert es_primo(-5) == False

def test_numero_2_es_primo():
    assert es_primo(2) == True

def test_numeros_pares_no_son_primos():
    assert es_primo(4) == False
    assert es_primo(10) == False
    assert es_primo(100) == False

def test_numeros_primos():
    assert es_primo(3) == True
    assert es_primo(7) == True
    assert es_primo(97) == True

def test_numeros_no_primos():
    assert es_primo(9) == False
    assert es_primo(15) == False
    assert es_primo(25) == False