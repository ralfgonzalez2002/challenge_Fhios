'''Proponer una representación con tuplas para las cartas de la baraja francesa.'''

class Carta:

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def __str__(self):
        return "[{}-{}]".format(self.valor, self.pinta)

class Baraja:

    def __init__(self):
        pintas = ["\u2660", "\u2665", "\u2666", "\u2663"]
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.pila = []
        for i in pintas:
            for j in valores:
                carta = Carta(j, i)
                self.pila.append(carta)
        self.pila = tuple(self.pila)



    def mostrar_baraja (self):
        for carta in self.pila:
            print (carta)
        print("Este mazo posee {} cartas.".format(len(self.pila)))




Baraja().mostrar_baraja()