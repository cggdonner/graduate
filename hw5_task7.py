# Catherine Donner
# CS 5013 Homework 5
# Task 7: Fairness in machine learning 

# Import packages
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from xgboost import XGBClassifier # For my method, XGBoost handles class imbalance well, 
# and in addition to weighting data equally can help address fairness more as an ensemble model

# --------------------------------------------------------
# We will experiment on the student performance data set
# You can find description of the original data set here
# https://archive.ics.uci.edu/dataset/320/student+performance
# We provide a preprocessed data set "student.csv". 
# The 1st column contains gender (1 for female; 0 for male)
# The last column contains final score (we will binarize it)
# ----------------------------------------------------------
# Load data
data = np.loadtxt('student.csv', delimiter=',')
# now we binarize the label so 1 means > 10 and 0 means <= 10
data[data[:,-1]<=12,-1] = 0
data[data[:,-1]>0,-1] = 1
[n,p] = np.shape(data)

# 75% for training, 25% for testing 
num_train = int(0.75*n)
num_test = int(0.25*n)
sample_train = data[0:num_train,0:-1]
label_train = data[0:num_train,-1]
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# Baseline Method - Linear Discriminant
# Standard training and testing 
model = LinearDiscriminantAnalysis()
model.fit(sample_train,label_train)
label_pred = model.predict(sample_test)

# Separately evaluate error on male students and female students
idx_female = np.where(sample_test[:,0]==1)[0]
idx_male = np.where(sample_test[:,0]==0)[0]
er_female = 1-accuracy_score(label_test[idx_female],label_pred[idx_female])
er_male = 1-accuracy_score(label_test[idx_male],label_pred[idx_male])
er_gap = abs(er_male - er_female)

# you will see, error is 10% higher on male than female 
print("Standard Method")
print(er_male)
print(er_female)
print(er_gap)

# MY METHOD - Weighted XGBoost, helps reduce bias
# Aim to reduce the gap between two errors with your method
# First separate male and female indices in the training data
idx_female_train = np.where(sample_train[:, 0] == 1)[0]
idx_male_train = np.where(sample_train[:, 0] == 0)[0]

# Calculate group-specific training error rates with XGBoost
model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(sample_train, label_train)
label_pred_train = model.predict(sample_train)

# Calculate training errors for both genders
er_female_train = 1 - accuracy_score(label_train[idx_female_train], label_pred_train[idx_female_train])
er_male_train = 1 - accuracy_score(label_train[idx_male_train], label_pred_train[idx_male_train])

# Ensure no zero-division by checking if both errors are zero
if er_female_train + er_male_train > 0:
	weight_female = er_male_train / (er_female_train + er_male_train)
	weight_male = er_female_train / (er_female_train + er_male_train)
else:
	weight_female = 1.0 # Set weights equally to reduce bias
	weight_male = 1.0

# Create sample weight vector to improve errors
sample_weights = np.ones(len(label_train))
sample_weights[idx_female_train] *= weight_female
sample_weights[idx_male_train] *= weight_male

# Train the model using sample weights with XGBoost
model_weighted = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model_weighted.fit(sample_train, label_train, sample_weight=sample_weights)

# whatever method you have, store your model prediction 
# on testing set in "label_pred". Then run the following code
label_pred = model_weighted.predict(sample_test)
idx_female = np.where(sample_test[:,0]==1)[0]
idx_male = np.where(sample_test[:,0]==0)[0]
er_female = 1-accuracy_score(label_test[idx_female],label_pred[idx_female])
er_male = 1-accuracy_score(label_test[idx_male],label_pred[idx_male])
er_gap = abs(er_male - er_female)
print("Fair Method")
print(er_male)
print(er_female)
print(er_gap)

# End of Task 7
