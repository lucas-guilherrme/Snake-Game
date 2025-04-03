import pygame
import sys
import random
from utils import draw_snake, draw_food, display_game_over


# Fazendo a primeira versao do jogo

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
BLACK = (0, 0, 0)

# Configurações da cobra
snake_body = [(100, 50), (90, 50), (80, 50)]  # Segmentos iniciais
snake_direction = "RIGHT"
change_to = snake_direction

# Configurações da comida
food_position = (random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10)
food_spawn = True

# Velocidade
SPEED = 15

# Loop principal
def main():
    global change_to, snake_direction, food_position, food_spawn

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Controle da direção
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    change_to = "RIGHT"

        # Atualiza a direção da cobra
        snake_direction = change_to

        # Move a cobra
        head_x, head_y = snake_body[0]
        if snake_direction == "UP":
            head_y -= 10
        elif snake_direction == "DOWN":
            head_y += 10
        elif snake_direction == "LEFT":
            head_x -= 10
        elif snake_direction == "RIGHT":
            head_x += 10

        # Adiciona o novo segmento na frente
        snake_body.insert(0, (head_x, head_y))

        # Verifica se a cobra comeu a comida
        if head_x == food_position[0] and head_y == food_position[1]:
            food_spawn = False
        else:
            # Remove o último segmento se não comeu
            snake_body.pop()

        # Reposiciona a comida
        if not food_spawn:
            food_position = (random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10)
        food_spawn = True

        # Verifica colisões com as bordas
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            display_game_over(screen, WIDTH, HEIGHT)
            running = False

        # Verifica colisões com o próprio corpo
        for segment in snake_body[1:]:
            if head_x == segment[0] and head_y == segment[1]:
                display_game_over(screen, WIDTH, HEIGHT)
                running = False

        # Preenche a tela com a cor preta
        screen.fill(BLACK)

        # Desenha a cobra e a comida
        draw_snake(screen, snake_body)
        draw_food(screen, food_position)

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de quadros
        clock.tick(SPEED)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()