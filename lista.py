def mostrarLista(lista):
    print("Lista atual:", lista)

def main():
    lista = []

    while True:
        print("==============================================")
        print("\nMenu:")
        print("1. Inserir novo item na lista")
        print("2. Excluir item da lista")
        print("3. Mostrar lista atual")
        print("4. Sair")
        print("==============================================")
        print("")
        print("----===+===----")
        escolha = input("Escolha uma opção: ")
        print("")

        if escolha == '1':
            novo_item = input("Digite o novo item: ")
            lista.append(novo_item)
            print("----===+===----")
            print("Item adicionado à lista.")
            print("")
            mostrarLista(lista)
        elif escolha == '2':
            if lista:
                itemExcluir = input("Digite o item que deseja excluir: ")
                if itemExcluir in lista:
                    lista.remove(itemExcluir)
                    print("----===+===----")
                    print("Item removido da lista.")
                    print("")
                    mostrarLista(lista)
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
