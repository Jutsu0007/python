#marvel.py


class Heroi:

    def __init__(self, nome):
        self.nome=nome

    def voar(self):
        print(f'{self.nome} voando...')

    def levantarPeso(self):
        print(f'{self.nome} levantando um caminhao...')

    def destruir(self):
        print(f'{self.nome} destruindo armas do inimigo...')

    def salvar(self):
        print(f'{self.nome} salvando pessoas...')

#Thor É UM Heroi
class Thor(Heroi):
    def __init__(self):
        super().__init__('Thor')

    def jogarMartelo(self):
        print('Thor jogando martelo...')


class Ironman(Heroi):
    def __init__(self):
        super().__init__('Ironman')

    def explodirInimigo(self):
        print('Ironman explodindo inimigo...')

class CapitaoAmerica(Heroi):
    def __init__(self):
        super().__init__('CapitaoAmerica')

    def pegarEscudo(self):
        print('Pegar escudo...')
        
thor=Thor()
thor.voar()
thor.levantarPeso()
thor.destruir()
thor.salvar()

ironman=Ironman()
ironman.voar()
ironman.explodirInimigo()

capitaoAmerica=CapitaoAmerica()
capitaoAmerica.pegarEscudo()
