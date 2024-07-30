def circulo(raio):
    area = 3.14 * (raio ** 2)  # Usar ** para exponenciação
    print(f"A área do círculo é {area}")

def quadrado(aresta):
    area = aresta ** 2  # A área é lado^2, não lado*4
    print(f"A área do quadrado é {area}")

def triangulo(base, altura):
    area = (base * altura) / 2  # Área do triângulo é (base * altura) / 2
    print(f"A área do triângulo é {area}")

def areas():
    print('Escolha qual área você deseja calcular.')
    area = int(input('(1) Círculo\n(2) Quadrado\n(3) Triângulo\n'))
    
    if area == 1:
        raio = float(input('Qual o raio do círculo? '))
        circulo(raio)
    elif area == 2:
        aresta = float(input('Qual o tamanho da aresta do quadrado? '))
        quadrado(aresta)
    elif area == 3:
        base = float(input('Qual o tamanho da base do triângulo? '))
        altura = float(input('Qual o tamanho da altura do triângulo? '))
        triangulo(base, altura)
    else:
        print('Valor inválido.')

while True:  # While loop infinito até que decidamos parar o programa
    areas()
    continuar = input("Você deseja calcular outra área? (s/n): ")
    if continuar.lower() != 's':
        break