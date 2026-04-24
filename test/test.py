from unittest.mock import patch
from src.main import *
import pytest

@pytest.mark.asyncio
async def test_root():
    assert await root() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoTeste():
    with patch('random.randint', return_value = 12345):
        result = await funcaoTeste()

    assert result == {
        "Message": "Deu certo",
        "Teste": True,
        "Num_aleatorio": 12345
    }

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_test = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    assert estudante_test == await create_estudante(estudante_test)

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    assert not await update_estudante(-5)

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    assert await update_estudante(10)

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    assert not await delete_estudante(-5)

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    assert await delete_estudante(5)