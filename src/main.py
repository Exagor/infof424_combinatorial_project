import gurobipy as gp
from gurobipy import GRB
import numpy as np
import pandas as pd

data_dir_path = "data/"
data_revenue = pd.read_csv(data_dir_path + "small-r.csv",sep=';')
data_prob = pd.read_csv(data_dir_path + "small-mu.csv",sep=';')
print(data_revenue.head())
print(data_revenue.shape)

def read_data(data_revenue, data_prob):
    return data_revenue, data_prob

def assortment_planning(data_revenue, data_prob, time_limit=60):
    model = gp.Model("Assortment Planning")
    model.setParam('TimeLimit', time_limit)
    model.setParam('OutputFlag', 1) # 1 for verbose, 0 for silent

    # define variables
    I = data_revenue.shape[0] # set of products

    x = {} # decision variable (1 if product i is selected, 0 otherwise)
    for i in range(data_revenue.shape[0]):
        x[i] = model.addVar(vtype=GRB.BINARY, name="x[%d]" % i)

    r = {} #revenue of product i
    for i in range(data_revenue.shape[0]):
        r[i] = model.addVar(vtype=GRB.CONTINUOUS, name="r[%d]" % i) # or %s i don't know

    mu = {} # mean utility of product i
    for i in range(data_prob.shape[0]):
        mu[i] = model.addVar(vtype=GRB.CONTINUOUS, name="mu[%d]" % i)

    S = {} #set of choice for the customer
    # define probability

    P = {} # probability of customer choosing product i depending on the assortment
    for i in range(data_prob.shape[0]):
        P[i] = model.addVar(vtype=GRB.CONTINUOUS, name="P[%d]" % i)

    # define constraints

    model.update()

    # define objective function
    model.setObjective(r[0]*P[0] + gp.quicksum(r[i]*P[i]), GRB.MAXIMIZE)

    return model

if __name__ == "__main__":
    print("Hi word")
    # assortment_model = assortment_planning(data_revenue, data_prob)
    # assortment_model.optimize()

