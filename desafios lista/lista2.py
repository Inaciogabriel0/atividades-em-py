frase = "Python é incrível"
palavras = frase.split()  
palavras_invertidas = list(reversed(palavras)) 
frase_invertida = " ".join(palavras_invertidas)
print(frase_invertida)