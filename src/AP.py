import numpy as np

def probability_of_choice(mu,i,S):
    return (np.exp(mu[i]))/(1+sum(np.exp(mu[j]) for j in S))

def greedy_algorithm_AP(r, mu):
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
        



