# Catherine Donner
# CS 5013 Homework 5
# Task 1: Linear Regression 

# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Load data 
data = np.loadtxt('crimerate.csv', delimiter=',')
[n,p] = np.shape(data)
# 75% for training, 25% for testing 
num_train = int(0.75*n)
num_test = int(0.25*n)
sample_train = data[0:num_train,0:-1]
label_train = data[0:num_train,-1]
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# Pick number of iterations 
num_iter = 25
# Randomly initialize w 
w = np.random.rand(p - 1) # Number of columns minus target

# Testing error storage
er_test = []

# Set alpha learning rate
alpha = 0.01

# Implement the iterative learning algorithm for w
# at the end of each iteration, evaluate the updated w 
# Iterate through number of iterations
for iter in range(num_iter): 

	# Calculate training predictions
	predictions_train = np.dot(sample_train, w)

	# Compute gradient
	gradient = -(1 / num_train) * np.dot(sample_train.T, (label_train - predictions_train))

	# Update w using learning rate and gradient
	w -= alpha * gradient

	# Evaluate testing error of the updated w 
	# Use mean-square-error (MSE)
	predictions_test = np.dot(sample_test, w) # Do testing predictions
	er = np.mean((label_test - predictions_test) ** 2) # Formula for MSE
	er_test.append(er)
    
# Plot MSE vs. Iteration of learned linear regression algorithm
plt.figure()    
plt.plot(er_test)
plt.title('MSE for Iterative Learned Linear Regression')
plt.xlabel('Iteration')
plt.ylabel('MSE')
plt.show()

# End of Task 1
