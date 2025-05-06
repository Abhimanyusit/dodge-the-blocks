import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Clock
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Font for score
font = pygame.font.SysFont(None, 36)

# Player setup
player_width, player_height = 50, 10
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 5

# Block setup
block_width, block_height = 50, 50
block_speed = 5
blocks = []

# Block spawn timer
spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 1000)

# Score
score = 0
score_event = pygame.USEREVENT + 2
pygame.time.set_timer(score_event, 500)  # Increase score every 0.5 sec

# Main loop
running = True
while running:
    clock.tick(60)
    SCREEN.fill(WHITE)

    # Player rectangle
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == spawn_event:
            block_x = random.randint(0, WIDTH - block_width)
            block_rect = pygame.Rect(block_x, 0, block_width, block_height)
            blocks.append(block_rect)
        elif event.type == score_event:
            score += 1

    # Handle keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move and draw blocks
    for block in blocks[:]:
        block.y += block_speed
        if block.y > HEIGHT:
            blocks.remove(block)
        if block.colliderect(player_rect):
            # Game Over
            game_over_font = pygame.font.SysFont(None, 60)
            text = game_over_font.render("GAME OVER", True, RED)
            SCREEN.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 30))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
        pygame.draw.rect(SCREEN, RED, block)

    # Draw player
    pygame.draw.rect(SCREEN, BLACK, player_rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
