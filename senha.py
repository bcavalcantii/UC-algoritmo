senha = input("Digite sua senha: ")

tem_oito_caracteres = len(senha) >= 8
tem_numero = any(char.isdigit() for char in senha)

if tem_oito_caracteres and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida")
    print("A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
