from ray import Ray
from optical_elements import FreeSpace, ThinLens, FlatRefraction
from screen_manager import ScreenManager

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

if __name__ == "__main__":
    sm = ScreenManager(SCREEN_WIDTH, SCREEN_HEIGHT)
    ray = Ray(SCREEN_HEIGHT/2, 0, 0)
    sm.add_ray(ray)  # Example ray

    sm.add_element(FreeSpace(2.0))

    sm.propagate_all()

    sm.loop()
    

