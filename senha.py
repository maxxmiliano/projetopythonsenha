import tkinter as tk
from tkinter import messagebox
import re

def verificar_forca_senha(senha):
    # Verifica o comprimento da senha
    if len(senha) < 8:
        return "Fraca (mínimo de 8 caracteres)"
    
    # Verifica se a senha contém números
    if not re.search(r'\d', senha):
        return "Fraca (deve conter números)"
    
    # Verifica se a senha contém letras maiúsculas e minúsculas
    if not re.search(r'[a-z]', senha) or not re.search(r'[A-Z]', senha):
        return "Fraca (deve conter letras maiúsculas e minúsculas)"
    
    # Verifica se a senha contém caracteres especiais
    if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~]', senha):
        return "Fraca (deve conter caracteres especiais)"
    
    return "Forte"

def verificar_senha():
    senha = senha_entry.get()
    forca = verificar_forca_senha(senha)
    messagebox.showinfo("Resultado", f"A força da senha é: {forca}")

# Cria uma janela
janela = tk.Tk()
janela.title("Verificador de Força de Senha")

# Rótulo
rotulo = tk.Label(janela, text="Digite sua senha:")
rotulo.pack()

# Entrada de senha
senha_entry = tk.Entry(janela, show="*")  # Mostra asteriscos no lugar da senha
senha_entry.pack()

# Botão para verificar senha
verificar_botao = tk.Button(janela, text="Verificar Senha", command=verificar_senha)
verificar_botao.pack()

# Inicia o loop da janela
janela.mainloop()
