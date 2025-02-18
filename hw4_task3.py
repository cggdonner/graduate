# CS 5013
# Catherine Donner
# Homework 4 Task 3

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge # Use Ridge Regression
from sklearn.metrics import mean_squared_error # Use MSE for calculating validation error
from sklearn.utils import shuffle

# Load crime rate dataset for this regression task
data = np.loadtxt('crimerate.csv', delimiter=',', skiprows=1)
[n,p] = np.shape(data)

# Use last 25% data for testing 
num_test = int(0.25*n)
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# Pick the percentage of data used for training 
# Observe overfitting with this pick 
# Note: maximum percentage is 0.75 
per = 0.7 # Use 70% training
num_train = int(n*per)
sample_train = data[0:num_train,0:-1]
label_train = data[0:num_train,-1]

# Pick 5 candidate values for alpha using Ridge (in ascending order)
# Aim to observe both overfitting and underfitting from these values 
# Suggestion: the first value should be very small and the last should be large 
alpha_vec = [0.0001, 0.01, 0.1, 1, 10]

# Initialize training testing and validation error storage lists
er_train_alpha = []
er_test_alpha = []
er_valid_alpha = []

# Set number of folds, number of samples in training, and array of indices
k = 5 # Use 5 folds
n = sample_train.shape[0]
indices = np.arange(n)
np.random.shuffle(indices)

# Calculate size of each fold
fold_size = n // k

# For every alpha hyperparameter, do k-fold cross validation on training set
for alpha in alpha_vec: 

	# Initialize Ridge model, then set its hyperparameter 
	model = Ridge(alpha = alpha)

	# Store validation errors for each fold
	er_valid_folds = []

	# For every k-fold, get validation score for cross validation
	for fold in range(k):
		# Determine starting and ending indices for validation set
		start = fold * fold_size
		end = start + fold_size

		# Handle fold size division
		if fold == k - 1:
			end = n

		# Determine indices for validation set
		valid_indices = indices[start:end]

		# Remaining indices to form training set
		train_indices = np.concatenate([indices[:start], indices[end:]])

		# Split data into training and validation sets for this fold
		X_train, X_valid = sample_train[train_indices], sample_train[valid_indices]
		y_train, y_valid = label_train[train_indices], label_train[valid_indices]

		# Train Ridge model
		model.fit(X_train, y_train)		

		# Calculate predictions of validation set
		y_valid_pred = model.predict(X_valid)
		er_valid_mse = mean_squared_error(y_valid, y_valid_pred)

		# Append and store validation error from this fold
		er_valid_folds.append(er_valid_mse)

	# Average validation error for k-folds for this alpha
	er_valid = np.mean(er_valid_folds)

	# Store validation error for the alpha
	er_valid_alpha.append(er_valid)

# Print er_valid_alpha for the alpha values
print(er_valid_alpha)


# Compare the candidate values and pick the alpha that gives the smallest error 
# set it to "alpha_opt"
#alpha_opt = ...

# now retrain your model on the entire training set using alpha_opt 
# then evaluate your model on the testing set 
#model = Ridge(alpha = alpha_opt)
# ......
# ......
# .....
#er_train = ...
#er_test = ...

# END OF TASK 3
