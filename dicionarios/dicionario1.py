dicionario =  {
    "Nome": "joao\ndavi",
    "telefone": "28827584\n839857485",
    "email": "joaocomecu255@gmail.com\ndavicomeuvocé@gmail.com"
}
nomes = dicionario["Nome"].split("\n")
telefones = dicionario["telefone"].split("\n")
emails = dicionario["email"].split("\n")

print("seu primeiro amigo  é:", nomes[0])
print("seu segundo amigo é:", nomes[1])
print("o numero de telefone do seu primeiro amigo é:", telefones[0])
print("onumero de telefone do seu segundo amigo é:", telefones[1])
print("o email do seu primeiro amigo é:", emails[0])
print("o email do seu primeiro amigo é:", emails[1])