
LIMITE_MINIMO = 5


def gerar_relatorio(produtos):
    if not produtos:
        print("Nenhum produto cadastrado para gerar relatório.")
        return

    total_unidades = sum(
        produto["quantidade"]
        for produto in produtos.values()
    )

    valor_total = sum(
        produto["preco"] * produto["quantidade"]
        for produto in produtos.values()
    )

    sem_estoque = [
        (codigo, produto)
        for codigo, produto in produtos.items()
        if produto["quantidade"] == 0
    ]

    abaixo_minimo = [
        (codigo, produto)
        for codigo, produto in produtos.items()
        if 0 < produto["quantidade"] < LIMITE_MINIMO
    ]

    print("\n========== RELATÓRIO DE ESTOQUE ==========")
    print(f"Total de produtos cadastrados: {len(produtos)}")
    print(f"Total de unidades disponíveis: {total_unidades}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

    print("\n--- PRODUTOS SEM ESTOQUE ---")

    if sem_estoque:
        for codigo, produto in sem_estoque:
            print(f"{codigo} - {produto['nome']}")
    else:
        print("Nenhum produto com estoque zerado.")

    print("\n--- ABAIXO DO LIMITE MÍNIMO ---")

    if abaixo_minimo:
        for codigo, produto in abaixo_minimo:
            print(
                f"{codigo} - {produto['nome']} | "
                f"Quantidade: {produto['quantidade']}"
            )
    else:
        print("Nenhum produto abaixo do limite mínimo.")
