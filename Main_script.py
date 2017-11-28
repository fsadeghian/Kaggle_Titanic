####### Clear all
for name in dir():
    del globals()[name]
del name

####### Import necessary libraries
import math as m # from math import * # Another way of importing libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

###### Load data
train_file = '/home/amir/Dropbox/Python_codes/GIT_repositories/Kaggle_Titanic_competition/Data/train.csv';
train_data = pd.read_csv(train_file)

test_file = '/home/amir/Dropbox/Python_codes/GIT_repositories/Kaggle_Titanic_competition/Data/test.csv';
test_data = pd.read_csv(test_file)

###### Plot some of the attributes
print train_data.head(1)
train_data['Age'].hist(bins=50)
plt.show()

