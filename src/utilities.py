import csv


def read_instance(instances_data_revenue, instances_data_mu, instance=0):
    data_revenue = instances_data_revenue.iloc[:,instance] #we use iloc to select the column
    data_mu = instances_data_mu.iloc[:,instance]
    return data_revenue.tolist(), data_mu.tolist()

def save_result_gurobi(model, filename, instance_nb, size_instance):
    with open(filename, mode='a',newline="") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([instance_nb, size_instance, model.objVal, model.Runtime])

def save_result(score, time, filename, instance_nb, size_instance):
    with open(filename, mode='a',newline="") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([instance_nb, size_instance, score, time])