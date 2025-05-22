from estoque import cadastrar_produto, estoque
from core import processar_pedido, finalizar_pedido
from logger import logger

def exibir_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    for produto, qtd in estoque.items():
        print(f"{produto}: {qtd} unidades")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar Produto")
        print("2. Fazer Pedido")
        print("3. Finalizar Pedido")
        print("4. Ver Estoque")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = input("ID do produto: ")
            try:
                qtd = int(input("Quantidade inicial: "))
                cadastrar_produto(produto, qtd)
            except Exception as e:
                print(f"Erro: {str(e)}")

        elif opcao == "2":
            produto = input("ID do produto: ")
            try:
                qtd = int(input("Quantidade: "))
                preco = float(input("Preço unitário: "))
                desc = float(input("Desconto (0 a 1, ex: 0.1 para 10%): ") or 0)
                total = processar_pedido(produto, qtd, preco, desc)
                print(f"Total do pedido: R${total:.2f}")
            except Exception as e:
                print(f"Erro: {str(e)}")

        elif opcao == "3":
            produto = input("ID do produto: ")
            try:
                qtd = int(input("Quantidade a remover do estoque: "))
                finalizar_pedido(produto, qtd)
                print("Pedido finalizado.")
            except Exception as e:
                print(f"Erro: {str(e)}")

        elif opcao == "4":
            exibir_estoque()

        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    logger.info("Iniciando sistema de pedidos...")
    menu()
    logger.info("Encerrando sistema de pedidos.")
