import os

def mostrarLista(lista):
    print("Lista atual:", lista)

def gravarLista(vLista):
    nomeArq = input("Qual o nome que você deseja para o arquivo?")
    nomeArq += ".txt"  # Adiciona .txt ao final do nome do arquivo
    with open(nomeArq, "w") as arquivo:
        for item in vLista:
            arquivo.write(item + "\n")
    print(f"Arquivo gravado com sucesso, nome do arquivo: {nomeArq}")

def carregarLista():
    nomeArq = input("Digite o nome do arquivo que deseja carregar: ")
    nomeArq += ".txt"  # Adiciona .txt ao final do nome do arquivo
    lista_carregada = []
    try:
        with open(nomeArq, "r") as arquivo:
            lista_carregada.clear()
            for linha in arquivo:
                lista_carregada.append(linha.strip())  # Remove qualquer espaço em branco adicional
        print(f"Lista carregada com sucesso do arquivo: {nomeArq}")
        return lista_carregada
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []
    except Exception as e:
        print("OCORREU UM ERRO: ", e)
        return
    
def ordenar_lista(lista):
    lista_ordenada = sorted(lista, reverse=True)
    print("Lista ordenada com sucesso:", lista_ordenada)
    return lista_ordenada

def listar_arquivos():
    # Diretório onde estão os arquivos
    diretorio = os.getcwd()  # Obtém o diretório atual

    # Lista para armazenar os nomes dos arquivos .txt
    arquivos_txt = []

    # Percorre todos os arquivos e diretórios dentro do diretório especificado
    for nome_arquivo in os.listdir(diretorio):
        # Verifica se o nome do arquivo termina com .txt
        if nome_arquivo.endswith(".txt"):
            # Se sim, adiciona à lista de arquivos .txt
            arquivos_txt.append(nome_arquivo)
    
    # Retorna a lista de arquivos .txt
    print(arquivos_txt)

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
        print("6. Ordenar Lista")
        print("7. Diretorio.")
        print("8. Sair")
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
        elif escolha == "6":
            lista = ordenar_lista(lista)
        elif escolha == "7":
            listar_arquivos()
        elif escolha == '8':
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
