# Programa de cálculo de média de notas
# Autor: Fernando José Santiago

#Entrada
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#Processamento

media = (nota1 + nota2)/2   #calcula da média

# Saída
print(f"\nAluno: {nome}") # mostra o nome do aluno
print(f"Média: {media}")  # mostra a média de notas do aluno

if media > 6:
    print("Situação: Aprovado")

else:
    print("Sitação: Reprovado")