####### Clear all
for name in dir():
    del globals()[name]
del name

####### Import necessary libraries
import math as m # from math import * # Another way of importing libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.close('all');

###### Load data
train_file = '/home/amir/Dropbox/Python_codes/GIT_repositories/Kaggle_Titanic/Data/train.csv';
train_data = pd.read_csv(train_file);

test_file = '/home/amir/Dropbox/Python_codes/GIT_repositories/Kaggle_Titanic/Data/test.csv';
test_data = pd.read_csv(test_file)

###### Extract a few attributes from the train data table
train_Age = train_data['Age'].values;
train_Survived = train_data['Survived'].values;
train_Fare = train_data['Fare'].values;
train_Parch = train_data['Parch'].values;
train_N_subject = np.size(train_Age); # Number of subjects in the training dataset

train_Age_range = np.linspace(1,np.size(train_Age),train_N_subject);
train_Survived_range = np.linspace(1,np.size(train_Survived),train_N_subject);
train_Fare_range = np.linspace(1,np.size(train_Fare),train_N_subject);
train_Parch_range = np.linspace(1,np.size(train_Parch),train_N_subject);


###### Plot some of the attributes
f, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2);

ax1.plot(train_Age_range,train_Age)
ax1.set_xlabel('Subject ID')
ax1.set_ylabel('Age')

ax2.plot(train_Survived_range,train_Survived)
ax2.set_xlabel('Subject ID')
ax2.set_ylabel('Survived')
ax2.set_ylim(-1,2)

ax3.plot(train_Fare_range,train_Fare)
ax3.set_xlabel('Subject ID')
ax3.set_ylabel('Fare')

ax4.plot(train_Parch_range,train_Parch)
ax4.set_xlabel('Subject ID')
ax4.set_ylabel('Parch')

plt.show()






