"""
Run this file to have statistics about the instances
"""
import pandas as pd

def stats_all() :
    models = ["AP", "APL", "APC_MILP", "APC_IP"]
    sizes = [10, 5000, 1000000]

    for model in models:
        for size in sizes:
            path = "results/results_" + model + "_" + str(size) + ".csv"
            data = pd.read_csv(path, header=None, names=['instance', 'optimal value', 'time'])
            analysis = data.agg(['min', 'mean', 'max']) #aggregate the data
            analysis = analysis.drop('instance', axis=1) #drop the 'instance' column
            print("Results for", model, "with", size, "instances:")
            print(analysis)

def stats_APC_MILP():
    sizes = ["10", "5000", "1000000"]
    P = ["1", "N5", "N2", "N"]

    for size in sizes:
        for p in P:
            path = "results/APC_MILP/results_APC_MILP_" + size + "_" + p + ".csv"
            data = pd.read_csv(path, header=None, names=['instance', 'optimal value', 'time'])
            analysis = data.agg(['min', 'mean', 'max'])
            analysis = analysis.drop('instance', axis=1)
            print("Results for APC_MILP with", size, "instances for p =", p ,":")
            print(analysis)

stats_all()
stats_APC_MILP()