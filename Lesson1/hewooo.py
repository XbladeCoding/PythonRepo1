import pygame
import os

width, height = 800, 600

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rohan Game')
PICTURE = pygame.image.load(os.path.join('Lesson1', 'python1pic.jpg'))
SONG = os.path.join(os.getcwd(), 'Lesson1/The Mandalorian Main Theme.mp3')

def draw_fn():
    GScreen.fill((100,100,100))
    GScreen.blit(PICTURE, (0, 0))
    pygame.display.update()

FPS = 60

def main():
    pygame.mixer.init()
    pygame.mixer.music.load(SONG)
    pygame.mixer.music.play(-1)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_fn()

if __name__ == "__main__":
    main()