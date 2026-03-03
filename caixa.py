senha_correta = "123456"
tentativas = 3

while tentativas > 0:
    senha = input("Digite sua senha: ")
    
    if senha == senha_correta:
        print("Olá, Beatriz. Seja bem-vindo ao nosso banco!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta! Você ainda tem {tentativas} tentativa(s).")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")