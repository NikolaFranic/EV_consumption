import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

column_names = ['Broad',"Height","Curb weight (EU)","Consumption combined (WLTP)"]

raw_dataset = pd.read_excel("ADAC_Database_eng.xls")

# extract only influential factors and range values
dataset = raw_dataset[column_names]

# CLEANING DATA
# separating only numeric value
dataset["Broad"]= dataset["Broad"].str[:-2]
dataset["Height"] = dataset["Height"].str[:-2]
dataset["Curb weight (EU)"] = dataset["Curb weight (EU)"].str[:-2]
dataset["Consumption combined (WLTP)"] = dataset["Consumption combined (WLTP)"].str[:-9]

# removing duplicates and empty cells
dataset.replace("",np.nan, inplace=True)
dataset.dropna(inplace=True) # removing rows with unknown values
dataset.drop_duplicates(inplace=True) # removing duplicates

dataset = dataset.reset_index(drop=True)

# removing rows with unexpected data
for col in range(len(dataset.columns)):
    for row in reversed(range(len(dataset))):
        try:
            dataset.iloc[row][col] = pd.to_numeric(dataset.iloc[row][col])
        except:
            dataset.drop([row],axis=0,inplace=True)
            dataset = dataset.reset_index(drop=True)

dataset = dataset.astype(float)

#creating the frontal area column = width*height

frontal_area = dataset["Broad"]*dataset["Height"]
dataset.insert(0,"Frontal_area",frontal_area)
dataset.drop(["Broad","Height"],axis=1,inplace=True)


# visualizations

def visualization(x,y,x_name,y_name):
    a, b = np.polyfit(x, y, 1)
    plt.scatter(x, y)
    plt.plot(x, a * x + b, color="red")
    plt.title("Correlation between " + x_name + " and " + y_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


visualization(dataset["Consumption combined (WLTP)"], dataset["Curb weight (EU)"],"Consumption","Weight")
visualization(dataset["Consumption combined (WLTP)"], dataset["Frontal_area"],"Consumption","Frontal area")

dataset.to_excel("Cleaned_dataset.xlsx")









