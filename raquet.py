import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura_tela = 600
altura_tela = 400
cor_fundo = (0, 0, 0)
cor_raquete = (255, 255, 255)
cor_bola = (255, 0, 0)
velocidade_raquete = 5
velocidade_bola = [4, 4]

# Criar a tela do jogo
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Raquete")

# Criar a raquete
raquete = pygame.Rect(largura_tela // 2 - 60, altura_tela - 20, 120, 10)

# Criar a bola
bola = pygame.Rect(largura_tela // 2 - 15, altura_tela // 2 - 15, 30, 30)

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento da raquete
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and raquete.left > 0:
        raquete.move_ip(-velocidade_raquete, 0)
    if teclas[pygame.K_RIGHT] and raquete.right < largura_tela:
        raquete.move_ip(velocidade_raquete, 0)

    # Movimento da bola
    bola.move_ip(velocidade_bola[0], velocidade_bola[1])

    # Verificar colisões com as bordas da tela
    if bola.left <= 0 or bola.right >= largura_tela:
        velocidade_bola[0] = -velocidade_bola[0]
    if bola.top <= 0 or bola.bottom >= altura_tela:
        velocidade_bola[1] = -velocidade_bola[1]

    # Verificar colisão com a raquete
    if bola.colliderect(raquete):
        velocidade_bola[1] = -velocidade_bola[1]

    # Limpar a tela
    tela.fill(cor_fundo)

    # Desenhar a raquete e a bola
    pygame.draw.rect(tela, cor_raquete, raquete)
    pygame.draw.ellipse(tela, cor_bola, bola)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros por segundo
    pygame.time.Clock().tick(60)