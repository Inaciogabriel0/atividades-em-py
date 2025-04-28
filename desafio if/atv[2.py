notas = [70,70,80,90]

nome = "davi"

soma = sum(notas)

media = soma / len(notas)

if media >= 70:
    print(nome , "esta passado")
elif media <= 60:
    print("vocé esta em recuperaçao.")