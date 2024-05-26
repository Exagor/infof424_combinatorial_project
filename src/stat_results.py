import pandas as pd

def stats_all() :
    models = ["AP", "APL", "APC_MILP"]
    sizes = [10, 5000, 100000, 1000000]

    for model in models:
        for size in sizes:
            path = "results/results_" + model + "_" + str(size) + ".csv"
            data = pd.read_csv(path, header=None, names=['instance', 'optimal value', 'time'])
            analysis = data.agg(['min', 'mean', 'max']) #aggregate the data
            analysis = analysis.drop('instance', axis=1) #drop the 'instance' column
            print("Results for", model, "with", size, "instances:")
            print(analysis)

def stats_APC_MILP():
    print("yello wirld ?")



stats_all()