
import pygame
import sys

pygame.init()


# Tela
LARGURA = 800
ALTURA = 500

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("TV KILLER")

clock = pygame.time.Clock()

# Cores
PRETO = (8, 8, 8)
BRANCO = (230, 230, 230)
VERMELHO = (180, 20, 20)
CINZA = (80, 80, 80)
CINZA_ESCURO = (30, 30, 30)
AZUL = (50, 90, 150)
PELE = (210, 170, 140)
BOTAO = (55, 55, 55)
BOTAO_ATIVO = (100, 100, 100)

# Jogador
jogador = pygame.Rect(100, 200, 30, 45)
velocidade = 4

# TV Killer
tv_killer = pygame.Rect(650, 200, 55, 85)
velocidade_killer = 1.3

perdeu = False


# -------------------------
# BOTÕES
# -------------------------

botao_esquerda = pygame.Rect(40, 400, 80, 70)
botao_direita = pygame.Rect(220, 400, 80, 70)

botao_cima = pygame.Rect(130, 320, 80, 70)
botao_baixo = pygame.Rect(130, 400, 80, 70)


# -------------------------
# DESENHAR JOGADOR
# -------------------------

def desenhar_jogador():

    pygame.draw.circle(
        tela,
        PELE,
        (jogador.centerx, jogador.y + 8),
        8
    )

    pygame.draw.rect(
        tela,
        AZUL,
        (jogador.x + 5, jogador.y + 15, 20, 25)
    )

    pygame.draw.line(
        tela,
        PRETO,
        (jogador.x + 10, jogador.y + 40),
        (jogador.x + 5, jogador.bottom),
        5
    )

    pygame.draw.line(
        tela,
        PRETO,
        (jogador.x + 20, jogador.y + 40),
        (jogador.x + 25, jogador.bottom),
        5
    )


# -------------------------
# DESENHAR TV KILLER
# -------------------------

def desenhar_tv_killer():

    # Corpo
    pygame.draw.rect(
        tela,
        (20, 20, 20),
        tv_killer
    )

    # Televisão
    tv = pygame.Rect(
        tv_killer.x - 5,
        tv_killer.y - 25,
        65,
        55
    )

    pygame.draw.rect(
        tela,
        CINZA_ESCURO,
        tv
    )

    pygame.draw.rect(
        tela,
        CINZA,
        tv,
        4
    )

    # Tela
    tela_tv = pygame.Rect(
        tv.x + 8,
        tv.y + 8,
        tv.width - 16,
        tv.height - 16
    )

    pygame.draw.rect(
        tela,
        (5, 5, 5),
        tela_tv
    )

    # Estática
    for y in range(tela_tv.top, tela_tv.bottom, 4):

        pygame.draw.line(
            tela,
            (70, 70, 70),
            (tela_tv.left, y),
            (tela_tv.right, y)
        )

    # Olhos
    pygame.draw.circle(
        tela,
        VERMELHO,
        (tela_tv.left + 17, tela_tv.centery),
        4
    )

    pygame.draw.circle(
        tela,
        VERMELHO,
        (tela_tv.right - 17, tela_tv.centery),
        4
    )

    # Antenas
    pygame.draw.line(
        tela,
        CINZA,
        (tv.centerx - 5, tv.top),
        (tv.centerx - 20, tv.top - 18),
        3
    )

    pygame.draw.line(
        tela,
        CINZA,
        (tv.centerx + 5, tv.top),
        (tv.centerx + 20, tv.top - 18),
        3
    )


# -------------------------
# BOTÃO
# -------------------------

def desenhar_botao(rect, texto, pressionado):

    if pressionado:
        cor = BOTAO_ATIVO
    else:
        cor = BOTAO

    pygame.draw.rect(
        tela,
        cor,
        rect,
        border_radius=12
    )

    pygame.draw.rect(
        tela,
        CINZA,
        rect,
        3,
        border_radius=12
    )

    fonte = pygame.font.Font(None, 45)

    imagem = fonte.render(
        texto,
        True,
        BRANCO
    )

    tela.blit(
        imagem,
        (
            rect.centerx - imagem.get_width() // 2,
            rect.centery - imagem.get_height() // 2
        )
    )


# -------------------------
# REINICIAR
# -------------------------

def reiniciar():

    global perdeu

    jogador.x = 100
    jogador.y = 200

    tv_killer.x = 650
    tv_killer.y = 200

    perdeu = False


# -------------------------
# LOOP
# -------------------------

while True:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --------------------------------
    # POSIÇÃO DO TOQUE / MOUSE
    # --------------------------------

    mouse_x, mouse_y = pygame.mouse.get_pos()

    mouse_pressionado = pygame.mouse.get_pressed()[0]

    # --------------------------------
    # DERROTA
    # --------------------------------

    if perdeu:

        tela.fill(PRETO)

        fonte = pygame.font.Font(None, 55)

        texto = fonte.render(
            "TV KILLER TE PEGOU",
            True,
            VERMELHO
        )

        tela.blit(
            texto,
            (
                LARGURA // 2 - texto.get_width() // 2,
                180
            )
        )

        fonte2 = pygame.font.Font(None, 30)

        texto2 = fonte2.render(
            "Toque para jogar novamente",
            True,
            BRANCO
        )

        tela.blit(
            texto2,
            (
                LARGURA // 2 - texto2.get_width() // 2,
                250
            )
        )

        if mouse_pressionado:
            reiniciar()

        pygame.display.flip()
        clock.tick(60)
        continue

    # --------------------------------
    # CONTROLES TOUCH
    # --------------------------------

    tocando_esquerda = (
        mouse_pressionado
        and botao_esquerda.collidepoint(mouse_x, mouse_y)
    )

    tocando_direita = (
        mouse_pressionado
        and botao_direita.collidepoint(mouse_x, mouse_y)
    )

    tocando_cima = (
        mouse_pressionado
        and botao_cima.collidepoint(mouse_x, mouse_y)
    )

    tocando_baixo = (
        mouse_pressionado
        and botao_baixo.collidepoint(mouse_x, mouse_y)
    )

    # --------------------------------
    # MOVIMENTO
    # --------------------------------

    if tocando_esquerda:
        jogador.x -= velocidade

    if tocando_direita:
        jogador.x += velocidade

    if tocando_cima:
        jogador.y -= velocidade

    if tocando_baixo:
        jogador.y += velocidade

    # Limites
    jogador.x = max(
        0,
        min(LARGURA - jogador.width, jogador.x)
    )

    jogador.y = max(
        80,
        min(ALTURA - 100, jogador.y)
    )

    # --------------------------------
    # TV KILLER PERSEGUE
    # --------------------------------

    if tv_killer.x < jogador.x:
        tv_killer.x += velocidade_killer

    if tv_killer.x > jogador.x:
        tv_killer.x -= velocidade_killer

    if tv_killer.y < jogador.y:
        tv_killer.y += velocidade_killer

    if tv_killer.y > jogador.y:
        tv_killer.y -= velocidade_killer

    # --------------------------------
    # COLISÃO
    # --------------------------------

    if jogador.colliderect(tv_killer):
        perdeu = True

    # --------------------------------
    # DESENHAR
    # --------------------------------

    tela.fill((15, 15, 15))

    # Área do cenário
    pygame.draw.rect(
        tela,
        (25, 25, 25),
        (0, 70, LARGURA, 320)
    )

    # Título
    fonte = pygame.font.Font(None, 40)

    titulo = fonte.render(
        "TV KILLER",
        True,
        VERMELHO
    )

    tela.blit(
        titulo,
        (20, 20)
    )

    # Personagens
    desenhar_jogador()
    desenhar_tv_killer()

    # Botões
    desenhar_botao(
        botao_esquerda,
        "<",
        tocando_esquerda
    )

    desenhar_botao(
        botao_direita,
        ">",
        tocando_direita
    )

    desenhar_botao(
        botao_cima,
        "^",
        tocando_cima
    )

    desenhar_botao(
        botao_baixo,
        "v",
        tocando_baixo
    )

    pygame.display.flip()

    clock.tick(60)
    
    
    pygame.display.set_caption("TV KILLER 0.1")