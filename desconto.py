valor_str = input("Digite o valor da compra: R$ ")
valor_compra = float(valor_str)

if valor_compra < 100:
    desconto_percentual = 0
elif valor_compra >= 100 and valor_compra < 500:
    desconto_percentual = 5
elif valor_compra >= 500 and valor_compra < 1000:
    desconto_percentual = 10
else:
    desconto_percentual = 15

desconto = valor_compra * (desconto_percentual / 100)
valor_final = valor_compra - desconto

print("\n===== RELATÓRIO DE COMPRA =====")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto_percentual}% (R$ {desconto:.2f})")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
print("===============================")
