# Catherine Donner
# CS 5013
# Homework 7 Task 3

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier # Multilayer perceptron
from sklearn.metrics import accuracy_score

# Import diabetes dataset
data = np.loadtxt('diabetes.csv', delimiter=',', skiprows=1)
[n,p] = np.shape(data)

# training data
num_train = int(0.5*n)
sample_train = data[0:num_train,0:-1]
label_train = data[0:num_train,-1]
# testing data
num_test = int(0.5*n)
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# Fix neurons per layer to 10
k = 10
# Fix number of layers to 20
m = 20
# List of activation functions
a_func = ['identity', 'logistic', 'tanh', 'relu']

# Initialize training and testing error storage
er_train_a = []
er_test_a = []
# Iterate MLP training for every activation function a
for a in a_func:

        # train a MLP classification model
        layer_sizes = tuple([k]*m) # Define layer size
        # Initialize MLP model with layer sizes and activation a
        model = MLPClassifier(hidden_layer_sizes=layer_sizes, activation=a, max_iter=1000, random_state=42)
        # Train model
        model.fit(sample_train, label_train)

        # evaluate training error and testing error
        # First calculate predictions
        pred_train = model.predict(sample_train) # Training
        pred_test = model.predict(sample_test) # Testing
        er_train = 1 - accuracy_score(pred_train, label_train)
        er_test = 1 - accuracy_score(pred_test, label_test)
        # Add errors to lists
        er_train_a.append(er_train)
        er_test_a.append(er_test)

# Print training and testing error lists
print("Training Classification Errors: ", er_train_a)
print("Testing Classification Errors: ", er_test_a)

# End of Task 3














































