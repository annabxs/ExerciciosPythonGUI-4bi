import tkinter as tk
from tkinter import messagebox

clientes = []

def limpar():
    entrada_nome.delete(0, tk.END)
    entrada_cpf.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_cidade.delete(0, tk.END)

    entrada_nome.focus()

def salvar():
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()
    cidade = entrada_cidade.get()

    if nome == "":
        messagebox.showwarning(
            "Atenção",
            "Informe o nome."
        )
        return

    if cpf == "":
        messagebox.showwarning(
            "Atenção",
            "Informe o cpf."
        )    
        return

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "cidade": cidade,
    }

    clientes.append(cliente)

    messagebox.showinfo(
        "Sucesso",
        "Cliente cadastrado com sucesso!"
    )

# JANELA PRINCIPAL

janela = tk.Tk()

janela.title("Cadastro de Clientes")
janela.geometry("550x500")

titulo = tk.Label(
    janela,
    text="CADASTRO DE CLIENTES",
    font=("Arial", 16, "bold")
)
titulo.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=20
)

# CAMPOS

tk.Label(
    janela,
    text="Nome:"
).grid(row=1, column=0, padx=10, pady=5)

entrada_nome = tk.Entry(
    janela,
    width = 40
)
entrada_nome.grid(
    row = 1,
    column = 1,
    padx = 10,
    pady = 5
)

tk.Label(
    janela,
    text="CPF: "
) .grid(row=2, column=0, padx=10, pady=5)

entrada_cpf= tk.Entry(
    janela,
    width=40
)

entrada_cpf.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)

tk.Label(
    janela,
    text="Telefone: "
) .grid(row=3, column=0, padx=10, pady=5)

entrada_telefone = tk.Entry(
    janela,
    width=40
)

entrada_telefone.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)

tk.Label(
    janela,
    text="Email: "
) .grid(row=4, column=0, padx=10, pady=5)

entrada_email = tk.Entry(
    janela,
    width=40
)

entrada_email.grid(
    row=4,
    column=1,
    padx=10,
    pady=5
)


tk.Label(
    janela,
    text="Cidade: "
) .grid(row=5, column=0, padx=10, pady=5)

entrada_cidade = tk.Entry(
    janela,
    width=40
)

entrada_cidade.grid(
    row=5,
    column=1,
    padx=10,
    pady=5
)

# Botões:

btn_limpar = tk.Button(
    janela,
    text="Limpar",
    width=12,
    command=limpar
)

btn_limpar.grid(
    row=6,
    column=0,
    pady=15
)

btn_salvar = tk.Button(
    janela,
    text="Salvar",
    width=12,
    command=salvar
)

btn_salvar.grid(
    row=6,
    column=1,
    pady=15
)


#Lista:

tk.Label(
    janela,
    text="Clientes cadastrados: "
) .grid(
    row=7,
    column=0,
    columnspan=2
)

lista_clientes = tk.Listbox(
    janela,
    width=60,
    height=8
)

lista_clientes.grid(
    row=8,
    column=0,
    columnspan=2,
    padx=10,
    pady=10
)


#Execução:

entrada_nome.focus()
janela.mainloop()