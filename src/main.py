import pandas as pd
from APL import *
from APC_MILP import *

data_dir_path = "data/"
size_name = "large" #or medium or large
instances_data_revenue = pd.read_csv(data_dir_path + size_name+"-r.csv",sep=';',header=None)
instances_data_mu = pd.read_csv(data_dir_path + size_name + "-mu.csv",sep=';',header=None)

def read_instance(instances_data_revenue, instances_data_mu, instance=0):
    data_revenue = instances_data_revenue.iloc[:,instance] #we use iloc to select the column
    data_mu = instances_data_mu.iloc[:,instance]
    return data_revenue.tolist(), data_mu.tolist()

if __name__ == "__main__":
    # AP-L
    data_revenue, data_mu = read_instance(instances_data_revenue, instances_data_mu, instance=0)
    apl_model = APL_model(data_revenue, data_mu)
    apl_model.optimize()
    print("Optimal value:", apl_model.objVal)
    print("Optimal solution:")
    for v in apl_model.getVars():
        print(v.varName, v.x)
    
    # APC-MILP
    apc_milp_model = APC_MILP(data_revenue, data_mu)
    apc_milp_model.optimize()
    print("Optimal value:", apc_milp_model.objVal)
    print("Optimal solution:")
    for v in apc_milp_model.getVars():
        print(v.varName, v.x)

