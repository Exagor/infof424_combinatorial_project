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

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--revenue', default='data/small-r.csv', help='Path to the revenue file')
parser.add_argument('-mu', '--mu', default='data/small-mu.csv', help='Path to the mu file')
parser.add_argument('-results', '--results', default='results/', help='Path to the results directory')
parser.add_argument('-m', '--model', default=0, help='Run specific model')
args = parser.parse_args()

# Reminder 0: AP, 1: APL, 2: APC_MILP, 3: APC_IP

revenue_file = args.revenue
mu_file = args.mu
results_dir = args.results

# To change accordingly to the files #TODO suppress this part
revenue_file = "data/small-r.csv"
mu_file = "data/small-mu.csv"
results_dir = "results/"

instances_data_revenue = pd.read_csv(revenue_file,sep=';',header=None)
instances_data_mu = pd.read_csv(mu_file,sep=';',header=None)

# Run all instances on a specific model #TODO uncomment this part
# if args.model == 0:
#     AP_instances(instances_data_revenue, instances_data_mu, results_dir)
# elif args.model == 1:
#     APL_instances(instances_data_revenue, instances_data_mu, results_dir)
# elif args.model == 2:
#     APC_MILP_instances(instances_data_revenue, instances_data_mu, results_dir)

# WARNING: if several instances of the same size are run, the results will be appended to the same file

if __name__ == "__main__":
    #TODO suppress this part
    # size_name = "data/small"
    # instances_data_revenue = pd.read_csv(data_dir_path + size_name+"-r.csv",sep=';',header=None)
    # instances_data_mu = pd.read_csv(data_dir_path + size_name + "-mu.csv",sep=';',header=None)
    # data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=0)

    # run all instances
    run_all_sizes_and_instances(AP=False, APL=False, APCMILP=False, delete_result=False) # Run all instances and don't delete previous results

    # APC-IP
    # r = data_revenue[1:]
    # mu = data_mu[1:]
    # langrangian_combination, langrangian_y0, langrangian_obj_val = lagrangian_dichotomic_search(mu, r, data_revenue[0], 10, len(r))
    # print("Lagrangian relaxation:")
    # print("Optimal value:", langrangian_obj_val)
    # print("Optimal solution:", langrangian_combination)
    # print("y0:", langrangian_y0)
    
    # AP-L
    # apl_model = APL_model(data_revenue, data_mu)
    # apl_model.optimize()
    # print("Optimal value:", apl_model.objVal)
    # print("Optimal solution:")
    # for v in apl_model.getVars():
    #     print(v.varName, v.x)
    
    # Greedy algorithm for AP
    # greedy_score, greedy_combination = greedy_algorithm_AP(data_revenue, data_mu)
    # print("Greedy algorithm:")
    # print("Optimal value:", greedy_score)
    # print("Optimal solution:", greedy_combination)
    
    # APC-MILP
    # apc_milp_model = APC_MILP(data_revenue, data_mu)
    # apc_milp_model.optimize()
    # print("Optimal value:", apc_milp_model.objVal)
    # print("Optimal solution:")
    # for v in apc_milp_model.getVars():
    #     print(v.varName, v.x)

