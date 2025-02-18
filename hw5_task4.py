# Catherine Donner
# CS 5013 Homework 5
# Task 4: kNN Classification 

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode # For counting mode of KNN

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

# Pick five values of k
k_values = [2,3,5,7,10]

# Initialize testing error storage
er_test = []

# For every k value do KNN algorithm
for k in k_values: 
	# Store predictions for k
	predictions = []

	# For each testing, find k-nearest neighbors
	for test_point in sample_test:
		# Compute distances
		distances = np.linalg.norm(sample_train - test_point, axis=1)

		# Sort distances and get indices of k-nearest neighbors
		k_nearest_indices = np.argsort(distances)[:k]

		# Get labels for nearest neighbors based on their indices
		k_nearest_labels = label_train[k_nearest_indices]

		# Predict label based on majority of class neighbors - use mode for this approach
		predict_label = mode(k_nearest_labels).mode[0]
		predictions.append(predict_label)

	# Store classification error in testing data 
	er = np.mean(predictions != label_test)
	er_test.append(er)

# Plot k versus classification error    
plt.figure()    
plt.plot(k_values,er_test)
plt.xlabel('k')
plt.ylabel('Classification Error')
plt.title('Classification Error for K-Nearest Neighbors Algorithm')
plt.show()

# End of Task 4

