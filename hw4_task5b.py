# CS 5013
# Catherine Donner
# Homework 4 Task 5 Bonus

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression # Baseline method
from sklearn.ensemble import RandomForestClassifier # My method
from sklearn.metrics import roc_auc_score # AUC score

# Load imbalanced data set (diabetes_new)
# 50 positive class instances and 500 negative class instances
data = np.loadtxt('diabetes_new.csv', delimiter=',', skiprows=1)
[n,p] = np.shape(data)

# Use last 25% data for testing
num_test = int(0.25*n)
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# Set percentage of data for training (70%)
num_train_per = 0.7

# Set array of different n_estimators values
n_estimators_list = [50, 100, 150, 200, 250, 300, 350, 400] 

# Storage for baseline method, my method, and my hyperparameter method's AUC
auc_base_per = []
auc_yours_per = []
auc_yours_hp_per = [] 

# For every value of n_estimators in the list
for n_est in n_estimators_list:

	# Create training data and labels
	num_train = int(n*num_train_per)
	sample_train = data[0:num_train,0:-1]
	label_train = data[0:num_train,-1]

	# Baseline model is Logistic regression
	baseline_model = LogisticRegression()

	# Implement a baseline method that standardly trains
	# the model using sample_train and label_train
	baseline_model.fit(sample_train, label_train)
	baseline_predictions = baseline_model.predict(sample_test)

	# evaluate model testing AUC score and stores it in "auc_base".
	auc_base = roc_auc_score(label_test, baseline_predictions)
	auc_base_per.append(auc_base)

	# Implement my method (without hyperparameter)
	model = RandomForestClassifier()

	# Aim to improve AUC score of baseline
	# while maintaining accuracy as much as possible
	model.fit(sample_train, label_train)
	your_predictions = model.predict(sample_test)
        
	# evaluate model testing AUC score and stores it in "auc_yours"
	auc_yours = roc_auc_score(label_test, your_predictions)
	auc_yours_per.append(auc_yours)

	# Initialize model with hyperparameter (use n_estimators)
	hp_model = RandomForestClassifier(n_estimators=n_est)
	
	# Train model and get predictions
	hp_model.fit(sample_train, label_train)
	hp_your_predictions = hp_model.predict(sample_test)

	# Get AUC and store in auc_yours_hp
	auc_yours_hp = roc_auc_score(label_test, hp_your_predictions)
	auc_yours_hp_per.append(auc_yours_hp)

# Plot figure for AUC
plt.figure()
plt.plot(n_estimators_list,auc_base_per, label='Base AUC Score')
plt.plot(n_estimators_list,auc_yours_per, label='Your AUC Score')
plt.plot(n_estimators_list,auc_yours_hp_per, label='Your Hyperparameter AUC Score')
plt.xlabel('Number of Estimators')
plt.ylabel('Classification AUC Score')
plt.title('Baseline vs. Your Model vs. Your Hyperparameter Model AUC')
plt.legend()
plt.show()

# END OF TASK 5 BONUS










