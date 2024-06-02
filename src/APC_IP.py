import numpy as np
import gurobipy as gp
import matplotlib.pyplot as plt


def lagrangian_relaxation(n, mu, r, lambda_val, p):
    model = gp.Model("AP-L(λ)")
    model.setParam('OutputFlag', 0) # 1 for verbose, 0 for silent

    # Define variables
    #y0 = model.addVar(lb=0, vtype=gp.GRB.CONTINUOUS, name="y0")
    y = model.addVars(n,lb=0, vtype=gp.GRB.CONTINUOUS, name="y")

    # Define constraints
    model.addConstr(y[0] + gp.quicksum(y[i] for i in range(n)) == 1, name="c0")
    for i in range(1, n):
        model.addConstr(y[i] <= y[0] * np.exp(mu[i]), name="c1_" + str(i))
    
    # Set objective
    model.setObjective(((r[0] + (lambda_val * p)) * y[0]) + gp.quicksum((((r[i]*np.exp(mu[i]) - lambda_val)/np.exp(mu[i])) * y[i]) for i in range(1, n)), gp.GRB.MAXIMIZE)

    model.update()

    model.optimize()

    y0_val = y[0].X
    y_val = [y[i].X for i in range(n)]
    obj_val = model.objVal

    return y_val, y0_val, obj_val

def is_feasible(y, p):
    return sum(1 for yi in y if yi > 0) <= p

def lagrangian_dichotomic_search(mu, r, p, n, max_iter=100, tol=1e-6):
    best_obj_val = np.inf
    best_y = None
    best_y0 = None
    obj_vals = []
    lambdas = []

    # Bounds for lambda
    lambda_low = 0
    lambda_up = (r[1] - r[0])/p

    for _ in range(max_iter): # index of loop is not used
        lambda_val = (lambda_low + lambda_up) / 2
        y, y0, obj_val = lagrangian_relaxation(n, mu, r, lambda_val, p)

        obj_vals.append(obj_val)
        lambdas.append(lambda_val)
        if is_feasible(y, p):
            if obj_val < best_obj_val:
                best_obj_val = obj_val
                best_y = y
                best_y0 = y0

        if obj_val < lagrangian_relaxation(n, mu, r, lambda_val + tol, p)[2]:
            lambda_up = lambda_val

        else:
            lambda_low = lambda_val

        if(lambda_up - lambda_low < tol):
            break

    print(lambdas)
    print(obj_vals)
    plot_bounds(obj_vals, lambdas)

    return best_y[1:], best_y0, best_obj_val

def plot_bounds(obj_vals, lambdas):
    
    plt.plot(lambdas, obj_vals)
    plt.xlabel("λ")
    plt.ylabel("Objective value")
    plt.title("Objective value as a function of λ")
    plt.show()
