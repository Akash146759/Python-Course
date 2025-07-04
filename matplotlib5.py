import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

import pygame
import numpy as np

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animated Sine Wave")
clock = pygame.time.Clock()

# Animation variables
frame = 0
running = True

while running:
    # Create matplotlib figure and axis
    fig, ax = plt.subplots(figsize=[4, 3], dpi=100)
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + frame / 10.0)
    ax.plot(x, y, color='blue')
    ax.set_title("Animated Sine Wave")
    ax.set_ylim(-1.5, 1.5)

    # Render to buffer
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.buffer_rgba()
    size = canvas.get_width_height()
    plot_surface = pygame.image.frombuffer(raw_data, size, "RGBA")

    # Display in Pygame
    screen.fill((30, 30, 30))
    screen.blit(plot_surface, (200, 150))
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame += 1
    clock.tick(30)  # Limit to 30 FPS

pygame.quit()
