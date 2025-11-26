class CoordinateTransformer:
    def __init__(self, screen_width: int, screen_height: int, scale: int = 50):
        self.screen_width: int = screen_width
        self.screen_height: int = screen_height
        self.scale: int = scale # pixels per fisical unit

    def world_to_screen(self, x: float, r: float) -> tuple[int, int]:
        """Convert fisical (x, r) coordinates to screen (x,y) coordinates."""
        screen_x = int(x * self.scale)
        screen_y = int(self.screen_height / 2 - r * self.scale)
        return screen_x, screen_y
    
    def screen_to_world(self, screen_x: int, screen_y: int) -> tuple[float, float]:
        """Convert screen (x,y) coordinates to fisical (x, r) coordinates."""
        x = screen_x / self.scale
        r = (self.screen_height / 2 - screen_y) / self.scale
        return x, r