fileName = "./dataset/svg_meta.csv"

from pandas import *
from matplotlib import pyplot as plt
import numpy as np
 
# reading CSV file
data = read_csv(fileName)
 
# converting column data to list
total_len = data['total_len'].tolist()
nb_groups = data['nb_groups'].tolist()


fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(nb_groups, bins=[a for a in range(0,50,5)])
# nb_groups
# ax.hist(total_len, bins=[a for a in range(0,1000,50)])
plt.xlim([0, 100])
 
# Show plot
plt.show()
