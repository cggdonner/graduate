# Catherine Donner
# CS 5013
# Homework 2 Programming Tasks

# Task 2 - Genetic Algorithm
# CreditCard.csv was preprocessed in Google Colab, renamed to CreditCard_preprocessed.csv

# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Define f(x) linear correlation between x attributes and y credit approval result
def f(x, w):
	return sum(w[j] * x[j] for j in range(len(w)))

# Define error function er(w)
def er(w, x, y):
	n = 340 # Number of records in dataset
	total_error = 0
	for i in range(n):
		total_error += (f(x[i], w) - y[i]) ** 2
	return total_error / n

# Fitness function (given in instructions)
def fitness(w, x, y):
	return np.exp(-er(w, x, y))

# Parent selection function
def parent_select(population, fitnesses):
	total_fitness = sum(fitnesses)
	probabilities = [fit / total_fitness for fit in fitnesses] # This chooses parents based on probabilities proportional to fitness values
	parents = random.choices(population, weights=probabilities, k=2) # 2 parents
	return parents

# Crossover function
def crossover(p1, p2):
	crossover_point = len(p1) // 2 # 3 elements from 1 parent, 3 elements from other parent (i.e. middle of w)
	child = p1[:crossover_point] + p2[crossover_point:]
	return child

# Mutation function
def mutation(chromosome, mutation_rate):
	for i in range(len(chromosome)):
		if random.random() < mutation_rate: # This is random mutation
			chromosome[i] = -chromosome[i] # Flip gene
	return chromosome

# Genetic algorithm function
def genetic_algorithm(x, y, population_size, generations, mutation_rate):
	# Initialize population
	population = [random.choices([-1, 1], k=6) for _ in range(population_size)] # Randomize initial w

	# Track history for plotting
	history = []

	# Create generations
	for generation in range(generations):
		# Calculate fitness for each individual in population
		fitnesses = [fitness(w, x, y) for w in population]
		# Record best w and error
		best_w = population[np.argmax(fitnesses)]
		best_er = er(best_w, x, y)
		history.append((generation, best_er))
		
		# Use elite 20% to minimize er(w)
		# Without this er(w) would not converge 
		sorted_population = [w for _, w in sorted(zip(fitnesses, population), reverse=True)]
		num_elite = int(0.2 * population_size)
		new_population = sorted_population[:num_elite]

		# Create next generations
		for _ in range((population_size-num_elite) // 2): # Retain elite individuals 
			# Select 2 parents
			parent1, parent2 = parent_select(population, fitnesses)
			# Perform crossover
			child1 = crossover(parent1, parent2)
			child2 = crossover(parent2, parent1)
			# Perform mutation
			child1 = mutation(child1, mutation_rate)
			child2 = mutation(child2, mutation_rate)
			# Add new children to population
			new_population.extend([child1, child2])

		# Get new population
		population = new_population

	# Return optimal w and er(w) and history for plotting
	return best_w, er(best_w, x, y), history

# Define function for plotting
def plot_history(history):
	generations, errors = zip(*history)
	plt.plot(generations, errors)
	plt.xlabel("Generation")
	plt.ylabel("er(w)")
	plt.title("Convergence of er(w) Using Genetic Algorithm")
	plt.show()

# Define main function
def main():
	# Load dataset
	df = pd.read_csv('CreditCard_preprocessed.csv')

	# Define x and y attributes
	x = df[['Gender', 'CarOwner', 'PropertyOwner', '#Children', 'WorkPhone', 'Email_ID']].values
	y = df['CreditApprove'].values

	# Run genetic algorithm
	optimal_w, optimal_er, history = genetic_algorithm(x, y, population_size=20, generations=100, mutation_rate=0.15)

	# Plot results
	plot_history(history)

	# Print optimal w and er(w)
	print("Optimal w:", optimal_w)
	print("Optimal er(w):", optimal_er)

# Call main to execute script
if __name__ == "__main__":
	main()

# End of genetic algorithm
	





























