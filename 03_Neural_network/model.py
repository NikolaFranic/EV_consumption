import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import model_selection
import Neural_Network as nn

np.random.seed(1)
# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

# loading dataset
dataset = pd.read_excel("Cleaned_dataset.xls")
dataset.drop(dataset.columns[0],axis=1,inplace=True)

# creating splits
train_dataset = dataset.drop(["Range WLTP (electric)"],axis=1)
test_dataset = dataset["Range WLTP (electric)"]


train_x, test_x, train_y, test_y = sklearn.model_selection.train_test_split(train_dataset,test_dataset, test_size=0.2, random_state=0)
train_x = np.reshape(train_x.values,(2,len(train_x)))
test_x = np.reshape(test_x.values,(2,len(test_x)))
train_y = np.reshape(train_y.values,(1,len(train_y)))
test_y = np.reshape(test_y.values,(1,len(test_y)))
print(train_x.shape)
# constants
layers_dims = [len(train_x),5,3, 1] #  3-layer model

# train model
def plot_costs(costs, learning_rate=0.0075):
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per hundreds)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()

#parameters, costs = nn.L_layer_model(train_x, train_y, layers_dims, num_iterations = 2500, print_cost = True)
#plot_costs(costs)


