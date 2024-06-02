# INFO-F424 – Combinatorial Optimization Project

June 2024
By Achten Alexandre and Boistel Julien\

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

$$ \text{(AP)} \quad \max_{S \subseteq \mathcal{I}} \{ r_0 \cdot P_0(S) + \sum_{i \in S} r_i \cdot P_i(S) \}$$

## How to run the code

### Install the required packages

```sh
pip install -r requirements.txt
```

### Modify the main.py file

You can modify the parameters of the problem, such as the revenue file and the mean utilities file directly in the main.\
Then you can run the main.py file to solve the problem.

```sh
python main.py
```

OR you can run the main.py file with the following arguments:

```sh
python main.py -r <revenue_file> -mu <mean_utilities_file> -m <modelisation> -results <results_directory>
```

The possible values for the modelisationare:

- 0: AP modelisation
- 1: AP-L modelisation
- 2: APC-MILP modelisation
- 3: APC-IP modelisation

### Example

```sh
python src/main.py -r data/small-r.csv -mu data/small-mu.csv -m 1 -results results/
```

### Results

The results will be saved in a file having the following template: `results_<modelisation>_<size_instance>.csv`.
Where the 3 columns are the instance name, the optimal value and the running time. WARNING : if several instances of the same size are run, the results will be appended to the same file

Example:

|Instance|Optimal Value|Running Time (s)|
|--------|-------------|------------|
|1|100| 0.5|
|2|200| 1.2|
|3|150| 0.8|
