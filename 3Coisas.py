# Primeiro
def media (n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    print (f"Sua média foi de {media}")

nota1 = int(input("Digite sua nota 1:"))
nota2 = int(input("Digite sua nota 2:"))
nota3 = int(input("Digite sua nota 3:"))
media(nota1, nota2, nota3,)

#Segundo
numerosPares = [0,2,4,6,8]

numEscolhido = int(input("Digite um valor."))
ultimoNum = numEscolhido % 10
print (ultimoNum)
if ultimoNum in numerosPares:
    print("Par")
else:
    print("Impar")

#Terceiro
def soma (n1,n2):
    resultado = n1 + n2
    print (f"O Resultado da conta é {resultado}")
def subtracao (n1,n2):
    resultado = n1 - n2
    print (f"O Resultado da conta é {resultado}")
def multiplicacao (n1,n2):
    resultado = n1 * n2
    print (f"O Resultado da conta é {resultado}")
def divisao (n1,n2):
    resultado = n1 / n2
    print (f"O Resultado da conta é {resultado}")

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))
operacao = input("Digite a operacao")

if operacao == "+":
    soma(num1,num2)
elif operacao == "-":
    subtracao(num1,num2)
elif operacao == "*":
    multiplicacao(num1,num2)
elif operacao == "/":
    divisao(num1,num2)