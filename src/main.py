"""
Combinatorial optimization project
By Alexandre Achten and Julien Boistel

02/06/2024
"""

import argparse
import pandas as pd
from APL import *
from APC_MILP import *
from AP import *
from APC_IP import *
from utilities import *
from instances import *

# Parse arguments when using the command line
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--revenue', default='data/small-r.csv', help='Path to the revenue file')
parser.add_argument('-mu', '--mu', default='data/small-mu.csv', help='Path to the mu file')
parser.add_argument('-results', '--results', default='results/', help='Path to the results directory')
parser.add_argument('-m', '--model', default=0, type=int, help='Run specific model')
args = parser.parse_args()

# Reminder 0: AP, 1: APL, 2: APC_MILP, 3: APC_IP
model_nb = args.model
revenue_file = args.revenue
mu_file = args.mu
results_dir = args.results

# UNCOMMENT THIS PART TO ENTER THE FILE PATHS DIRECTLY
# model_nb = 3
# revenue_file = "data/medium-r.csv"
# mu_file = "data/medium-mu.csv"
# results_dir = "doc/"

instances_data_revenue = pd.read_csv(revenue_file,sep=';',header=None)
instances_data_mu = pd.read_csv(mu_file,sep=';',header=None)
print("Instances loaded")

# Run all instances on a specific model
print("Running instances on model", model_nb)
print("Computing...")
if model_nb == 0:
    AP_instances(instances_data_revenue, instances_data_mu, results_dir)
elif model_nb == 1:
    APL_instances(instances_data_revenue, instances_data_mu, results_dir)
elif model_nb == 2:
    APC_MILP_instances(instances_data_revenue, instances_data_mu, results_dir)
elif model_nb == 3:
    APC_IP_instances(instances_data_revenue, instances_data_mu, results_dir)

# WARNING: if several instances of the same size are run, the results will be appended to the same file