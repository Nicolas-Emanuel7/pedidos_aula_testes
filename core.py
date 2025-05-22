from estoque import verificar_estoque
from logger import logger

def calcular_total(preco_unitario, quantidade, desconto=0):
    if preco_unitario < 0 or quantidade <= 0:
        logger.error("Parâmetros inválidos para cálculo de total.")
        raise ValueError("Preço e quantidade devem ser positivos.")
    
    total_bruto = preco_unitario * quantidade
    total_final = total_bruto * (1 - desconto)
    
    logger.info(f"Total calculado: {total_final:.2f}")
    return total_final

def processar_pedido(produto_id, quantidade, preco_unitario, desconto=0):
    logger.info(f"Processando pedido de {quantidade} unidades de '{produto_id}'.")

    if not verificar_estoque(produto_id, quantidade):
        logger.warning(f"Estoque insuficiente para '{produto_id}'.")
        raise RuntimeError("Estoque insuficiente.")
    
    total = calcular_total(preco_unitario, quantidade, desconto)
    logger.info(f"Pedido processado com sucesso. Total: R${total:.2f}")
    return total

def finalizar_pedido(produto_id, quantidade):
    from estoque import estoque
    try:
        if estoque.get(produto_id, 0) < quantidade:
            raise RuntimeError("Estoque insuficiente para finalizar o pedido.")
        estoque[produto_id] -= quantidade
        logger.info(f"Pedido finalizado. {quantidade} unidades de '{produto_id}' removidas do estoque.")
    except Exception as e:
        logger.error(f"Erro ao finalizar pedido: {str(e)}")
        raise