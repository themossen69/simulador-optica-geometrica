import numpy as np
# s'haurà de tenir en compte el radi positiu o negatiu segons si curva convexa o concava

def ray_transfer_matrix(d: float) -> np.ndarray:
    return np.array([[1, d],
                     [0, 1]])

def flat_refraction(ni: float, nt: float) -> np.ndarray:
    return np.array([[1, 0],
                     [0, ni / nt]])

def curved_refraction(ni: float, nt: float, R: float) -> np.ndarray:
    return np.array([[1, 0],
                    [(nt - ni) / (R * nt), ni / nt]])

def thin_lens(f: float) -> np.ndarray:
    return np.array([[1, 0],
                     [-1 / f, 1]])

def flat_reflection(horizontal: bool) -> np.ndarray:
    # For now only horizontal and vertical mirrors are supported
    if horizontal:
        return np.array([[1, 0],
                         [0, -1]])
    else:
        return np.array([[-1, 0],
                         [0, 1]])
    
def curved_reflection(R: float) -> np.ndarray:
    return np.array([[1, 0],
                     [-2 / R, 1]])