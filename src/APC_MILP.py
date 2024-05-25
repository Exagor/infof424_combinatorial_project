import gurobipy as gb
from gurobipy import GRB
import numpy as np

def APC_MILP(data_revenue, data_mu, time_limit=60):
    #data
    r = data_revenue
    mu = data_mu
    N = len(r)
    p = N//5 # Max number of product that can be offered to the customer

    # Create a new model
    model = gb.Model("APC_MILP")

    # Create variables
   
    y = model.addVars(N,lb=0, vtype=GRB.CONTINUOUS, name="y")
    z = model.addVars(N, vtype=GRB.BINARY, name="z")

    # Add constraints
    model.addConstr(y[0] + gb.quicksum(y[i] for i in range(1,N)) == 1, name="c0")
    model.addConstr(gb.quicksum(z[i] for i in range(1,N)) <= p, name="c3")
    for i in range(1,N):
        model.addConstr(y[i] <= y[0] * np.exp(mu[i]) , name="c1_" + str(i))
        model.addConstr(y[i] <= z[i], name="c2_" + str(i))

    model.update()

    # Set objective
    model.setObjective(r[0]*y[0] + gb.quicksum((r[i]*y[i]) for i in range (1,N)), GRB.MAXIMIZE)

    model.update()

    return model