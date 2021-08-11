import plotly.figure_factory as ff 
import statistics
import random
import pandas as pd 
import csv

df = pd.read_csv('data.csv')
data = df['temp'].tolist()
population_mean = statistics.mean(data)
fig = ff.create_distplot([data],['temp'], show_hist = False)
#fig.show()
std_deviation = statistics.stdev(data)
print(std_deviation)
print(population_mean)

# code to find out the 100 deviation points
dataset = []
for i in range(0,1000):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)
print(std_deviation)

def random_set_of_mean(counter):
    dataset= []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean 

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],['temp'],show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
print(mean)
setup()



