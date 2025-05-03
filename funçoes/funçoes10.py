def valorPagamento(valor, dias):
    return valor if dias <= 0 else valor * 1.03 + valor * 0.001 * dias

total = 0.0
count = 0

while True:
    v = float(input("Prestação (0 sai): "))  
    if v == 0:
        break
    d = int(input("Dias de atraso: "))        
    p = valorPagamento(v, d)                
    print(f"R$ {p:.2f}")                     
    total += p
    count += 1

print(f"\nTotal de prestações: {count}")
print(f"Valor total pago: R$ {total:.2f}")
