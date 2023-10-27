import numpy as np
import matplotlib.pyplot as plt

# Defina os parâmetros da distribuição normal
media = 20
desvio_padrao = 2

# Gere 1000 pontos seguindo a distribuição normal
dados = np.random.normal(media, desvio_padrao, 1000)

# Crie o histograma
plt.hist(dados, bins=30, density=True, alpha=0.6, color='b')

# Adicione rótulos e um título ao gráfico
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Histograma da Distribuição Normal')

# Mostre o gráfico
plt.show()