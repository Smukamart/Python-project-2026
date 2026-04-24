from unittest.mock import patch
from src.main import *
import pytest

@pytest.mark.asyncio
def test_root():
    assert root() == {"message": "Hello World"}

@pytest.mark.asyncio
def test_funcaoTeste():
    with patch('random.randint', return_value = 12345):
        result = funcaoTeste()

    assert result == {
        "Message": "Deu certo",
        "Teste": True,
        "Num_aleatorio": 12345
    }

@pytest.mark.asyncio
def test_create_estudante():
    estudante_test = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    assert estudante_test == create_estudante(estudante_test)

@pytest.mark.asyncio
def test_update_estudante_negativo():
    assert not update_estudante(-5)

@pytest.mark.asyncio
def test_update_estudante_positivo():
    assert update_estudante(10)

@pytest.mark.asyncio
def test_delete_estudante_negativo():
    assert not delete_estudante(-5)

@pytest.mark.asyncio
def test_delete_estudante_positivo():
    assert delete_estudante(5)