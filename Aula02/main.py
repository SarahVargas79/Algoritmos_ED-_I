from Pessoa import Pessoa
from Produto import Produto
from Pedido import Pedido
from Cidade import Cidade

c1 = Cidade()
c2 = Cidade("Porto Alegre")

p1 = Pessoa("Pedro")
p2 = Pessoa("Agatha", cid=c1)

prod01 = Produto("Coca-cola", 9.99)
prod02 = Produto("Pepsi", qtd=50)
prod03 = Produto("Splite", 12.50, 30)

ped = Pedido(cli=p2)
ped.addProd(prod02)
ped.addProd(prod03)

print(ped)
