# Catherine Donner
# CS 5013 Homework 5
# Task 6: Random Forest Classification 

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier # Directly call random forest

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

# Pick five values of m (number of decision trees or estimators)
m_values = [50,100,250,400,500]

# Initialize storage for testing error
er_test = []

# For every m decision trees do random forest
for m in m_values: 
	# Initialize random forest classifier
	model = RandomForestClassifier(n_estimators=m, random_state = 42) # set n_estimators to each m value

	# Fit model on training data
	model.fit(sample_train, label_train)

	# Make predictions based on testing data
	predictions = model.predict(sample_test)
	
	# Calculate classification error manually based on testing predictions
	er = np.mean(label_test != predictions) # Use mean of all incorrect predictions
	er_test.append(er)
    
# Plot m number of trees vs. classification error
plt.figure()    
plt.plot(m_values,er_test)
plt.xlabel('m')
plt.ylabel('Classification Error')
plt.title('Classification Error vs. m Decision Trees - Random Forest')
plt.show()

# End of Task 6


