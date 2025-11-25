import pygame
import tkinter as tk

class WindowManager:
    caption = "Simulador"
    def __init__(self):
        if not pygame.get_init():
            pygame.init()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.caption)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True


if __name__ == "__main__":
    window = WindowManager()
    running = True
    print("Window initialized with size:", window.SCREEN_WIDTH, "x", window.SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    while running:
        window.screen.fill((0, 0, 0))  # Clear screen with black
        pygame.display.flip()
        running = window.handle_events()
        clock.tick(60)
    pygame.quit()

