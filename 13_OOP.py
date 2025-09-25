class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'O Carro{self.modelo} acelerou para {self.velocidade} Km/h.') 

    def desacelerar(self, freio):
        while self.velocidade > 0:
         self.velocidade -= freio
         print(f'O Carro {self.modelo} desacelerou para {self.velocidade} Km/h.')
        print(f'O Carro{self.modelo} parou.')

        
meu_carro = Carro("Fiat","preto")
carro_instrutor = Carro("Bmw",'Preto')
uber =  Carro("Uno", "Branco")

carro_instrutor.acelerar(20)       
carro_instrutor.acelerar(32)
carro_instrutor.desacelerar(1)       
carro_instrutor.acelerar(50)
