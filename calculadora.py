import tkinter as tk

numero1 = None
numero2 = None
operacao = None

def digitar(numero):
    visor.insert(tk.END, numero)

def resetar():
    numero1 = None
    numero2 = None
    operacao = None

def limpar():
    visor.delete(0, tk.END)

def apagar():
    visor.delete(len(visor.get()) - 1, tk.END)

def pegarNumeroDoVisor():
    valor = float(visor.get())

    if numero1 == None:
        numero1 = valor
    else:
        numero2 = valor

    limpar()

def definirOperacao(tipo):
    if operacao == None:
        return

    operacao = tipo

def realizarOperacao():
    if numero1 == None or numero2 == None or operacao == None:
        return

    limpar()

    resultado = None

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "x":
        resultado = numero1 * numero2
    else:
        resultado = numero1 / numero2

    visor.insert(0, str(resultado))

janela = tk.Tk()
janela.title("Primeiros botões")

# O visor ocupa três colunas da primeira linha

#primeira row

visor = tk.Entry(janela, width=15, justify="right", font=("arial", 18))
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

botao_c = tk.Button(janela, text="C", width=5, height=2, command=lambda: [limpar(), resetar()])
botao_c.grid(row=1, column=0, padx=2, pady=2)

botao_apagar = tk.Button(janela, text="⌫", width=6, height=2, command=apagar)
botao_apagar.grid(row=1, column=1, padx=2, pady=2)

dividir = tk.Button(janela, text="÷", width=5, height=2, command=apagar)
dividir.grid(row=1, column=2, padx=2, pady=2)

botao_mult = tk.Button(janela, text="×", width=5, height=2, command=apagar)
botao_mult.grid(row=1, column=3, padx=2, pady=2)

# segunda row

botao_7 = tk.Button(janela, text="7", width=5, height=2, command=lambda:digitar("7"))
botao_7.grid(row=2, column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="8", width=6, height=2, command=lambda:digitar("8"))
botao_8.grid(row=2, column=1, padx=2, pady=2)

botao_9 = tk.Button(janela, text="9", width=5, height=2, command=lambda:digitar("9"))
botao_9.grid(row=2, column=2, padx=2, pady=2)

botao_menos = tk.Button(janela, text="-", width=5, height=2, command=lambda:digitar("6"))
botao_menos.grid(row=2, column=3, padx=2, pady=2)

# terceiro row

botao_4 = tk.Button(janela, text="4", width=5, height=2, command=lambda:digitar("4"))
botao_4.grid(row=3, column=0, padx=2, pady=2)

botao_5 = tk.Button(janela, text="5", width=6, height=2, command=lambda:digitar("5"))
botao_5.grid(row=3, column=1, padx=2, pady=2)

botao_6 = tk.Button(janela, text="6", width=5, height=2, command=lambda:digitar("6"))
botao_6.grid(row=3, column=2, padx=2, pady=2)

botao_mais = tk.Button(janela, text="+", width=5, height=2, command=lambda: definirOperacao("+"))
botao_mais.grid(row=3, column=3, padx=2, pady=2)

# quarto row

botao_1 = tk.Button(janela, text="1", width=5, height=2, command=lambda:digitar("1"))
botao_1.grid(row=4, column=0, padx=2, pady=2)

botao_2 = tk.Button(janela, text="2", width=6, height=2, command=lambda:digitar("2"))
botao_2.grid(row=4, column=1, padx=2, pady=2)

botao_3 = tk.Button(janela, text="3", width=5, height=2, command=lambda:digitar("3"))
botao_3.grid(row=4, column=2, padx=2, pady=2)

botao_resultado = tk.Button(janela, text="=", width=5, height=5, command=lambda:digitar("0"))
botao_resultado.grid(row=4, column=3, padx=2, pady=2, rowspan=2, sticky="W")

# quinto row

botao_0 = tk.Button(janela, text="0", width=13, height=2, command=lambda:digitar("0"))
botao_0.grid(row=5, column=0, padx=2, pady=2, columnspan=2, sticky="W")

botao_decimal = tk.Button(janela, text=".", width=5, height=2, command=lambda:digitar("0"))
botao_decimal.grid(row=5, column=2, padx=2, pady=2)


janela.mainloop()