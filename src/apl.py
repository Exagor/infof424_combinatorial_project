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
    model.addConstr(y[0] + gp.quicksum(y[i] for i in range(1,I))==1, name="c0")
    for i in range(1,I):
        model.addConstr(y[i] <= y[0]*np.exp(mu[i]), name="c1_" + str(i)) #all constraints for i in I

    model.update()

    # define objective function
    model.setObjective(r[0]*y[0] + gp.quicksum(r[i]*y[i] for i in range(1,I)), GRB.MAXIMIZE)
    model.update()

    return model

def greedy_algorithm(r, mu):

    I = len(r)
    best_revenue = 0
    best_combination = None

    sorted_indices = np.argsort(r)[::-1]

    for k in range(I-1):
        den = (1 + sum(np.exp(mu[j]) for j in range(1,k+1)))
        y_0 = 1 / den
        y = [0]*(I-1)

        for i in range(k+1):
            y[sorted_indices[i-1]] = y_0*np.exp(mu[sorted_indices[i-1]])

        revenue = r[0]*y_0 + sum(r[i]*y[i] for i in range(I-1))

        if revenue > best_revenue:
            best_revenue = revenue
            best_combination = (y_0, y)

    return best_revenue, best_combination
