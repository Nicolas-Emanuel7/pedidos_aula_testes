estoque = {
    "produto_1": 10,
    "produto_2": 0,   # Sem estoque
}

def verificar_estoque(produto_id, quantidade):
    return estoque.get(produto_id, 0) >= quantidade
