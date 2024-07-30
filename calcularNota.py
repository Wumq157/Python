listaMateria = []

def adicionar_nota(nota):
    listaMateria.append(nota)
    print(f"Nota {nota} adicionada com sucesso.")

def calcular_media():
    if len(listaMateria) == 0:
        print("Não há notas na lista para calcular a média.")
        return

    media = sum(listaMateria) / len(listaMateria)
    print(f"A média das notas é: {media}")

while True:
    opcao = input("Digite 'a' para adicionar uma nota, 'm' para calcular a média ou 's' para sair: ").strip().lower()
    
    if opcao == 'a':
        try:
            nota = float(input("Digite a nota a ser adicionada: "))
            adicionar_nota(nota)
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
    
    elif opcao == 'm':
        calcular_media()
    
    elif opcao == 's':
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")