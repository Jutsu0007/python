#veiculo.py

class Veiculo:

    def __init__(self, marca, modelo,ano):
       self.marca = marca
       self.modelo = modelo
       self.ano = ano
    #funçoes no padrao __xxx__ sao chamadas funçoes builtin
    def __str__(self):
        return f'Marca: {self.marca} \nModelo: {self.modelo} \nAno: {self.ano}'        
    
    def ligar(self):
        
        print('Veiculo ligando...')

    def desligar(self):
        print('veiculo desligado...')

    def abastecer(self):
        print('Veiculo abastecendo...')

    def acelerar(self):
        print('veiculo acelerando...vrum..vrum...')

class Carro(Veiculo):
     def __init__(self, marca, modelo, placa,ano):
       self.marca = marca
       self.modelo = modelo
       self.placa = placa
       self.ano = ano

class Motocicleta(Veiculo):
     def __init__(self, marca, modelo, placa, ano, cilindrada):
       self.marca = marca
       self.modelo = modelo
       self.placa = placa
       self.ano = ano
       self.cilindrada = cilindrada
    
       
    


if __name__=='__main__':
    #gol = Veiculo('VW', 'Gol','bcd 4567',2019)
    gol = Carro('VW', 'Gol','bcd 4567',2019)
    gol.ligar()
    gol.desligar()
    gol.abastecer()
    gol.acelerar()
    print(gol)
    print('Placa: ' + gol.placa)

    moto = Motocicleta('Honda', 'CG 160 Titan','XYZ-4321',2021, 600)
    print(moto)
    print('Placa: '+ gol.placa)
