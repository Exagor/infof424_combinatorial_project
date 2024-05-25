import gurobipy as gb
from gurobipy import GRB
import numpy as np

def APC_MILP(data_revenue, data_mu, time_limit=60):
    model = gb.Model("APC_MILP")
    model.setParam('TimeLimit', time_limit)
    model.setParam('OutputFlag', 1) 

    # Define parameters
    r = data_revenue
    mu = data_mu
    N = len(r)
    p = N # Max number of product that can be offered to the customer [1, N//5, N//2, N]

    # Create variables
    y = model.addVars(N,lb=0, vtype=GRB.CONTINUOUS, name="y")
    z = model.addVars(N, vtype=GRB.BINARY, name="z")

    # Add constraints
    model.addConstr(y[0] + gb.quicksum(y[i] for i in range(1,N)) == 1, name="c0")
    for i in range(1,N):
        model.addConstr(y[i] <= y[0] * np.exp(mu[i]) , name="c1_" + str(i))
        model.addConstr(y[i] <= z[i], name="c2_" + str(i)) #we suppose that it's y[i] and z[i]
    model.addConstr(gb.quicksum(z[i] for i in range(1,N)) <= p, name="c3")
    model.update()

    # Set objective
    model.setObjective(r[0]*y[0] + gb.quicksum((r[i]*y[i]) for i in range (1,N)), GRB.MAXIMIZE)
    model.update()

    return model