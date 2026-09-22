import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x_arr = np.asarray(x)
    var = float(np.var(x_arr, ddof=1))
    return {"variance": var, "standard_deviation": float(np.sqrt(var))}
    