
def pon(altura, peso):
    soma2= peso / (altura ** 2)
    
    if soma2 < 18.5:
        return soma2, "Você está abaixo do peso"
    elif 18.5 <= soma2 < 24.9:
        return soma2, "Você está com o peso normal"
    elif 25 <= soma2 < 29.9:
        return soma2, "Você está acima do peso"
    else:
        return soma2, "Você está obeso"

altura = 2.00
peso = 90
soma2, classificacao = pon(altura, peso)
print(f"IMC: {soma2:.2f} - {classificacao}")
