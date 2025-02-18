# CS 5013
# Catherine Donner
# Homework 4 Task 2

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge # This time use Ridge regression
from sklearn import metrics

# Load crime rate dataset again for regression
data = np.loadtxt('crimerate.csv', delimiter=',', skiprows=1)
[n,p] = np.shape(data)

# Use last 25% data for testing 
num_test = int(0.25*n)
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# Pick one percentage of data used for training 
# remember we should be able to observe overfitting with this pick 
# note: maximum percentage is 0.75 
per = 0.70 # Use 70% for this training
num_train = int(n*per)
sample_train = data[0:num_train,0:-1]
label_train = data[0:num_train,-1]

# Ridge model has a hyper-parameter alpha. Larger alpha means simpler model. 
# Pick 8 candidate values for alpha (in ascending order)
# A to observe both overfitting and underfitting from these values 
# Suggestion: the first value should be very small and the last should be large 
alpha_vec = [1e-10, 1e-05, 0.001, 0.01, 0.1, 1, 5, 10]

# Initialize training and testing MSE list storage
er_train_alpha = []
er_test_alpha = []

# For every alpha train the Ridge model
for alpha in alpha_vec: 

	# Pick ridge model, then set its hyperparameter 
	model = Ridge(alpha = alpha)
    
	# Train Ridge model
	model.fit(sample_train, label_train)
	
	# Calculate training and testing predictions using fitted model
	train_predictions = model.predict(sample_train)
	test_predictions = model.predict(sample_test)

	# Evaluate training error (MSE) and store it in "er_train"
	er_train = metrics.mean_squared_error(label_train, train_predictions)
	er_train_alpha.append(er_train)

	# Evaluate testing error (MSE) and store it in "er_test"
	er_test = metrics.mean_squared_error(label_test, test_predictions)
	er_test_alpha.append(er_test)

# Plot trainin and testing errors for the different values of alpha
plt.plot(alpha_vec,er_train_alpha, label='Training Error')
plt.plot(alpha_vec,er_test_alpha, label='Testing Error')
plt.xlabel('Hyper-Parameter Alpha')
plt.ylabel('Prediction Error (MSE)')
plt.title('Prediction Error (MSE) vs. Alpha')
plt.legend()
plt.show()

# END OF TASK 2

