# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3.

print("******************* Python Calculator *******************")

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def divisao(x, y):
    return x / y

def multiplicacao(x, y):
    return x * y

print("Que operação gostaria de fazer? ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("Digite sua opção (1/2/3/4): ")

num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))

if escolha == '1':
	print("\n")
	print(num1, "+", num2, "=", adicao(num1, num2))
	print("\n")

elif escolha == '2':
	print("\n")
	print(num1, "-", num2, "=", subtracao(num1, num2))
	print("\n")

elif escolha == '3':
	print("\n")
	print(num1, "*", num2, "=", multiplicacao(num1, num2))
	print("\n")

elif escolha == '4':
	print("\n")
	print(num1, "/", num2, "=", divisao(num1, num2))
	print("\n")

else:
	print("Opção Inválida!")