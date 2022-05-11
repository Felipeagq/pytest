# PyTest
The ```pytest``` framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

pytest will run all files of the form ````test_*.py```` or ```*_test.py``` in the current directory and its subdirectories.

Run tests in a module : ```pytest test_mod.py```
Run tests in a directory :```pytest testing/```

Run a specific test in a file : ```pytest test_mod.py::test_func```

Run a specific test in a class of a file : ```pytest test_mod.py::TestClass::test_method```  

## assert
- assert True : No levanta error.
- assert False : Levanta error
````
# test_with_pytest.py

def test_always_passes():
    assert True

def test_always_fails():
    assert False
````


## @pytest.fixture
Este decorador nos permite recibir una función como parametro de nuestra función de testing, nuestra función necesariamente debe retornar un valor o objeto.
- Primero creamos una función, en este caso retornará la creación de un objeto.
```python
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
```
- Luego tenemos la función de nuestro codigo que queremos examinar su comportamiento y testearla.
```python
def get_name(persona:Persona):
    return persona.name
```
- Luego creamos la función de testing y le pasamos como parametro nuestra función que definimos en nuestro fixture.
```python 
def test_get_nme_persona(crear_persona):
    assert get_name(crear_persona) == "felipe"
```


## source
https://www.youtube.com/watch?v=E4Yc8dhM638&t=1s