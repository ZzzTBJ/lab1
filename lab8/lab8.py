import pygame
import sys
import time
import random
pygame.init()
WIDTH, HEIGHT = 600, 600  
CELL_SIZE = 20  
FPS = 10  


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Алматинский жылан")
clock = pygame.time.Clock()



pos = [250, 250]
font_style = pygame.font.SysFont(None, 50)

def draw_score(score):
    score_text = font_style.render(f"Счет: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))
clock = pygame.time.Clock()
over = False

def check_collision(position, snake_body):
    return (
        position in snake_body or
        position[0] < 0 or
        position[1] < 0 or
        position[0] >= 600 or
        position[1] >= 600
    )

def main():
    snake = [(100, 100), (80, 100), (60, 100)]  
    direction = "RIGHT"  
    food_position = (
       random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
       random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    )
    score = 0
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

            head_x, head_y = snake[0]
            if direction == "UP":
                head_y -= CELL_SIZE
            elif direction == "DOWN":
                head_y += CELL_SIZE
            elif direction == "LEFT":
                head_x -= CELL_SIZE
            elif direction == "RIGHT":
                head_x += CELL_SIZE
            new_head = (head_x, head_y)

            if check_collision(new_head, snake):
                print(f"Игра окончена! Ваш счет: {score}")
                running = False
                break

            snake.insert(0, new_head)

            if new_head == food_position:
                score += 1
                food_position = (
                random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
                )
            else:
                snake.pop()  
            screen.fill((255,255,255))  
            for segment in snake:
                pygame.draw.rect(screen, (1, 50, 32), pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (138, 2,2 ), pygame.Rect(food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))
            draw_score(score)


            pygame.display.flip()
            clock.tick(FPS) 
if __name__ == "__main__":
    main()