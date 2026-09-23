import numpy as np


def matrix_normalization(
    matrix: list, axis=None, norm_type: str = "l2"
) -> np.ndarray:
    """Returns a NumPy array with the same shape as matrix."""
    x_arr = np.asarray(matrix, dtype=float)

    match norm_type:
        case "l1":
            norm = np.sum(np.abs(x_arr), axis=axis, keepdims=True)
        case "l2":
            norm = np.sqrt(np.sum(x_arr**2, axis=axis, keepdims=True))
        case "max":
            norm = np.max(np.abs(x_arr), axis=axis, keepdims=True)
        case _:
            raise ValueError(f"Unknown norm_type: {norm_type}")

    # Avoid division by zero
    norm = np.where(norm == 0, 1.0, norm)

    return x_arr / norm