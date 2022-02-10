# Composição

# Quando uma classe compõe ou é composta pela outra


class Item:

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Mapa(Item):
    pass


class PocaoMagica(Item):
    pass

class Mochila:

    def __init__(self):
        self._itens = []

    def adicionar(self, item):
        if item in self._itens:
            print("O item já está na mochila!")

        elif len(self._itens) == 5:
            print("A mochila já está cheia!")
        else:
            self._itens.append(item)

    def remover(self, item):
        self._itens.remove(item)

    def listar_itens(self):
        print("ITENS NA MOCHILA")
        for item in self._itens:
            print(f"* {item.nome}")

        print('-'*50)


if __name__ == '__main__':

    mochila = Mochila()
    mochila.listar_itens()

    pocao_de_mana_01 = PocaoMagica('Poção de Mana')
    pocao_de_mana_02 = PocaoMagica('Poção de Mana')
    pocao_de_energia_01 = PocaoMagica('Poção de Energia')
    pocao_de_energia_02 = PocaoMagica('Poção de Energia')
    mapa = Mapa('Mapa')

    mochila.adicionar(pocao_de_mana_01)
    mochila.adicionar(pocao_de_mana_02)
    mochila.adicionar(pocao_de_energia_01)
    mochila.adicionar(pocao_de_energia_02)
    mochila.adicionar(mapa)

    mochila.listar_itens()

    # mochila.remover(pocao_de_mana_02)

    mochila.listar_itens()

    mochila.adicionar(pocao_de_mana_02)
    mochila.adicionar(pocao_de_mana_02)