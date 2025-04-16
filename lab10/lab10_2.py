import pygame
import sys
import time
import random
import psycopg2
import csv
pygame.init()
WIDTH, HEIGHT = 600, 600  
CELL_SIZE = 20  
FPS = 10  
SPEED = 6


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Алматинский жылан")
clock = pygame.time.Clock()

pos = [250, 250]
font_style = pygame.font.SysFont(None, 30)

def connect_db():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="postgres",
        password="2303",
        host="localhost",
        port="5432"
    )
    return conn

def crtab():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS player (
            id SERIAL PRIMARY KEY,
            username VARCHAR(30) NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES player(id),
            score INTEGER,
            level INTEGER,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def draw_score(score, lvl):
    score_text = font_style.render(f"Счет: {score}", True, (0,0,0))
    lvl_text = font_style.render(f"Уровень: {lvl}", True, (0,0,0))
    screen.blit(score_text, (10, 10))
    screen.blit(lvl_text, (10, 40))
    save_sc(score, lvl, user_id)
    
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
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

BERRY_TIMER = pygame.USEREVENT + 1  
pygame.time.set_timer(BERRY_TIMER, 10000)

snake = [(100, 100), (80, 100), (60, 100)]  
direction = "RIGHT"  
food_position1 = (
       random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
       random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
)
food_position2 = (
       random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
       random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
)

score = 0
lvl = 0
running = True

def save_sc(score, level, user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO score (user_id, score, level) VALUES (%s, %s, %s)", 
                (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

def user_login():
    conn = connect_db()
    username = input("Enter your username: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM player WHERE username = %s", (username,))
    user = cur.fetchone()
    
    if not user:
        cur.execute("INSERT INTO player (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        print(f"New user {username} created.")
    else:
        user_id = user[0]
        print(f"Welcome back {username}!")

    conn.commit()

    cur.execute("""
        SELECT score, level FROM score 
        WHERE user_id = %s 
        ORDER BY date DESC LIMIT 1
    """, (user_id,))
    user_score_data = cur.fetchone()
    
    if user_score_data:
        last_score, last_level = user_score_data
    else:
        last_score, last_level = 0, 1 
    
    print(f"Your last score: {last_score}, Last level: {last_level}")

    cur.close()
    conn.close()
    return user_id, last_score, last_level

crtab()
user_id, score, level = user_login()
while running:
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.5   
            if event.type == BERRY_TIMER:
                food_position1 = (
                    random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
                )
                food_position2 = (
                    random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
                )
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
                print(f"Игра окончена! Ваш счет: {lvl*3+score}")
                running = False
                break

            snake.insert(0, new_head)
            if (score >= 4):
                lvl += 1
                score = 0
                FPS += 2
            if new_head == food_position1:
                score += 1
                food_position1 = (
                random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
                )
            elif new_head == food_position2:
                score += 3
                food_position2 = (
                    random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
                )
            else:
                snake.pop()  
            screen.fill((255,255,255))  
            for segment in snake:
                pygame.draw.rect(screen, (1, 50, 32), pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (138, 2,2 ), pygame.Rect(food_position1[0], food_position1[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (255, 215,0 ), pygame.Rect(food_position2[0], food_position2[1], CELL_SIZE, CELL_SIZE))
            draw_score(score, lvl)

        clock.tick(FPS) 
        pygame.display.flip()
        