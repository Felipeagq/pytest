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



## source
https://www.youtube.com/watch?v=E4Yc8dhM638&t=1s