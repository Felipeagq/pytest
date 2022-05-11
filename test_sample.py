import pytest
import os

os.system("clear")

def func(x):
    return x+1

def test_answer():
    assert func(3)==5
    
def test_answer2():
    assert func(3)==6

def test_answer3():
    assert func(3)==4

# Parametrize

@pytest.mark.parametrize("a,expected_result",
    [
        (1,2),
        (2,3),
        (3,4)
    ]
)

def test_func(a,expected_result):
    assert func(a) == expected_result



## FIXTURE

class Persona:
    def __init__(self,name,edad,dinero):
        self.name = name
        self.edad = edad + 5
        self.dinero = dinero + 20000

@pytest.fixture
def crear_persona():
    return Persona(
        name="felipe",
        edad=22,
        dinero=2000
    )

def get_name(persona:Persona):
    return persona.name

def test_get_nme_persona(crear_persona):
    assert get_name(crear_persona) == "felipe"

def test_get_nme_persona(crear_persona):
    assert get_name(crear_persona) == "Camila"


## FIXTURE: PYTEST-MOCK

def some_calculation(a,b):
    return a+b

def make_a_dict(a,b):
    operation = some_calculation(a,b)
    return {
        "a":a,
        "b":b,
        "result":operation
    }

def test_some_calculation():
    assert some_calculation(1,2) == 3

# def test_make_a_dict(mocker):
#     mocker.patch