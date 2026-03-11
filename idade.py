idade_str = input("Digite a idade do atleta: ")
idade = int(idade_str)

if idade < 12:
    categoria = "Infantil"
elif idade >= 12 and idade < 18:
    categoria = "Juvenil"
elif idade >= 18 and idade < 60:
    categoria = "Adulto"
else:
    categoria = "Sênior"

print(f"O atleta tem {idade} anos e pertence à categoria {categoria}.")
print(f"Bem-vindo(a) à competição, categoria {categoria}!")
