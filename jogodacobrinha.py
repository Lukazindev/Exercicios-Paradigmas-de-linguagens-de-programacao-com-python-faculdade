import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Definições
largura, altura = 640, 480
tamanho_bloco = 20
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)

# Configuração da janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Função para desenhar a cobra
def desenhar_cobra(cobra):
    for segmento in cobra:
        pygame.draw.rect(janela, cor_cobra, (segmento[0], segmento[1], tamanho_bloco, tamanho_bloco))

# Função principal do jogo
def jogo_da_cobrinha():
    # Inicialização
    cobra = [(largura // 2, altura // 2)]
    direcao = 'direita'
    comida = (random.randrange(0, largura - tamanho_bloco, tamanho_bloco), random.randrange(0, altura - tamanho_bloco, tamanho_bloco))

    # Loop principal
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != 'baixo':
                    direcao = 'cima'
                elif evento.key == pygame.K_DOWN and direcao != 'cima':
                    direcao = 'baixo'
                elif evento.key == pygame.K_LEFT and direcao != 'direita':
                    direcao = 'esquerda'
                elif evento.key == pygame.K_RIGHT and direcao != 'esquerda':
                    direcao = 'direita'

        # Movimento da cobra
        if direcao == 'cima':
            cobra[0] = (cobra[0][0], cobra[0][1] - tamanho_bloco)
        elif direcao == 'baixo':
            cobra[0] = (cobra[0][0], cobra[0][1] + tamanho_bloco)
        elif direcao == 'esquerda':
            cobra[0] = (cobra[0][0] - tamanho_bloco, cobra[0][1])
        elif direcao == 'direita':
            cobra[0] = (cobra[0][0] + tamanho_bloco, cobra[0][1])

        # Verifica se a cobra comeu a comida
        if cobra[0] == comida:
            cobra.append((0, 0))
            comida = (random.randrange(0, largura - tamanho_bloco, tamanho_bloco), random.randrange(0, altura - tamanho_bloco, tamanho_bloco))

        # Verifica se a cobra bateu na parede ou em si mesma
        if cobra[0][0] < 0 or cobra[0][0] >= largura or cobra[0][1] < 0 or cobra[0][1] >= altura:
            pygame.quit()
            sys.exit()

        for segmento in cobra[1:]:
            if cobra[0] == segmento:
                pygame.quit()
                sys.exit()

        # Limpa a janela
        janela.fill(cor_fundo)

        # Desenha a comida
        pygame.draw.rect(janela, cor_comida, (comida[0], comida[1], tamanho_bloco, tamanho_bloco))

        # Desenha a cobra
        desenhar_cobra(cobra)

        # Atualiza a tela
        pygame.display.update()

        # Define a taxa de atualização
        pygame.time.delay(150)

# Inicia o jogo
jogo_da_cobrinha()
