import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("newdata.csv")
data=df["average"].tolist()
population_mean=statistics.mean(data)
standard_deviation=statistics.stdev(data)
print("mean", population_mean)
print("standard deviation",standard_deviation)
def random_set_of_mean(counter): 
    dataset = [] 
    for i in range(0, counter): 
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index] 
        dataset.append(value) 
    mean = statistics.mean(dataset) 
    return mean

def standard_deviation():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(100),
        mean_list.append(set_of_means)

    std_deviation=statistics.stdev(mean_list)
    print("standard deviation"), std_deviation

standard_deviation()