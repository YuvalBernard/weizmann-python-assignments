import sys
import pandas as pd
from helper_functions import get_dist_info

def main():
    filename = sys.argv[1]
    data = pd.read_csv(filename)
    mu, sigma = get_dist_info(data)
    for i, par in enumerate(parameters):
        mu, sigma = mu_sigma[i]
        print(f"{par} ~ Normal({mu:.3g},{sigma:.3g})")