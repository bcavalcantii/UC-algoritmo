distancia_percorrida = 450.0
consumo_carro = 8.0
preco_litro = 5.50

litros_consumidos = distancia_percorrida / consumo_carro

custo_total = litros_consumidos * preco_litro

print("Distância percorrida:", distancia_percorrida, "km")
print("Consumo do carro:", consumo_carro, "km/l")
print("Preço do litro de gasolina: R$", preco_litro)
print("Litros consumidos:", litros_consumidos, "litros")
print("Custo total de combustível: R$", custo_total)