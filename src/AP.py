import numpy as np

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

def probability_of_choice(mu,i,S):
    return (np.exp(mu[i]))/(1+sum(np.exp(mu[j]) for j in S))

def greedy_algorithm2(r, mu):
    I = len(r)
    S=[]
    # S.append(0)

    best_combination = []
    best_score = 0

    for i in range(1,I):
        S.append(i) #add products one by one because they are sorted by revenue
        score = r[0]*probability_of_choice(mu,0,S) + sum(r[j]*probability_of_choice(mu,j,S) for j in S)
        if score >= best_score:
            best_score = score
            best_combination = S.copy()
        else:
            S.remove(i)
            break

    return best_score, best_combination
        



