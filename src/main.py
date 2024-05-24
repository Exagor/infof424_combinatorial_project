import gurobipy as gp
import numpy as np
import pandas as pd

data_dir_path = "data/"
data_revenue = pd.read_csv(data_dir_path + "small-r.csv")
data_prob = pd.read_csv(data_dir_path + "small-mu.csv")

def read_data(data_revenue, data_prob):
    return data_revenue, data_prob

def assortment_planning(data_revenue, data_prob, time_limit=60):
    model = gp.Model("Assortment Planning")
    model.setParam('TimeLimit', time_limit)
    model.setParam('OutputFlag', 1) # 1 for verbose, 0 for silent

    # define variables

    # define constraints


    return model

if __name__ == "__main__":
    print("Hello World !")

