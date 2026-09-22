from collections import Counter
import numpy as np


def mean_median_mode(x: list) -> dict:
    """Returns a dictionary with mean, median, and mode."""
    sorted_x = sorted(x)
    n = len(sorted_x)

    mean = float(np.mean(sorted_x))

    # Sort first, then compute median
    mid = n // 2
    if n % 2 == 0:
        median = float((sorted_x[mid - 1] + sorted_x[mid]) / 2.0)
    else:
        median = float(sorted_x[mid])

    # Mode: element with the highest frequency
    counts = Counter(sorted_x)
    mode = float(max(counts, key=counts.get))

    return {"mean": mean, "median": median, "mode": mode}