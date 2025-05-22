estoque = {
    "produto_1": 10,
    "produto_2": 0,   # Sem estoque
}

def verificar_estoque(produto_id, quantidade):
    return estoque.get(produto_id, 0) >= quantidade

def cadastrar_produto(produto_id, quantidade):
    from logger import logger
    try:
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        if produto_id in estoque:
            raise KeyError("Produto já cadastrado.")
        estoque[produto_id] = quantidade
        logger.info(f"Produto '{produto_id}' cadastrado com {quantidade} unidades.")
    except Exception as e:
        logger.error(f"Erro ao cadastrar produto: {str(e)}")
        raise
