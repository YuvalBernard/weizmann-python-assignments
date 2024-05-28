import pytest
from helper_functions import get_dist_info

def test_get_dist_info():
    data = pd.read_csv("example.csv")
    mu, sigma = get_dist_info(data)
    assert f"{mu[2]:.3g}, {sigma[2]:.3g}" == "155, 74"