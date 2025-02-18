# Catherine Donner
# CS 5013 Artificial Intelligence
# Homework 2 Programming Tasks

# Task 1 - Local Hill Climbing Algorithm

# CreditCard.csv was preprocessed in Google Colab, renamed 'CreditCard_preprocessed.csv'
# Preprocessing included encoding M,F,Y,N to 0s and 1s

# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Define linear relation for x attributes and y result of credit approval
def f(x, w):
	return sum(w[j] * x[j] for j in range(len(w)))

# Define error function er(w) to be minimized
def er(w, x, y):
	n = 340 # Predefined number of records in dataset
	total_error = 0
	for i in range(n):
		total_error += (f(x[i], w) - y[i]) ** 2
	return total_error / n

# Define generating neighbors function
def generate_neighbors(w):
	neighbors = []
	for i in range (len(w)):
		neighbor = w.copy()
		neighbor[i] = -neighbor[i] # Solution is adjacent if differs by 1 element
		neighbors.append(neighbor) # Add all neighbors
	return neighbors

# Define hill-climbing local search function
def hill_climbing(x, y, max_rounds):
	w = random.choices([-1,1], k=6) # Initial random guess for w
	history = [(0, er(w, x, y))] # To keep track of plotting er(w)

	# Get best local neighbor
	for i_round in range(1, max_rounds): 
		neighbors = generate_neighbors(w) # Get neighbors
		best_neighbor = min(neighbors, key=lambda w_prime: er(w_prime, x, y)) # Get minimum possible error given all possible w primes

		# If no improvement on convergence, stop
		if er(best_neighbor, x, y) >= er(w, x, y):
			break

		# Set new best w solution
		w = best_neighbor
		history.append((i_round, er(w, x, y)))
	
	# Return optimal w, er(w), and plotting history
	return w, er(w, x, y), history

# Function to plot history
def plot_history(history): 
	rounds, errors = zip(*history) # Collect errors and rounds for plot
	plt.plot(rounds, errors)
	plt.xlabel("Round")
	plt.ylabel("er(w)")
	plt.title("Convergence of er(w) Using Hill Climbing")
	plt.xticks(range(0, len(rounds))) # Set integer x-ticks
	plt.show()

# Define main function
def main():
	# Import preprocessed CreditCard dataset
	df = pd.read_csv('CreditCard_preprocessed.csv')

	# Define x and y attributes
	x = df[['Gender', 'CarOwner', 'PropertyOwner', '#Children', 'WorkPhone', 'Email_ID']].values
	y = df['CreditApprove'].values
	
	# Run hill_climbing function to return optimal w, er(w) and plotting history
	optimal_w, optimal_er, history = hill_climbing(x, y, max_rounds=10)

	# Plot results of history
	plot_history(history)

	# Print optimal w and optimal er(w)
	print("Optimal w:", optimal_w)
	print("Optimal er(w):", optimal_er)

# Call main to execute script
if __name__ == "__main__":
	main()

# End of Hill Climbing Search code













