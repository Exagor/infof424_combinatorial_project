import pandas as pd

models = ["AP", "APL", "APC_MILP"]
sizes = [10, 5000, 100000, 1000000]

for model in models:
    for size in sizes:
        path = "results/results_" + model + "_" + str(size) + ".csv"
        data = pd.read_csv(path, header=None, names=['instance', 'score', 'time'])
        analysis = data.agg(['mean', 'min', 'max']) #aggregate the data
        analysis = analysis.drop('instance', axis=1) #drop the 'instance' column
        print("Results for", model, "with", size, "instances:")
        print(analysis)
