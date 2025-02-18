# Catherine Donner 
# CS 5013 Homework 5
# Task 2: Logistic Regression 

# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Load data 
data = np.loadtxt('diabetes.csv', delimiter=',')
[n,p] = np.shape(data)
# 75% for training, 25% for testing 
num_train = int(0.75*n)
num_test = int(0.25*n)
sample_train = data[0:num_train,0:-1]
label_train = data[0:num_train,-1]
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# Pick number of iterations 
num_iter = 1000
# Randomly initialize w 
w = np.random.rand(p - 1) # Number of columns minus target column

# Storage for testing classification error
er_test = []

# Set alpha learning rate
alpha = 0.01

# Implement the iterative learning algorithm for w
# At the end of each iteration, evaluate the updated w 
# For every iteration run algorithm
for iter in range(num_iter): 

	# Calculate training predictions
	linear_comb = np.dot(sample_train, w) # Linear combination of inputs and weights
	predictions_train = 1 / (1 + np.exp(-linear_comb)) # Sigmoid function for predictions

	# Compute gradient
	gradient = -(1/num_train) * np.dot(sample_train.T, (label_train - predictions_train))

	# Update w using learning rate and gradient
	w -= alpha * gradient

	# Evaluate testing error of the updated w 
	# measure classification error
	linear_comb_test = np.dot(sample_test, w) # Linear combination for testing data
	predictions_test = 1 / (1 + np.exp(-linear_comb_test)) # Sigmoid function again

	# Convert testing predictions to binary predictions
	binary_preds = (predictions_test >= 0.5).astype(int) # 0.5 is classification threshold
	er = np.mean(binary_preds != label_test) # Classification error: mean of all incorrect predictions
	er_test.append(er)
    
# Plot classification error vs. iteration of learned logistic regression
plt.figure()    
plt.plot(er_test)
plt.title('Classification Error of Iterative Learned Logistic Regression')
plt.xlabel('Iteration')
plt.ylabel('Classification Error')
plt.show()

# End of Task 2

