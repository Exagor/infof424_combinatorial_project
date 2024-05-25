import time
import pandas as pd
from APL import *
from APC_MILP import *
from AP import *
from utilities import *

def APL_instances(instances_data_revenue, instances_data_mu):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        apl_model = APL_model(data_revenue, data_mu)
        apl_model.optimize()
        save_result_gurobi(apl_model, "results/results_APL_"+str(len(data_revenue)-1)+".csv", instance_nb=i)

def AP_instances(instances_data_revenue, instances_data_mu):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        start_time = time.perf_counter()
        greedy_score, greedy_combination = greedy_algorithm2(data_revenue, data_mu)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        save_result(greedy_score, execution_time, "results/results_AP_"+str(len(data_revenue)-1)+".csv", instance_nb=i)

def APC_MILP_instances(instances_data_revenue, instances_data_mu):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        apc_milp_model = APC_MILP(data_revenue, data_mu, time_limit=150)
        apc_milp_model.optimize()
        save_result_gurobi(apc_milp_model, "results/results_APC_MILP_"+str(len(data_revenue)-1)+".csv", instance_nb=i)


def run_all_instances(delete_results=False):
    data_dir_path = "data/"
    names = ["small", "medium", "large", "extralarge"]
    if delete_results:
        delete_results("results/")

    for name in names:
        print("Processing", name, "instances")
        size_name = name 
        instances_data_revenue = pd.read_csv(data_dir_path + size_name+"-r.csv",sep=';',header=None)
        instances_data_mu = pd.read_csv(data_dir_path + size_name + "-mu.csv",sep=';',header=None)
        print("AP instances")
        AP_instances(instances_data_revenue, instances_data_mu)
        print("APL instances")
        APL_instances(instances_data_revenue, instances_data_mu)
        print("APC-MILP instances")
        APC_MILP_instances(instances_data_revenue, instances_data_mu)