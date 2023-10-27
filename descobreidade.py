import tkinter as tk
from datetime import datetime

def calcular_idade():
    data_nascimento = entrada_data.get()
    ano_atual = int(entrada_ano.get())
    
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    ano_nascimento = data_nascimento.year
    
    idade = ano_atual - ano_nascimento
    
    resultado_label.config(text=f"Sua idade é: {idade} anos")

# Cria a janela
janela = tk.Tk()
janela.title("Calculadora de Idade")

# Cria os widgets (rótulos, entradas e botão)
rotulo_data = tk.Label(janela, text="Data de Nascimento (dd/mm/aaaa):")
entrada_data = tk.Entry(janela)
rotulo_ano = tk.Label(janela, text="Ano Atual:")
entrada_ano = tk.Entry(janela)
calcular_button = tk.Button(janela, text="Calcular Idade", command=calcular_idade)
resultado_label = tk.Label(janela, text="Sua idade é:")

# Posiciona os widgets na janela
rotulo_data.pack()
entrada_data.pack()
rotulo_ano.pack()
entrada_ano.pack()
calcular_button.pack()
resultado_label.pack()

# Inicia a janela
janela.mainloop()
