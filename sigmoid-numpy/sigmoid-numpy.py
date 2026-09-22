import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    x_arr = np.asarray(x)
    # Write code here
    return 1/(1+np.exp(-x_arr))