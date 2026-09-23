import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    x_arr = np.asarray(X)
    x_c = x_arr - np.mean(x_arr, axis=0)
    return (np.dot(x_c.T, x_c)) / (len(x_arr)-1)
    