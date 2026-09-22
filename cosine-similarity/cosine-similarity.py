import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    x_arr = np.asarray(a)
    y_arr = np.asarray(b)
    norm_product = ((np.linalg.norm(x_arr, ord=2)*np.linalg.norm(y_arr, ord=2)))
    if norm_product == 0:
        return 0.0

    return float(np.dot(x_arr, y_arr)/norm_product)
    