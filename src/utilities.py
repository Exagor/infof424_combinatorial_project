import csv
import os


def read_instance(instances_data_revenue, instances_data_mu, instance=0):
    data_revenue = instances_data_revenue.iloc[:,instance] #we use iloc to select the column
    data_mu = instances_data_mu.iloc[:,instance]
    return data_revenue.tolist(), data_mu.tolist()

def save_result_gurobi(model, filename, instance_nb):
    with open(filename, mode='a',newline="") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([instance_nb, model.objVal, "{:.19f}".format(model.Runtime)])

def save_result(score, time, filename, instance_nb):
    with open(filename, mode='a',newline="") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([instance_nb, score, time])

def delete_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)