# Catherine Donner
# CS 5013
# Homework 6 Task 1

# Import packages
import numpy as np
import random

# NOTE: array indices for states are not the same as in homework grid diagram
# Set up grid world parameters
rows, cols = 3, 4 # 3 rows x 4 columns
grid = np.zeros((rows, cols))  # Initialize grid world matrix as 0's but utilities will be stored here later
rewards = np.full((rows, cols), -0.04)  # Reward for each non-terminal state
rewards[0, 3] = 1  # Positive terminal state
rewards[1, 3] = -1  # Negative terminal state
block = (1, 1) # Block position
rewards[block] = None  # Mark state where block is with no utility/reward

# Next state direction probabilities
actions = ["up", "down", "left", "right"] # Actions that can be done
probs = {"target": 0.6, "left": 0.2, "right": 0.1, "opposite": 0.1} # Probabilities of target, opposite, etc. direction

# Policy for non-terminal states
policy = {
	(2, 0): "right", (2, 1): "up", (2, 2): "left", (2, 3): "left", # Bottom row
	(1, 0): "up", (1, 2): "left", # Middle row
	(0, 0): "left", (0, 1): "down", (0, 2): "right" # Top row
}

# Define grid boundaries
def valid_next_state(state, action):
	# Initialize state 
	x, y = state
	# Define valid actions
	if action == "up": x -= 1
	elif action == "down": x += 1
	elif action == "left": y -= 1
	elif action == "right": y += 1
    
	# Ensure next state is not beyond grid boundaries or block position
	if x < 0 or x >= rows or y < 0 or y >= cols or (x, y) == block:
		return state # Stay in current state
	return (x, y)

# Experiment simulation function, set discount rate at 0.8 as in instructions
def simulate_experiment(start, discount_rate=0.8):
	# Initialize state and trajectory path storage
	state = start # This will be (2, 0) 
	trajectory = []
	# While state is non-terminal state
	while state not in [(0, 3), (1, 3), (1, 1)]:  
		# Choose target action based on policy
		target_action = policy[state] # Get target action where starting state is
		# Evaluate and append each action based on probability
		action_probabilities = []
		for action in actions:
			if action == target_action:
				action_probabilities.append(probs["target"])
			elif action == actions[(actions.index(target_action) + 1) % 4]:  # Left
				action_probabilities.append(probs["left"])
			elif action == actions[(actions.index(target_action) - 1) % 4]:  # Right
				action_probabilities.append(probs["right"])
			else:  # Opposite
				action_probabilities.append(probs["opposite"])
        
		# Select an action based on probabilities
		action = random.choices(actions, weights=action_probabilities, k=1)[0]
		next_state = valid_next_state(state, action) # Make sure this move follows boundaries

        	# Append state and reward of state (these are to be averaged later)
		trajectory.append((state, rewards[state]))
		# Set current state to the next state
		state = next_state
    
	# Add state
	trajectory.append((state, rewards[state]))
    
	# Calculate returns
	G = 0 # Init G at 0
	returns = []
	# In order of state traveled, calculate utility for each state using formula
	for _, reward in reversed(trajectory):
		G = reward + discount_rate * G
		returns.insert(0, G)
    
	return trajectory, returns

# Monte Carlo estimation - do at least 10 experiments
def monte_carlo(grid, rewards, experiments=15, discount_rate=0.8):
	utilities = np.zeros_like(grid)
	# Non-terminal state returns
	returns = {state: [] for state in np.ndindex(grid.shape) if rewards[state] is not None}

	# For number of experiments, run experiment function
	for _ in range(experiments):
		for start in returns.keys():
			trajectory, G = simulate_experiment((2, 0), discount_rate) # Set starting state to (2, 0) or (1, 1) in homework instructions
			for idx, (state, _) in enumerate(trajectory):
				if state in returns:
					returns[state].append(G[idx])
    
	# Average returns across state to be utility
	for state, values in returns.items():
		utilities[state] = np.mean(values) if values else 0
    
	# Return utilities array
	return utilities

# Calculate estimated utilities
utilities = monte_carlo(grid, rewards)
print("Estimated utilities after 15 experiments:")
print(utilities) # This prints final utilities in matrix form

# This prints utilities for each state in the grid
for row in range(3):
	for col in range(4):
		print(f"Utility for state ({row}, {col}): {utilities[row, col]}")

# End of Task 1






















































