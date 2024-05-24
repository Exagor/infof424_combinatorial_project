# INFO-F424 – Combinatorial Optimization Project

## Introduction

In this project, we focus on the Assortment Planning Problem (AP), where a retailer wants to determine
which products it has to propose to its customers in order to maximize its expected revenue. More precisely,
consider a set of products $\mathcal{I} = {1, . . . , n}$ that the retailer can propose to its customers, and selling product
$i$ generates a net revenue of $r_i > 0$ for him. We assume that the products are sorted in decreasing order of
revenue, i.e. $r_1 > r_2 > · · · > r_n > 0$, and that each product $i$ will be purchased according to a particular
probability that depends on:

1. The mean utilities $\mu_j, j \in \mathcal{I}$ for the customers when they buy product $j \in \mathcal{I}$,
2. The set of alternatives $S$ made available to the customers.

These probabilities come from a discrete choice model called multinomial logit, and can be written as follows:

$$ P_i(S) = \frac{e^{\mu_i}}{e^{\mu_0}+ \sum_{j\in S}e^{\mu_j}}= \frac{e^{\mu_i}}{1+ \sum_{j\in S}e^{\mu_j}}, \quad \forall i \in \mathcal{I} \cup \{0\}$$

where $\mu_0 = 0$ represents the utility - for the customers - of buying nothing. As we will see later on, it is
convenient to assume that selling nothing does come with a revenue $r_0 \geq 0$ (that is, however, usually zero).\
With all of the above, the problem can be posed as the following combinatorial optimization problem :

$$ \text{(AP)} \quad \max_{S \subseteq \mathcal{I}} \Bigg\{ r_0 \cdot P_0(S) + \sum_{i \in S} r_i \cdot P_i(S) \Bigg\}$$
## How to run the code

press "run" button lol