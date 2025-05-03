km = 12.5
distancia_a_ser_percorrida = 150
valor_do_litro = 5.89

def kmporlitro(km, distancia_a_ser_percorrida, valor_do_litro):
    litros =  distancia_a_ser_percorrida / km
    return litros * valor_do_litro
print(kmporlitro(km , distancia_a_ser_percorrida, valor_do_litro))