palavras = ["azul", "verde", "amarelo", "vermelho"]
if len(palavras) >= 2:
    palavras[0], palavras[-1] = palavras[-1], palavras[0]

print(palavras)
