import tkinter as tk
from tkinter import messagebox

# Função para exibir o resultado com base na escolha
def exibir_resultado(escolha):
    if escolha == "sim":
        resultado_label.config(text="Conhecss")
    elif escolha == "não":
        resultado_label.config(text="FRESCO É GALADO")

# Criar a janela principal
janela = tk.Tk()
janela.title("Pergunta Importante")

# Pergunta
pergunta_label = tk.Label(janela, text="Você é fresco ou chupa bila?", font=("Helvetica", 12))
pergunta_label.pack(pady=20)

# Botão "sou sim"
botao_sim = tk.Button(janela, text="Sou sim", command=lambda: exibir_resultado("sim"))
botao_sim.pack()

# Botão "sou não"
botao_nao = tk.Button(janela, text="Sou não", command=lambda: exibir_resultado("não"))
botao_nao.pack()

# Label para exibir o resultado
resultado_label = tk.Label(janela, text="", font=("Helvetica", 14))
resultado_label.pack(pady=20)

# Iniciar a janela
janela.mainloop()