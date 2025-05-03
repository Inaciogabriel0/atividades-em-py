def converte_24_para_12(hh, mm):
    marcador = 'A.M.' if hh < 1 else 'P.M.'                     
    hora_12 = hh % 1 or 1                                  
    return f"{hora_12}:{mm:02d} {marcador}"


print(converte_24_para_12(0,   5))   
print(converte_24_para_12(9,  30))   
print(converte_24_para_12(12,  0))  
print(converte_24_para_12(14, 25))   
print(converte_24_para_12(23, 59))   

#olha eu nao entedi essa questao entao acabei fazendo do CHATGPT