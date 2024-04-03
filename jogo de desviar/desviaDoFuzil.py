import pygame
import random
import sys


# Inicialização do Pygame
pygame.init()


# Configurações do jogo
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Esquiva de Obstáculos")


# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)


# Personagem
personagem_largura = 50
personagem_altura = 50
personagem_x = largura // 2 - personagem_largura // 2
personagem_y = altura - personagem_altura - 10
personagem_velocidade = 5


# Obstáculos
obstaculo_largura = 50
obstaculo_altura = 50
obstaculo_x = random.randint(0, largura - obstaculo_largura)
obstaculo_y = 0
obstaculo_velocidade = 3


# Pontuação
pontuacao = 0
fonte = pygame.font.Font(None, 36)


# Estado do jogo
jogando = False


# Função para reiniciar o jogo
def reiniciar_jogo():
    global personagem_x, pontuacao, jogando
    personagem_x = largura // 2 - personagem_largura // 2
    pontuacao = 0
    jogando = True


# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if not jogando:
                reiniciar_jogo()


    if jogando:
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and personagem_x > 0:
            personagem_x -= personagem_velocidade
        if teclas[pygame.K_RIGHT] and personagem_x < largura - personagem_largura:
            personagem_x += personagem_velocidade


        # Movimento do obstáculo
        obstaculo_y += obstaculo_velocidade


        # Verifica se o obstáculo atingiu o chão
        if obstaculo_y > altura:
            obstaculo_x = random.randint(0, largura - obstaculo_largura)
            obstaculo_y = 0
            pontuacao += 1


        # Verifica colisão com o personagem
        if (personagem_x < obstaculo_x + obstaculo_largura and
                personagem_x + personagem_largura > obstaculo_x and
                personagem_y < obstaculo_y + obstaculo_altura and
                personagem_y + personagem_altura > obstaculo_y):
            jogando = False


        # Limpa a tela
        tela.fill(preto)


        # Desenha o personagem
        pygame.draw.rect(tela, branco, (personagem_x, personagem_y, personagem_largura, personagem_altura))


        # Desenha o obstáculo
        pygame.draw.rect(tela, branco, (obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura))


        # Exibe a pontuação na tela
        texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, branco)
        tela.blit(texto_pontuacao, (10, 10))
    else:
        # Tela de menu
        tela.fill(preto)
        texto_menu = fonte.render("Pressione qualquer tecla para iniciar", True, branco)
        tela.blit(texto_menu, (largura // 2 - texto_menu.get_width() // 2, altura // 2 - 18))


    # Atualiza a tela
    pygame.display.update()
