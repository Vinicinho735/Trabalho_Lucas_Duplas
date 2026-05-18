import pytest
from calculadora import Calculadora


def test_soma():
    calc = Calculadora()
    
    assert calc.soma(2, 3) == 5           
    assert calc.soma(-7, 4) == -3         
    assert calc.soma(0.1, 0.2) == pytest.approx(0.3)  

def test_subtracao():
    calc = Calculadora()
    assert calc.subtracao(10, 5) == 5

def test_multiplicacao():
    calc = Calculadora()
    assert calc.multiplicacao(3, 4) == 12

def test_divisao():
    calc = Calculadora()
    assert calc.divisao(10, 2) == 5


def test_varias_operacoes():
    """Valida o comportamento das operações em sequência (cadeia)"""
    calc = Calculadora()
    
    resultado = calc.soma(10.5, 4.5)
    
    resultado = calc.subtracao(resultado, 3)
    
    resultado = calc.soma(resultado, -2)
    
    resultado = calc.multiplicacao(resultado, 2)
    
    assert resultado == 20.0

def test_divisao_por_zero():
    calc = Calculadora()
    with pytest.raises(ValueError):
        calc.divisao(10, 0)
        
def test_potencia():
    calc = Calculadora()
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1