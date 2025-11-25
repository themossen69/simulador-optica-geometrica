import pygame
from ray import Ray
from coordinates import CoordinateTransformer
from optical_elements import OpticalElement

class ScreenManager:
    caption = "Ray Optics Simulator"
    def __init__(self, width: int, height: int):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.transform = CoordinateTransformer(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.rays: list[Ray] = []
        self.elements: list[OpticalElement] = []
        self.background_color = (0, 0, 0)
        self.running = True

        if not pygame.get_init():
            pygame.init()
        
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.caption)

    def add_ray(self, ray: Ray):
        self.rays.append(ray)

    def add_element(self, element: OpticalElement):
        self.elements.append(element)

    def propagate_all(self):
        for elem in self.elements:
            for r in self.rays:
                elem.propagate(r)

    def draw_rays(self):
        for ray in self.rays:
            points = ray.get_path()
            screen_points = [self.transform.world_to_screen(x, r) for x, r in points]
            pygame.draw.lines(self.screen, ray.color, False, screen_points, 2)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def loop(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.screen.fill(self.background_color)
            self.draw_rays()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
    