import pygame

# Inicialize o Pygame
pygame.init()

# Defina as dimensões iniciais do mapa
map_width, map_height = 800, 600

# Crie a janela do jogo
screen = pygame.display.set_mode((map_width, map_height))

# Defina a cor azul
blue = (0, 0, 255)

# Função para desenhar o mapa
def draw_map():
    screen.fill(blue)

# Função para detectar se o jogador está próximo da borda do mapa
def near_border(player_position, border_distance=50):
    x, y = player_position
    return x < border_distance or y < border_distance or x > map_width - border_distance or y > map_height - border_distance

# Função para estender o mapa
def extend_map():
    global map_width, map_height
    map_width += 100
    map_height += 100
    pygame.display.set_mode((map_width, map_height))

# Loop principal do jogo
while True:
    # Obtenha a posição do jogador
    player_position = pygame.mouse.get_pos()

    # Se o jogador estiver próximo da borda, estenda o mapa
    if near_border(player_position):
        extend_map()

    # Desenhe o mapa
    draw_map()

    # Atualize a tela
    pygame.display.flip()