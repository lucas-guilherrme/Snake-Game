import pygame

def draw_snake(screen, snake_body):
    """
    Desenha a cobra na tela.
    :param screen: Superfície do pygame onde a cobra será desenhada.
    :param snake_body: Lista de segmentos da cobra (cada segmento é uma tupla com coordenadas x, y).
    """
    for segment in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))

def draw_food(screen, food_position):
    """
    Desenha a comida na tela.
    :param screen: Superfície do pygame onde a comida será desenhada.
    :param food_position: Coordenadas (x, y) da comida.
    """
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_position[0], food_position[1], 10, 10))

def display_game_over(screen, width, height):
    """
    Exibe a mensagem de "Game Over" na tela.
    :param screen: Superfície do pygame onde a mensagem será exibida.
    :param width: Largura da tela.
    :param height: Altura da tela.
    """
    font = pygame.font.SysFont('Arial', 50)
    game_over_surface = font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)