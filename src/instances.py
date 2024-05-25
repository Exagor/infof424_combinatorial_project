import time
from APL import *
from APC_MILP import *
from AP import *
from utilities import *

def APL_instances(instances_data_revenue, instances_data_mu):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        apl_model = APL_model(data_revenue, data_mu)
        apl_model.optimize()
        save_result_gurobi(apl_model, "results/results_APL.csv", instance_nb=i, size_instance=len(data_revenue)-1)

def AP_instances(instances_data_revenue, instances_data_mu):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        start_time = time.perf_counter()
        greedy_score, greedy_combination = greedy_algorithm2(data_revenue, data_mu)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        save_result(greedy_score, execution_time, "results/results_AP.csv", instance_nb=i, size_instance=len(data_revenue)-1)

def APC_MILP_instances(instances_data_revenue, instances_data_mu):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        apc_milp_model = APC_MILP(data_revenue, data_mu)
        apc_milp_model.optimize()
        save_result_gurobi(apc_milp_model, "results/results_APC_MILP.csv", instance_nb=i, size_instance=len(data_revenue)-1)