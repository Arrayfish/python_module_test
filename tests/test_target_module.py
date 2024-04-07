import pytest
import python_module_test
from python_module_test.main import main

@pytest.fixture
def python_mock_module(mocker):
    return mocker.patch("python_module_test.hello")

def test_function_hello():
    assert python_module_test.hello() == "Hello from python-module-test!"
    
def test_main_function(python_mock_module):
    assert main() == "o_module_value"
    python_mock_module.assert_called_once()