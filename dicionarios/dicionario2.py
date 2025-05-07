lista_de_compras = {
    "produtos": ["macarrao", "miojo", "banana", "maça"],
    "quantidades": [1, 2, 3, 4],
    "precos": [2.50, 1.00, 5.00, 10.00]
}

# Exibindo cada produto com sua quantidade e preço
for i in range(len(lista_de_compras["produtos"])):
    produto = lista_de_compras["produtos"][i]
    quantidade = lista_de_compras["quantidades"][i]
    preco = lista_de_compras["precos"][i]
    print(f"Produto: {produto}, Quantidade: {quantidade}, Preço: R${preco:.2f}")
    