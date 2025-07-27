import pygame
from menu import Menu
from levels.fase01 import Fase1
from settings import LARGURA, ALTURA


pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Wormhole")
clock = pygame.time.Clock()
# Estados do jogo
estados = {
    "menu": Menu(LARGURA, ALTURA),
    "fase1": Fase1(LARGURA, ALTURA)
}

estado_atual = "menu"
rodando = True

while rodando:
    # Processa o estado atual
    if estado_atual == "menu":
        menu = estados["menu"]
        menu.desenhar(tela)

        pygame.display.flip()
        mouse_pos = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = evento.pos
                    if 300<click_x<500 and 185<click_y<235:
                        estado_atual = "fase1"
                    elif 350<mouse_pos[0]<450 and 247<mouse_pos[1]<277:
                        rodando = False

    elif estado_atual == "fase1":
        resultado = estados["fase1"].executar(tela)
        if resultado == "menu":
            estado_atual = "menu"
        elif resultado == "sair":
            rodando = False

    clock.tick(60)

pygame.quit()