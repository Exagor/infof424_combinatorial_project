import pandas as pd
from APL import *
from APC_MILP import *
from AP import *
from utilities import *


data_dir_path = "data/"
size_name = "small" #or medium or large
instances_data_revenue = pd.read_csv(data_dir_path + size_name+"-r.csv",sep=';',header=None)
instances_data_mu = pd.read_csv(data_dir_path + size_name + "-mu.csv",sep=';',header=None)

def APL_instances(instances_data_revenue, instances_data_mu):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        apl_model = APL_model(data_revenue, data_mu)
        apl_model.optimize()
        save_result_gurobi(apl_model, "results/results_APL.csv", instance_nb=i, size_instance=len(data_revenue)-1)

def AP_instances(instances_data_revenue, instances_data_mu):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        greedy_score, greedy_combination = greedy_algorithm2(data_revenue, data_mu)
        save_result(greedy_score, "results/results_AP.csv", instance_nb=i, size_instance=len(data_revenue)-1)

if __name__ == "__main__":
    data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=0)
    # AP-L
    # apl_model = APL_model(data_revenue, data_mu)
    # apl_model.optimize()
    # print("Optimal value:", apl_model.objVal)
    # print("Optimal solution:")
    # for v in apl_model.getVars():
    #     print(v.varName, v.x)
    
    # Greedy algorithm for AP
    # greedy_score, greedy_combination = greedy_algorithm2(data_revenue, data_mu)
    # print("Greedy algorithm:")
    # print("Optimal value:", greedy_score)
    # print("Optimal solution:", greedy_combination)
    AP_instances(instances_data_revenue, instances_data_mu)
    
    # APC-MILP
    # apc_milp_model = APC_MILP(data_revenue, data_mu)
    # apc_milp_model.optimize()
    # print("Optimal value:", apc_milp_model.objVal)
    # print("Optimal solution:")
    # for v in apc_milp_model.getVars():
    #     print(v.varName, v.x)

