import matplotlib.pyplot as plt

# Dados de exemplo: nomes dos produtos e suas respectivas vendas
produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]
vendas = [100, 80, 120, 90]

# Criar um gráfico de barras
plt.bar(produtos, vendas)

# Adicionar rótulos e título ao gráfico
plt.xlabel("Produtos")
plt.ylabel("Vendas")
plt.title("Vendas de Produtos")

# Mostrar o gráfico
plt.show()