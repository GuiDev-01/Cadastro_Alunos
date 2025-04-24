import json
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Arquivo onde os dados serão salvos
ARQUIVO = "alunos.json"

# Lista de alunos (carregada do arquivo se existir)
alunos = []
if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r") as f:
        alunos = json.load(f)

# Função para salvar no arquivo JSON
def salvar_dados():
    with open(ARQUIVO, "w") as f:
        json.dump(alunos, f, indent=4)

# Função para cadastrar um aluno
def cadastrar_aluno():
    nome = nome_entry.get().strip().casefold()
    try:
        nota1 = float(nota1_entry.get())
        nota2 = float(nota2_entry.get())
        media = (nota1 + nota2) / 2
        aluno = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "media": media
        }
        alunos.append(aluno)
        salvar_dados()
        messagebox.showinfo("Cadastro", f'Aluno {nome.capitalize()} cadastrado com sucesso!')
        nome_entry.delete(0, 'end')
        nota1_entry.delete(0, 'end')
        nota2_entry.delete(0, 'end')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para as notas.")

# Função para exibir o boletim de um aluno
def ver_boletim():
    nome = boletim_entry.get().strip().casefold()
    for aluno in alunos:
        if aluno["nome"] == nome:
            messagebox.showinfo("Boletim", f'A média final de {aluno["nome"].capitalize()} foi: {aluno["media"]}')
            return
    messagebox.showerror("Erro", "Aluno não encontrado.")

# Função para exibir as notas de um aluno
def ver_notas():
    nome = notas_entry.get().strip().casefold()
    for aluno in alunos:
        if aluno["nome"] == nome:
            messagebox.showinfo("Notas", f'As notas de {aluno["nome"].capitalize()} foram {aluno["nota1"]} e {aluno["nota2"]}')
            return
    messagebox.showerror("Erro", "Aluno não encontrado.")

def ver_lista_alunos():
    if not alunos:
        messagebox.showinfo("Lista de Alunos", "Nenhum aluno cadastrado.")
        return

    lista = ""
    for i, aluno in enumerate(alunos, start=1):
        lista += f"{i}. {aluno['nome'].capitalize()} - Nota 1: {aluno['nota1']}, Nota 2: {aluno['nota2']}, Média: {aluno['media']:.2f}\n"

    messagebox.showinfo("Lista de Alunos", lista)

def limpar_lista_alunos():
    if not alunos:
        messagebox.showinfo("Limpar Lista", "A lista já está vazia.")
        return

    confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja apagar todos os alunos?")
    if confirmacao:
        alunos.clear()
        messagebox.showinfo("Limpar Lista", "Lista de alunos apagada com sucesso!")

# Função para sair
def sair():
    root.quit()

# Criando a janela principal
root = ttk.Window(themename="darkly")
root.title("Cadastro de Alunos")
root.geometry('800x800')

# Definindo os componentes da interface gráfica
ttk.Label(root, text="Cadastro de Alunos", font=("Arial", 16), bootstyle=INFO).pack(pady=10)

# Tela de cadastro de aluno
ttk.Label(root, text="Nome do aluno:").pack(pady=5)
nome_entry = ttk.Entry(root, bootstyle=SUCCESS)
nome_entry.pack(pady=5)

ttk.Label(root, text="Primeira Nota:").pack(pady=5)
nota1_entry = ttk.Entry(root, bootstyle=SUCCESS)
nota1_entry.pack(pady=5)

ttk.Label(root, text="Segunda Nota:").pack(pady=5)
nota2_entry = ttk.Entry(root, bootstyle=SUCCESS)
nota2_entry.pack(pady=5)

cadastrar_button = ttk.Button(root, text="Cadastrar Aluno", bootstyle=PRIMARY, command=cadastrar_aluno)
cadastrar_button.pack(pady=10)

# Tela de ver boletim
ttk.Label(root, text="Ver Boletim de um Aluno:").pack(pady=5)
boletim_entry = ttk.Entry(root, bootstyle=SUCCESS)
boletim_entry.pack(pady=5)

boletim_button = ttk.Button(root, text="Ver Boletim", bootstyle=INFO, command=ver_boletim)
boletim_button.pack(pady=10)

# Tela de ver notas
ttk.Label(root, text="Ver Notas Individuais de um Aluno:").pack(pady=5)
notas_entry = ttk.Entry(root, bootstyle=SUCCESS)
notas_entry.pack(pady=5)

notas_button = ttk.Button(root, text="Ver Notas", bootstyle=INFO, command=ver_notas)
notas_button.pack(pady=10)

#Botão para ver a lista de alunos cadastrados
lista_button = ttk.Button(root, text="Ver Lista de Alunos", bootstyle=SECONDARY, command=ver_lista_alunos)
lista_button.pack(pady=10)

#Botão para limpar a lista de alunos cadastrados
limpar_button = ttk.Button(root, text="Limpar Lista de Alunos", bootstyle=WARNING, command=limpar_lista_alunos)
limpar_button.pack(pady=10)

# Botão para sair
sair_button = ttk.Button(root, text="Sair", bootstyle=DANGER, command=sair)
sair_button.pack(pady=20)

# Iniciar a interface gráfica
root.mainloop()
