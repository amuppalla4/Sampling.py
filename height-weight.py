import pandas as pd
import statistics
import csv
df=pd.read_csv("data2.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.mean(height_list)
weight_median=statistics.mean(weight_list)

height_mode=statistics.mean(height_list)
weight_mode=statistics.mean(weight_list)

print("mean,median,mode of height is {},{} and {} respectively".format(height_mean,height_median,height_mode))
print("mean,median,mode of weight is {},{} and {} respectively".format(weight_mean,weight_median,weight_mode))