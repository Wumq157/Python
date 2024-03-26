def mostrarLista(lista):
    print("Lista atual:", lista)

def gravarLista(vLista):
    nomeArq = input("Qual o nome que você deseja para o arquivo?")
    with open(nomeArq, "w") as arquivo:
        for item in vLista:
            arquivo.write(item + "\n")
    print(f"Arquivo gravado com sucesso, nome do arquivo: {nomeArq}")

def carregarLista():
    nomeArq = input("Digite o nome do arquivo que deseja carregar: ")
    lista_carregada = []
    try:
        with open(nomeArq, "r") as arquivo:
            for linha in arquivo:
                lista_carregada.append(linha.strip())  # Remove qualquer espaço em branco adicional
        print(f"Lista carregada com sucesso do arquivo: {nomeArq}")
        return lista_carregada
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []

def main():
    lista = []

    while True:
        print("==============================================")
        print("\nMenu:")
        print("1. Inserir novo item na lista")
        print("2. Excluir item da lista")
        print("3. Mostrar lista atual")
        print("4. Gravar lista")
        print("5. Carregar lista")
        print("6. Sair")
        print("==============================================\n")
        print("----===+===----")
        escolha = input("Escolha uma opção: ")
        print("")

        if escolha == '1':
            novo_item = input("Digite o novo item: ")
            lista.append(novo_item)
            print("----===+===----")
            print("Item adicionado à lista.")
            print("")
        elif escolha == '2':
            if lista:
                itemExcluir = input("Digite o item que deseja excluir: ")
                if itemExcluir in lista:
                    lista.remove(itemExcluir)
                    print("----===+===----")
                    print("Item removido da lista.")
                    print("")
                else:
                    print("----===+===----")
                    print("Item não encontrado na lista.")
                    print("")
            else:
                print("----===+===----")
                print("Lista vazia. Não há itens para excluir.")
                print("")
        elif escolha == '3':
            if lista:
                mostrarLista(lista)
            else:
                print("----===+===----")
                print("Lista vazia.")
                print("")
        elif escolha == '4':
            gravarLista(lista)
        elif escolha == '5':
            lista = carregarLista()
        elif escolha == '6':
            print("----===+===----")
            print("Encerrando o programa.")
            print("")
            break
        else:
            print("----===+===----")
            print("Opção inválida. Tente novamente.")
            print("")

if __name__ == "__main__":
    main()
