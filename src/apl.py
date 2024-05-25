import gurobipy as gp
from gurobipy import GRB
import numpy as np


def APL_model(data_revenue, data_mu, time_limit=60):
    model = gp.Model("AP-L")
    model.setParam('TimeLimit', time_limit)
    model.setParam('OutputFlag', 1) # 1 for verbose, 0 for silent

    # define parameters (constants for constraints and objective function)
    I = len(data_revenue) # number of products
    r = data_revenue # revenue of product i
    mu = data_mu # mean utility of product i

    # define variables
    y = model.addVars(I,lb=0, vtype=GRB.CONTINUOUS, name="y") #lb for lower bound
    # y0 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y0")

    # define constraints
    model.addConstr(y[0] + gp.quicksum(y[i] for i in range(I))==1, name="c0")
    for i in range(I):
        model.addConstr(y[i] <= y[0]*np.exp(mu[i]), name="c1_" + str(i)) #all constraints for i in I

    model.update()

    # define objective function
    model.setObjective(r[0]*y[0] + gp.quicksum(r[i]*y[i] for i in range(I)), GRB.MAXIMIZE)
    model.update()

    return model