import tkinter as tk
import funcoes  # Importar o arquivo funcoes.py

def calcular():
    # Obter os números inseridos nos campos de entrada
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    
    # Verificar qual operação foi selecionada
    operacao = opcoes_operacao.get()
    
    # Realizar a operação apropriada com base na seleção
    if operacao == "Soma":
        resultado = funcoes.somar(num1, num2)
    elif operacao == "Subtração":
        resultado = funcoes.subtrair(num1, num2)
    elif operacao == "Multiplicação":
        resultado = funcoes.multiplicar(num1, num2)
    elif operacao == "Divisão":
        resultado = funcoes.dividir(num1, num2)
    
    # Exibir o resultado na área de texto
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, resultado)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Criar campos de entrada para números
entrada_num1 = tk.Entry(janela, width=10)
entrada_num1.pack(side=tk.LEFT, padx=5)

entrada_num2 = tk.Entry(janela, width=10)
entrada_num2.pack(side=tk.LEFT, padx=5)

# Criar uma lista de opções para as operações
opcoes_operacao = tk.StringVar(janela)
opcoes_operacao.set("Soma")  # Valor padrão
menu_operacao = tk.OptionMenu(janela, opcoes_operacao, "Soma", "Subtração", "Multiplicação", "Divisão")
menu_operacao.pack(side=tk.LEFT)

# Criar um botão para calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.pack(side=tk.LEFT)

# Criar uma área de texto para mostrar o resultado
texto_resultado = tk.Text(janela, height=1, width=20)
texto_resultado.pack(side=tk.LEFT)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
