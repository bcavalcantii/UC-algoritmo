nome = input("Digite o nome completo do aluno: ")

matricula_str = input("Digite a matrícula do aluno: ")
matricula = int(matricula_str)

nota1_str = input("Digite a primeira nota: ")
nota1 = float(nota1_str)
nota2_str = input("Digite a segunda nota: ")
nota2 = float(nota2_str)

media = (nota1 + nota2) / 2

print("\n===== RELATÓRIO DO ALUNO =====")
print(f"Nome: {nome}")
print(f"Matrícula: {matricula}")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Média: {media:.2f}")
print("==============================")