# CS 5013
# Catherine Donner
# Homework 4 Task 4

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression # Use Logistic Regression for this task
from sklearn.metrics import accuracy_score # Non-MSE evaluation metric for classification

# Load diabetes dataset for classification 
# in array "data", each row represents a patient 
# each column represents an attribute of patients 
# last column is the binary label: 1 means the patient has diabetes, 0 means otherwise
data = np.loadtxt('diabetes.csv', delimiter=',', skiprows=1)
[n,p] = np.shape(data)

# Use last 25% data for testing 
num_test = int(0.25*n)
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# Vary the percentage of data used for training
# Pick 8 values for array "num_train_per" e.g., 0.5 means using 50% of the available data for training
# Aim to observe overiftting (and normal performance) from these 8 values
# Note: maximum percentage is 0.75
# Add lower values for training
num_train_per = [0.01, 0.05, 0.10, 0.15, 0.2, 0.3, 0.4, 0.5]

# Initialize training and testing MSE list storage
er_train_per = []
er_test_per = []

# For each percentage of training data
for per in num_train_per:

	# Create training data and labels
	num_train = int(n*per)
	sample_train = data[0:num_train,0:-1]
	label_train = data[0:num_train,-1]

	# Initialize logistic regression model
	model = LogisticRegression()

	# Train the model using training data
	model.fit(sample_train, label_train)

	# Calculate predictions of fitted model using training and testing data
	train_predictions = model.predict(sample_train)
	test_predictions = model.predict(sample_test)

	# Evaluate training error of model
	# Store in "er_train"
	er_train_acc = accuracy_score(label_train, train_predictions)
	er_train = 1 - er_train_acc # Subtract accuracy from 1
	er_train_per.append(er_train)

	# Evaluate testing error of model
	# Store in "er_test"
	er_test_acc = accuracy_score(label_test, test_predictions)
	er_test = 1 - er_test_acc # Subtract accuracy from 1
	er_test_per.append(er_test)
	
# Now plot training and testing MSEs for the different training sizes
plt.plot(num_train_per,er_train_per, label='Training Error')
plt.plot(num_train_per,er_test_per, label='Testing Error')
plt.xlabel('Percentage of Training Data')
plt.ylabel('Classification Error')
plt.title('Plot of Classification Error vs. Training Data Size')
plt.legend()
plt.show()

# END OF TASK 4












