taxa = 7.5   
custo = 100.0 


def soma_imposto(taxa_imposto, custo):
    return custo * (1 + taxa_imposto / 100)
print(soma_imposto(taxa, custo)) 