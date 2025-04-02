class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.__kilometragem = 0

    def incremetar(self, km):
        if km > 0:
            self.__kilometragem = km

    def setKM(self, km):
        if km > self.__kilometragem:
            self._kilometragem = km

    def __str__(self):
        txt = "Modelo" + self.modelo
        txt += "\nAno" + str(self.ano)
        txt += "\nKilometragem: " + str(self.__kilometragem)
        return txt

x = Carro("Doblo", 2025)
print(x)
