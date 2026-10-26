
def registrar_entrada(produtos, historico):
    codigo = input("Código do produto: ").strip()

    if codigo not in produtos:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade recebida: "))
    except ValueError:
        print("Digite uma quantidade inteira válida.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    produtos[codigo]["quantidade"] += quantidade

    historico.append({
        "codigo": codigo,
        "nome": produtos[codigo]["nome"],
        "tipo": "Entrada",
        "quantidade": quantidade
    })

    print("Entrada registrada com sucesso.")


def registrar_saida(produtos, historico):
    codigo = input("Código do produto: ").strip()

    if codigo not in produtos:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade retirada: "))
    except ValueError:
        print("Digite uma quantidade inteira válida.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    estoque = produtos[codigo]["quantidade"]

    if quantidade > estoque:
        print("Erro: estoque insuficiente.")
        print(f"Quantidade disponível: {estoque}")
        return

    produtos[codigo]["quantidade"] -= quantidade

    historico.append({
        "codigo": codigo,
        "nome": produtos[codigo]["nome"],
        "tipo": "Saída",
        "quantidade": quantidade
    })

    print("Saída registrada com sucesso.")


def mostrar_historico(historico):
    if not historico:
        print("Nenhuma movimentação registrada.")
        return

    print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---")

    for numero, movimento in enumerate(historico, start=1):
        print(
            f"{numero}. {movimento['tipo']} | "
            f"Código: {movimento['codigo']} | "
            f"Produto: {movimento['nome']} | "
            f"Quantidade: {movimento['quantidade']}"
        )
