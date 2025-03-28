import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)
choices = ["Rock", "Paper", "Scissors"]
rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")
images = {"Rock": rock_img, "Paper": paper_img, "Scissors": scissors_img}
for key in images:
    images[key] = pygame.transform.scale(images[key], (100, 100))
running = True
player_choice = None
computer_choice = None
result = ""
while running:
    screen.fill(WHITE)
    title_text = font.render("Rock Paper Scissors", True, BLACK)
    screen.blit(title_text, (200, 20))
    screen.blit(images["Rock"], (50, 150))
    screen.blit(images["Paper"], (250, 150))
    screen.blit(images["Scissors"], (450, 150))
    if player_choice and computer_choice:
        result_text = font.render(
            f"{player_choice} vs {computer_choice}: {result}", True, BLACK)
        screen.blit(result_text, (150, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 50 <= x <= 150 and 150 <= y <= 250:
                player_choice = "Rock"
            elif 250 <= x <= 350 and 150 <= y <= 250:
                player_choice = "Paper"
            elif 450 <= x <= 550 and 150 <= y <= 250:
                player_choice = "Scissors"
            if player_choice:
                computer_choice = random.choice(choices)
                if player_choice == computer_choice:
                    result = "It's a Tie!"
                elif (player_choice == "Rock" and computer_choice == "Scissors") or \
                     (player_choice == "Paper" and computer_choice == "Rock") or \
                     (player_choice == "Scissors" and computer_choice == "Paper"):
                    result = "You Win!"
                else:
                    result = "You Lose!"
    pygame.display.flip()
pygame.quit()
