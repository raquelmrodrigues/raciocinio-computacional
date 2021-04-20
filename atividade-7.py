"""
Exercício de listas em Pyhton:
Um professor solicitou um programa para saber a maior e menor nota em uma turma de 10 alunos.
As notas de 0 a 10 serão digitadas pelo teclado, verificadas e, ao final, os valores da maior e menor nota deverão
aparecer na tela do computador.
"""
notas = []

def lista_notas(notas):
    nota = int(input('digite a nota: '))
    notas.append(nota)

while len(notas) < 10:
    lista_notas(notas)
    print(notas)

menor = 10
maior = 0

for i in range(len(notas)):
     if maior < notas[i]:
         maior = notas[i]
     if menor > notas[i]:
         menor = notas[i]
     print('A maior nota é:', maior)

print(f'a maior nota da turma foi {menor} e a menor nota da turma foi {maior}')