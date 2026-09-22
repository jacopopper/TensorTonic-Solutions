import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = []
    for i in range(len(x)):
        if x[i] == 0:
            pmf.append(1-p)
        else:
            pmf.append(p)
    
    return {"pmf": np.asarray(pmf), "mean": float(p), "variance": float(p*(1-p))}