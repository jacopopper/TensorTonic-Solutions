import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    def pmf(n,p,k):
        return (math.factorial(n)*(p**k)*(1-p)**(n-k)) / (math.factorial(k)*math.factorial(n-k))
    pmf_val = pmf(n,p,k)
    
    cdf = []
    for i in range(k+1):
        cdf.append(pmf(n,p,i))
    cdf_val = sum(cdf)

    return {"pmf": pmf_val, "cdf": cdf_val}