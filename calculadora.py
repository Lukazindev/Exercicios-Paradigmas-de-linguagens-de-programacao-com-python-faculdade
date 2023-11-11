import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        
        # Adiciona um estilo ao tema
        style = ThemedStyle(self.root)
        style.set_theme("radiance")

        # Variável para armazenar a expressão
        self.expression = tk.StringVar()

        # Entry para mostrar a expressão
        entry = ttk.Entry(self.root, textvariable=self.expression, font=('Helvetica', 18), justify='right', state='disabled')
        entry.grid(row=0, column=0, columnspan=4, ipady=10, sticky='news')

        # Botões
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(self.root, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky='news')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configuração das células para expandir com a janela
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        current_expression = self.expression.get()

        if button == 'C':
            # Limpa a expressão
            self.expression.set('')
        elif button == '=':
            try:
                # Avalia a expressão e exibe o resultado
                result = str(eval(current_expression))
                self.expression.set(result)
            except Exception as e:
                # Se houver um erro na expressão, exibe uma mensagem de erro
                self.expression.set('Erro')
        else:
            # Adiciona o botão clicado à expressão
            self.expression.set(current_expression + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
