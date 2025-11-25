import numpy as np
import pygame
from ray import Ray

class OpticalElement:
    """"ABCD martix + propagation distance of a given optical element."""
    def __init__(self, M: np.ndarray, dx: float):
        self.M: np.ndarray = M
        self.dx: float = dx

    def propagate(self, ray: Ray):
        ray.aply_matrix(self.M, self.dx)
    
    def draw(self, screen, transform):
        pass
    
class FreeSpace(OpticalElement):
    def __init__(self, d: float):
        M = np.array([[1, d],
                      [0, 1]])
        super().__init__(M, d)

class FlatRefraction(OpticalElement):
    def __init__(self, ni: float, nt: float, dx: float = 0):
        M = np.array([[1, 0],
                      [0, ni / nt]])
        super().__init__(M, dx)

class ThinLens(OpticalElement):
    def __init__(self, f: float, dx: float = 0):
        M = np.array([[1, 0],
                      [-1 / f, 1]])
        super().__init__(M, dx)
