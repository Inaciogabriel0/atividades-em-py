class Carro:
    def __init__(self):
        self.motor_ligado = False

    def ligar_motor(self):
        if not self.motor_ligado:
            self.motor_ligado = True
            print("Carro ligado.")
        else:
            print("O carro já está ligado.")

    def desligar_motor(self):
        if self.motor_ligado:
            self.motor_ligado = False
            print("Carro desligado.")
        else:
            print("O carro já está desligado.")


carro = Carro()
carro.ligar_motor()
carro.ligar_motor()
carro.desligar_motor()
carro.desligar_motor()