import numpy as np
class Ray:
    def __init__(self, r: float, theta: float, x_0: float, color: tuple[int, int, int] = (255, 255, 0)):
        self.xs: np.array[float] = np.array([x_0])
        self.color: tuple[int, int, int] = color
        self.path: np.array[float] = np.array([[r, theta]])

