import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the player
player_size = 60
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT // 2 - player_size // 2
player_speed = 5
player_jump_speed = 12
player_jump_height = 200
player_is_jumping = False
player_direction = "right"
player_is_running = False
player_jump_speed_current = 0
player_jump_start_y = 0

# Load images
player_image = pygame.transform.scale(pygame.image.load("player.png").convert_alpha(), (player_size, player_size))

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                if not player_is_jumping:
                    player_is_jumping = True
                    player_jump_start_y = player_y
                    player_jump_speed_current = player_jump_speed
            elif event.key == pygame.K_RIGHT:
                player_direction = "right"
            elif event.key == pygame.K_LEFT:
                player_direction = "left"
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                player_speed = 20  # Change player speed to faster
                player_is_running = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                player_speed = 5  # Change player speed back to normal
                player_is_running = False

    # Handle jumping
    if player_is_jumping:
        player_y -= player_jump_speed_current
        player_jump_speed_current -= 1
        if player_y > player_jump_start_y:
            player_y = player_jump_start_y
            player_is_jumping = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        if not player_is_jumping:
            player_is_jumping = True
            player_jump_start_y = player_y
            player_jump_speed_current = player_jump_speed

    # Fill the screen with white
    screen.fill((245, 245, 245))

    # Draw the player
    player_rect = player_image.get_rect(center=(player_x + player_size // 2, player_y + player_size // 0.3))
    screen.blit(player_image, player_rect)

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    clock.tick(40)
