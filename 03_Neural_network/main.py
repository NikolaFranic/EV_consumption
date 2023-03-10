import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import Neural_Network as nbb

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

# import dataset
dataset = pd.read_excel("Cleaned_dataset.xls")
dataset.drop(dataset.columns[0],axis=1,inplace=True)

# make splits
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# visual inspection
sns.pairplot(train_dataset[['Consumption combined (WLTP)', 'Curb weight (EU)', 'Frontal_area']], diag_kind='kde')
plt.show()

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('Consumption combined (WLTP)')
test_labels = test_features.pop('Consumption combined (WLTP)')

# network
normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(np.array(train_features))

dnn_model = nbb.build_and_compile_model(normalizer)
dnn_model.summary()

history = dnn_model.fit(
    train_features,
    train_labels,
    verbose=0, epochs=100)

# plot loss
plt.plot(history.history['loss'], label='loss')
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.legend()
plt.grid(True)
plt.show()


test_predictions = dnn_model.predict(test_features).flatten()

# print error
print("Mean Absolute Error: " + str(dnn_model.evaluate(test_features, test_labels, verbose=0)))

# plot predictions - true values
a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
lims = [0, 40]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)
plt.show()

# plot error
error = test_predictions - test_labels
plt.hist(error, bins=25)
plt.xlabel('Prediction Error [Consumption]')
_ = plt.ylabel('Count')
plt.show()

# save model
dnn_model.save('nn_model')