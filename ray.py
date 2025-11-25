import numpy as np

class RayState:
    def __init__(self, r: float, theta: float, x: float = 0.0):
        self.r: float = r
        self.theta: float = theta
        self.x: float = x

    def as_vector(self) -> np.ndarray:
        return np.array([self.r, self.theta])

class Ray():
    def __init__(self, r0: float, theta0: float, x_0: float, color: tuple[int, int, int] = (255, 255, 0)):
        self.color: tuple[int, int, int] = color
        self.states: list[RayState] = [RayState(r0, theta0, x_0)]

    def aply_matrix(self, M: np.ndarray, dx: float):
        last_state = self.states[-1]
        new_vector = M @ last_state.as_vector()
        new_x = last_state.x + dx
        new_state = RayState(new_vector[0], new_vector[1], new_x)
        self.states.append(new_state)
    
    def get_path(self) -> list[tuple[float, float]]:
        return [(s.x, s.r) for s in self.states]



