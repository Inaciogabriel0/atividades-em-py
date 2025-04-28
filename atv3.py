altura = 2.00

peso = 90

calculo = altura * altura 

calculo2 = peso / calculo

if calculo2 < 18.5:
    print("voce esta abaixo do peso ideal.")
elif calculo2 > 18.5 and calculo2 < 24.9:
    print("vocé esta no peso ideal.")
elif calculo2 > 25 and calculo2 < 29.9:
    print("vocé esta acima do peso")
elif calculo2 > 30:
    print("vocé esta obeso.")           


