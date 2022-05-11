import pytest

def func(x):
    return x+1

def test_answer():
    assert func(3)==5
    

def test_answer2():
    assert func(3)==6


def test_answer3():
    assert func(3)==4


##

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

