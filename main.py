
from produtos import (
    cadastrar_produto,
    listar_produtos,
    consultar_produto,
    atualizar_produto,
    remover_produto,
    ordenar_produtos,
    listar_por_categoria
)

from movimentacoes import (
    registrar_entrada,
    registrar_saida,
    mostrar_historico
)

from relatorios import gerar_relatorio


produtos = {}
historico = []


def menu():
    while True:
        print("\n========== SISTEMA DE ESTOQUE ==========")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Consultar produto")
        print("4 - Atualizar produto")
        print("5 - Remover produto")
        print("6 - Registrar entrada")
        print("7 - Registrar saída")
        print("8 - Gerar relatório")
        print("9 - Ver histórico de movimentações")
        print("10 - Ordenar produtos")
        print("11 - Listar produtos por categoria")
        print("0 - Encerrar sistema")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto(produtos)

        elif opcao == "2":
            listar_produtos(produtos)

        elif opcao == "3":
            consultar_produto(produtos)

        elif opcao == "4":
            atualizar_produto(produtos)

        elif opcao == "5":
            remover_produto(produtos)

        elif opcao == "6":
            registrar_entrada(produtos, historico)

        elif opcao == "7":
            registrar_saida(produtos, historico)

        elif opcao == "8":
            gerar_relatorio(produtos)

        elif opcao == "9":
            mostrar_historico(historico)

        elif opcao == "10":
            ordenar_produtos(produtos)

        elif opcao == "11":
            listar_por_categoria(produtos)

        elif opcao == "0":
            print("Sistema encerrado. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
