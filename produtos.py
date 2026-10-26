
def cadastrar_produto(produtos):
    codigo = input("Código do produto: ").strip()

    if not codigo:
        print("O código não pode ficar vazio.")
        return

    if codigo in produtos:
        print("Erro: esse código já está cadastrado.")
        return

    nome = input("Nome do produto: ").strip()
    categoria = input("Categoria: ").strip()

    if not nome or not categoria:
        print("Nome e categoria são obrigatórios.")
        return

    try:
        preco = float(input("Preço unitário: R$ ").replace(",", "."))
        quantidade = int(input("Quantidade inicial: "))
    except ValueError:
        print("Digite um preço e uma quantidade válidos.")
        return

    if preco <= 0 or quantidade < 0:
        print("O preço deve ser positivo e a quantidade não pode ser negativa.")
        return

    produtos[codigo] = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    print("Produto cadastrado com sucesso!")


def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for codigo, produto in produtos.items():
        print(
            f"Código: {codigo} | "
            f"Nome: {produto['nome']} | "
            f"Categoria: {produto['categoria']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Quantidade: {produto['quantidade']}"
        )


def consultar_produto(produtos):
    termo = input("Digite o código, nome ou categoria: ").strip().lower()

    encontrados = {
        codigo: produto
        for codigo, produto in produtos.items()
        if termo == codigo.lower()
        or termo in produto["nome"].lower()
        or termo in produto["categoria"].lower()
    }

    listar_produtos(encontrados)


def atualizar_produto(produtos):
    codigo = input("Código do produto: ").strip()

    if codigo not in produtos:
        print("Produto não encontrado.")
        return

    produto = produtos[codigo]

    print("Deixe vazio o campo que não deseja alterar.")

    nome = input(f"Nome [{produto['nome']}]: ").strip()
    categoria = input(
        f"Categoria [{produto['categoria']}]: "
    ).strip()
    preco_texto = input(
        f"Preço [{produto['preco']:.2f}]: "
    ).strip()

    if nome:
        produto["nome"] = nome

    if categoria:
        produto["categoria"] = categoria

    if preco_texto:
        try:
            preco = float(preco_texto.replace(",", "."))
            if preco <= 0:
                print("Preço inválido. Alteração cancelada.")
                return
            produto["preco"] = preco
        except ValueError:
            print("Preço inválido. Alteração cancelada.")
            return

    print("Produto atualizado com sucesso!")


def remover_produto(produtos):
    codigo = input("Código do produto: ").strip()

    if codigo not in produtos:
        print("Produto não encontrado.")
        return

    confirmacao = input(
        f"Deseja remover {produtos[codigo]['nome']}? (s/n): "
    ).strip().lower()

    if confirmacao == "s":
        del produtos[codigo]
        print("Produto removido com sucesso.")
    else:
        print("Remoção cancelada.")


def ordenar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("1 - Ordenar por nome")
    print("2 - Ordenar por preço")
    print("3 - Ordenar por quantidade")

    opcao = input("Escolha: ")

    campos = {
        "1": "nome",
        "2": "preco",
        "3": "quantidade"
    }

    campo = campos.get(opcao)

    if campo is None:
        print("Opção inválida.")
        return

    ordenados = sorted(
        produtos.items(),
        key=lambda item: item[1][campo]
    )

    for codigo, produto in ordenados:
        print(
            f"{codigo} - {produto['nome']} | "
            f"R$ {produto['preco']:.2f} | "
            f"Estoque: {produto['quantidade']}"
        )


def listar_por_categoria(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    categorias = sorted({
        produto["categoria"]
        for produto in produtos.values()
    }, key=str.lower)

    for categoria in categorias:
        print(f"\nCategoria: {categoria}")

        for codigo, produto in produtos.items():
            if produto["categoria"].lower() == categoria.lower():
                print(
                    f"  {codigo} - {produto['nome']} "
                    f"(Estoque: {produto['quantidade']})"
                )
