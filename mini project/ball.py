import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
ball_radius = 20
ball_color = (255, 255, 255)
bg_color = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Set up the ball's initial position and velocity
ball_pos = [width // 2, height // 2]
ball_velocity = [5, 5]  # Adjust the velocity as needed

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Bounce off the walls
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
        ball_velocity[0] = -ball_velocity[0]
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_velocity[1] = -ball_velocity[1]

    # Fill the background
    screen.fill(bg_color)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

