import random 

def jogar_adivinhaçao():
    secret = random.randint(1,100)
    tries = 0

    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.\n")

    while True:
        try:
            guess = int(input("manda um palpitew: "))
        except ValueError:
            print("Por favor, digite um número inteiro.\n")
            continue 

        tries += 1

        if guess > secret:
            print("Tente um número mais baixo! 🤏\n")
        elif guess < secret:
            print("Tente um número mais alto! 🆙\n")
        else:
            print("🎉 Acertou em {tries} tentativas! O número era {secret}.")   
            break
                     
if __name__ == "__main__":
    jogar_adivinhaçao()         


            