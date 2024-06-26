"""
In this file we can automatically do the test on one instance or on all instances of a given size.
"""
import time
from tqdm import tqdm
import pandas as pd
from APL import *
from APC_MILP import *
from AP import *
from APC_IP import *
from utilities import *

def APL_instances(instances_data_revenue, instances_data_mu, res_dir="results/"):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        apl_model = APL_model(data_revenue, data_mu)
        apl_model.optimize()
        save_result_gurobi(apl_model, res_dir+"results_APL_"+str(len(data_revenue)-1)+".csv", instance_nb=i)

def AP_instances(instances_data_revenue, instances_data_mu, res_dir="results/"):
    for i in range(len(instances_data_revenue.columns)):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        start_time = time.perf_counter()
        greedy_score, greedy_combination = greedy_algorithm_AP(data_revenue, data_mu)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        save_result(greedy_score, execution_time, res_dir+"results_AP_"+str(len(data_revenue)-1)+".csv", instance_nb=i)

def APC_MILP_instances(instances_data_revenue, instances_data_mu, res_dir="results/"):
    for i in tqdm(range(len(instances_data_revenue.columns))):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        apc_milp_model = APC_MILP(data_revenue, data_mu, time_limit=150)
        apc_milp_model.optimize()
        save_result_gurobi(apc_milp_model, res_dir+"results_APC_MILP_"+str(len(data_revenue)-1)+".csv", instance_nb=i)

def APC_IP_instances(instances_data_revenue, instances_data_mu, res_dir="results/"):
    for i in tqdm(range(len(instances_data_revenue.columns))):
        data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=i)
        N = len(data_revenue)
        start_time = time.perf_counter()
        lagrangian_combination, lagrangian_y0, lagrangian_obj_val = lagrangian_dichotomic_search(data_mu, data_revenue, N, N)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        save_result(lagrangian_obj_val,execution_time, res_dir+"results_APC_IP_"+str(len(data_revenue)-1)+".csv", instance_nb=i)

def run_all_sizes_and_instances(AP=True, APL=True, APCMILP=True, APCIP=True, delete_result=False):
    names = ["small", "medium", "extralarge"] #["small", "medium", "extralarge"]
    if delete_result:
        delete_files("results/")

    for name in names:
        print("Processing", name, "instances")
        size_name = name 
        instances_data_revenue = pd.read_csv("data/" + size_name+"-r.csv",sep=';',header=None)
        instances_data_mu = pd.read_csv("data/" + size_name + "-mu.csv",sep=';',header=None)
        if AP:
            print("Computing AP instances...")
            AP_instances(instances_data_revenue, instances_data_mu)
        if APL:
            print("Computing APL instances...")
            APL_instances(instances_data_revenue, instances_data_mu)
        if APCMILP:
            print("Computing APC-MILP instances...")
            APC_MILP_instances(instances_data_revenue, instances_data_mu)
        if APCIP:
            print("Computing APC-IP instances...")
            APC_IP_instances(instances_data_revenue, instances_data_mu)