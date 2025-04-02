# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.km = 0

    def incrementarKm(self, km_percorridos):
        self.km += km_percorridos

    def mostrarDados(self):
        print("******************************")
        print(f'Modelo: {self.modelo}')
        print(f'Ano de lançamento: {self.ano}')
        print(f'Quilometragem: {self.km} km')
        print("******************************")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    carro1 = Carro("Toyota Corolla", 2000)
    carro1.mostrarDados()

    # Incrementando a quilometragem
    carro1.incrementarKm(150)
    carro1.mostrarDados()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
