import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elliptical Orbits Simulation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Function to calculate the position of a point in an elliptical orbit
def calculate_position(center, semi_major_axis, semi_minor_axis, angle):
    x = center[0] + semi_major_axis * math.cos(angle)
    y = center[1] + semi_minor_axis * math.sin(angle)
    return int(x), int(y)

# Function to draw the elliptical orbit
def draw_ellipse(center, semi_major_axis, semi_minor_axis):
    pygame.draw.ellipse(screen, white, [center[0] - semi_major_axis, center[1] - semi_minor_axis, semi_major_axis * 2, semi_minor_axis * 2], 1)

# Main game loop
clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    # Elliptical orbit parameters
    center = (width // 2, height // 2)
    semi_major_axis = 200
    semi_minor_axis = 100

    # Calculate position on the elliptical orbit
    planet_radius = 10
    planet_position = calculate_position(center, semi_major_axis, semi_minor_axis, math.radians(angle))

    # Draw the elliptical orbit
    draw_ellipse(center, semi_major_axis, semi_minor_axis)

    # Draw the planet
    pygame.draw.circle(screen, white, planet_position, planet_radius)

    # Increment the angle for the next frame
    angle += 1

    pygame.display.flip()
    clock.tick(60)
