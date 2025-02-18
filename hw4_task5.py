# CS 5013
# Catherine Donner
# Homework 4 Task 5

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression # Baseline method
from sklearn.ensemble import RandomForestClassifier # My method
from sklearn.metrics import accuracy_score # Classification accuracy
from sklearn.metrics import roc_auc_score # AUC score

# Load imbalanced data set (diabetes_new)
# 50 positive class instances and 500 negative class instances 
data = np.loadtxt('diabetes_new.csv', delimiter=',', skiprows=1)
[n,p] = np.shape(data)

# Use last 25% data for testing 
num_test = int(0.25*n)
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# Vary the percentage of data for training
num_train_per = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

# Storage for my method and baseline method's classification accuracy and AUC
acc_base_per = []
auc_base_per = []

acc_yours_per = []
auc_yours_per = []

# For every percentage of training dataset in the list
for per in num_train_per: 

	# Create training data and labels
	num_train = int(n*per)
	sample_train = data[0:num_train,0:-1]
	label_train = data[0:num_train,-1]
	
	# Baseline model is Logistic regression
	baseline_model = LogisticRegression()

	# Implement a baseline method that standardly trains 
	# the model using sample_train and label_train
	baseline_model.fit(sample_train, label_train)
	baseline_predictions = baseline_model.predict(sample_test)
	acc_base = accuracy_score(label_test, baseline_predictions)
    
	# evaluate model testing accuracy and stores it in "acc_base"
	acc_base_per.append(acc_base)
    
	# evaluate model testing AUC score and stores it in "auc_base".
	auc_base = roc_auc_score(label_test, baseline_predictions)
	auc_base_per.append(auc_base)
    
	# Implement my method
	model = RandomForestClassifier()

	# Aim to improve AUC score of baseline 
	# while maintaining accuracy as much as possible 
	# evaluate model testing accuracy and stores it in "acc_yours"
	model.fit(sample_train, label_train)
	your_predictions = model.predict(sample_test)
	acc_yours = accuracy_score(label_test, your_predictions)
	acc_yours_per.append(acc_yours)
	# evaluate model testing AUC score and stores it in "auc_yours"
	auc_yours = roc_auc_score(label_test, your_predictions)
	auc_yours_per.append(auc_yours)
    
# Plot figures for accuracy and AUC
plt.figure()    
plt.plot(num_train_per,acc_base_per, label='Base Accuracy')
plt.plot(num_train_per,acc_yours_per, label='Your Accuracy')
plt.xlabel('Percentage of Training Data')
plt.ylabel('Classification Accuracy')
plt.title('Baseline vs. Your Model Accuracy')
plt.legend()
plt.show()

plt.figure()
plt.plot(num_train_per,auc_base_per, label='Base AUC Score')
plt.plot(num_train_per,auc_yours_per, label='Your AUC Score')
plt.xlabel('Percentage of Training Data')
plt.ylabel('Classification AUC Score')
plt.title('Baseline vs. Your Model AUC')
plt.legend()
plt.show()

# END OF TASK 5   


