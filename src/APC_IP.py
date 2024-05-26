import numpy as np


def lagrangian_relaxation(n, mu, r, r0, lambda_val, p):
    # Adjust marginal utilities for the Lagrangian multiplier
    utilities = r * np.exp(mu) - lambda_val * np.exp(mu)
    
    # Select the top-p items based on marginal utilities
    sorted_indices = np.argsort(-utilities)
    selected_indices = sorted_indices[:p]
    
    # Create y based on selected indices
    y = np.zeros(n)
    for i in selected_indices:
        y[i] = np.exp(mu[i])

    y0 = 1 / (1 + np.sum(y))
    y = y*y0
    
    obj_val = (r0 + np.sum(y * r * np.exp(mu)))/(1 + np.sum(y * np.exp(mu))) - lambda_val * (np.sum(y) - p * y0)
    return y, y0, obj_val, np.sum(y) - p * y0



def lagrangian_dichotomic_search(mu, r, r0, p, n, max_iter=100, tol=1e-6):
    best_obj_val = -np.inf
    best_y = None
    best_y0 = None

    # Bounds for lambda
    lambda_low = 0
    lambda_up = (max(r) - r0)/p

    for _ in range(max_iter): # index of loop is not used
        lambda_val = (lambda_low + lambda_up) / 2
        y, y0, obj_val, violation = lagrangian_relaxation(n, mu, r, r0, lambda_val, p)

        if obj_val > best_obj_val:
            best_obj_val = obj_val
            best_y = y
            best_y0 = y0

        if(np.abs(violation) < tol):
            break

        if violation > 0:
            lambda_low = lambda_val

        else:
            lambda_up = lambda_val

        return best_y, best_y0, best_obj_val
