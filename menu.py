import pygame

class Menu:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.fonte = pygame.font.SysFont(None, 48)
        self.fonte_pequena = pygame.font.SysFont(None, 36)

    def desenhar(self, tela):
        tela.fill((0, 0, 0))  # Fundo preto

        # Título
        titulo = self.fonte.render("WORMHOLE", True, (255, 255, 255))
        tela.blit(titulo, (self.largura // 2 - titulo.get_width() // 2, 100))

        botao_start = pygame.draw.rect(tela, (0,255,0),(300, 185, 200, 50))
        botao_sair = pygame.draw.rect(tela, (255, 0, 0), (350, 247, 100, 30))
        # Opções
        opcoes = [
            "Start/Resume",
            "Sair"
        ]

        for i, opcao in enumerate(opcoes):
            texto = self.fonte_pequena.render(opcao, True, (255, 255, 255))
            tela.blit(texto, (self.largura // 2 - texto.get_width() // 2, 200 + i * 50))
