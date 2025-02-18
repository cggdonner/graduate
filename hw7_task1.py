# Catherine Donner
# CS 5013
# Homework 7 Task 1

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

# Choose values of k (neurons per layer)
k_values = [2,5,10,15,20]
# Fix m number of layers to 5
m = 5

# Initialize training and testing error storage
er_train_k = []
er_test_k = []
# Iterate MLP training for every value of k
for k in k_values: 
    
	# train a MLP classification model 
	layer_sizes = tuple([k]*m) # Define layer size
	# Initialize MLP model with layer sizes
	model = MLPClassifier(hidden_layer_sizes=layer_sizes, max_iter=1000, random_state=42)   
	# Train model
	model.fit(sample_train, label_train)  

	# evaluate training error and testing error 
	# First calculate predictions
	pred_train = model.predict(sample_train) # Training
	pred_test = model.predict(sample_test) # Testing
	er_train = 1 - accuracy_score(pred_train, label_train)
	er_test = 1 - accuracy_score(pred_test, label_test)
	# Add errors to lists
	er_train_k.append(er_train)
	er_test_k.append(er_test)
   
# Plot classification error vs. k
plt.figure()
plt.plot(k_values,er_train_k, label='Training Error')
plt.plot(k_values,er_test_k, label='Testing Error')
plt.xlabel('k value') 
plt.ylabel('Classification Error')
plt.title('MLP Classification Error vs. k Neurons per Layer')
plt.legend()
plt.show()

# End of Task 1


