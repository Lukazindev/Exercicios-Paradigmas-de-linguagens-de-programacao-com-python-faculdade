import tkinter as tk

def obter_resposta():
    resposta = "perguntoukkkkkkkkkkkkkk"
    resposta_label.config(text=resposta)

# Cria a janela
janela = tk.Tk()
janela.title("Pergunta")
janela.geometry("500x300")

# Cria um rótulo para a pergunta
pergunta_label = tk.Label(janela, text="Quem?")
pergunta_label.pack()

# Cria uma caixa de entrada para que o usuário responda
resposta_entry = tk.Entry(janela)
resposta_entry.pack()

# Cria um botão para obter a resposta
botao_responder = tk.Button(janela, text="Responder", command=obter_resposta)
botao_responder.pack()

# Cria um rótulo para exibir a resposta
resposta_label = tk.Label(janela, text="")
resposta_label.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()
