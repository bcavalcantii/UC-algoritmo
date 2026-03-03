usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

login1_usuario = "procopio"
login1_senha = "12345"

login2_usuario = "paiva"
login2_senha = "54321"

if (usuario == login1_usuario and senha == login1_senha) or \
   (usuario == login2_usuario and senha == login2_senha):
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem")