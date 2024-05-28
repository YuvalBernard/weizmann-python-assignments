import numpy as np
from scipy.stats import norm
from functools import partial

@partial(np.vectorize, excluded=[2,3], signature='(),()->(n)')
def normal_dist_from_quantiles(x1, x2, p1, p2):
    mu = (x1*norm.ppf(p2) - x2*norm.ppf(p1))/(norm.ppf(p2) - norm.ppf(p1))
    sigma = (x2 - x1)/(norm.ppf(p2) - norm.ppf(p1))
    return np.array([mu, sigma])

def get_dist_info(data):
    parameters = data["parameter"]
    lb = data["lb"]
    ub = data["ub"]
    mu_sigma = normal_dist_from_quantiles(lb, ub, 0.025, 0.975)

    return mu_sigma[:, 0], mu_sigma[:, 1]
