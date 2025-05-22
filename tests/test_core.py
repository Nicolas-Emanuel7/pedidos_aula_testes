import pytest
from core import calcular_total, processar_pedido, finalizar_pedido
from estoque import cadastrar_produto, estoque

def test_calcular_total_sem_desconto():
    assert calcular_total(10, 2) == 20

def test_calcular_total_com_desconto():
    assert calcular_total(10, 2, desconto=0.1) == 18

def test_calcular_total_parametros_invalidos():
    with pytest.raises(ValueError):
        calcular_total(-5, 2)

def test_processar_pedido_sucesso():
    total = processar_pedido("produto_1", 2, 15)
    assert total == 30

def test_processar_pedido_estoque_insuficiente():
    with pytest.raises(RuntimeError):
        processar_pedido("produto_2", 1, 10)

def test_cadastrar_produto_novo():
    cadastrar_produto("produto_novo", 5)
    assert estoque["produto_novo"] == 5

def test_cadastrar_produto_existente():
    with pytest.raises(KeyError):
        cadastrar_produto("produto_1", 5)

def test_finalizar_pedido_sucesso():
    estoque["produto_1"] = 5
    finalizar_pedido("produto_1", 2)
    assert estoque["produto_1"] == 3

def test_finalizar_pedido_falha():
    estoque["produto_1"] = 1
    with pytest.raises(RuntimeError):
        finalizar_pedido("produto_1", 5)