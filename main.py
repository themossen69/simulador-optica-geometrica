from ray import Ray
from optical_elements import FreeSpace, ThinLens, FlatRefraction
from screen_manager import ScreenManager

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

if __name__ == "__main__":
    sm = ScreenManager(SCREEN_WIDTH, SCREEN_HEIGHT)
    ray = Ray(0.0, 0.2, 0.0)
    sm.add_ray(ray)  # Example ray

    dist_window = sm.transform.screen_to_world(SCREEN_WIDTH, 0)[0]
     # Add optical elements

    sm.add_element(FreeSpace(dist_window))

    sm.propagate_all()

    sm.loop()
    

