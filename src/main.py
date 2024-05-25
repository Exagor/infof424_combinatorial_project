import gurobipy as gp
from gurobipy import GRB
import numpy as np
import pandas as pd
import apl
import APC_MILP

data_dir_path = "data/"
instances_data_revenue = pd.read_csv(data_dir_path + "small-r.csv",sep=';',header=None)
instances_data_mu = pd.read_csv(data_dir_path + "small-mu.csv",sep=';',header=None)

def read_instance(instances_data_revenue, instances_data_mu, instance=0):
    data_revenue = instances_data_revenue.iloc[:,instance] #we use iloc to select the column
    data_mu = instances_data_mu.iloc[:,instance]
    return data_revenue.tolist(), data_mu.tolist()


    

if __name__ == "__main__":
    data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=0)
    apl_model = apl.APL_model(data_revenue, data_mu)
    apl_model.optimize()
    print("Optimal value:", apl_model.objVal)
    print("Optimal solution:")
    for v in apl_model.getVars():
        print(v.varName, v.x)
    
    """
    apc_milp_model = APC_MILP.APC_MILP(data_revenue, data_mu)
    apc_milp_model.optimize()
    print("Optimal value:", apc_milp_model.objVal)
    print("Optimal solution:")
    for v in apc_milp_model.getVars():
        print(v.varName, v.x)
    """
    greedy_revenue, greedy_combination = apl.greedy_algorithm(data_revenue, data_mu)
    print("Greedy algorithm:")
    print("Optimal value:", greedy_revenue)
    print("Optimal solution:", greedy_combination)

