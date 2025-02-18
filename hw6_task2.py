# Catherine Donner
# CS 5013
# Homework 6 Task 2

# Import packages
import numpy as np

# Define estimated utilities array from Task 1 (rounded to 4 decimal points)
estimated_utilities = np.array([
    [-0.1543, -0.0773,  0.4534,  1.0 ],
    [-0.1692,   None, -0.3678, -1.0 ],
    [-0.1933, -0.2068, -0.2341, -0.2884]
])

# Define grid world parameters
rewards = np.full((3, 4), -0.04) # Grid size with non-terminal state rewards
rewards[0, 3] = 1  # Positive terminal state
rewards[1, 3] = -1  # Negative terminal state
rewards[1, 1] = None  # Block position

# Define valid actions
actions = ["up", "down", "left", "right"]
# Probabilities for target, opposite, etc. directions taken
probs = {"target": 0.6, "left": 0.2, "right": 0.1, "opposite": 0.1}

# Define grid boundaries function
def valid_next_state(state, action):
	# Initialize state
	x, y = state
	# Action for next state
	if action == "up": x -= 1
	elif action == "down": x += 1
	elif action == "left": y -= 1
	elif action == "right": y += 1

	# Make sure next move does not extend beyond 3 rows x 4 columns grid or block position
	if x < 0 or x >= 3 or y < 0 or y >= 4 or (x, y) == (1, 1):
		return state  # Stay in current state
	return (x, y)

# Policy optimization based on utility estimations from Task 1
def optimize_policy(utilities, rewards, discount_rate=0.8):
	# Set rows and columns based on utilities matrix shape
	rows, cols = utilities.shape
	# Initialize optimal policy storage
	optimal_policy = {}

	# For every state in the grid
	for x in range(rows):
		for y in range(cols):
			state = (x, y)
			# Do optimal policy as long as state is non-terminal
			if rewards[state] is None or state in [(0, 3), (1, 3), (1,1)]:  # Skip terminal and block states
				continue # Stay in current state

			# Evaluate each action
			action_values = {}
			for action in actions:
				expected_utility = 0 # Initialize expected utility
				# For every (zipped) direction with probability, move to next state
				for direction, probability in zip(
				["target", "left", "right", "opposite"], 
				[probs["target"], probs["left"], probs["right"], probs["opposite"]]
				):
					if direction == "target":
						next_state = valid_next_state(state, action)
					elif direction == "left":
						next_state = valid_next_state(state, actions[(actions.index(action) + 1) % 4])
					elif direction == "right":
						next_state = valid_next_state(state, actions[(actions.index(action) - 1) % 4])
					else:  # Opposite
						next_state = valid_next_state(state, actions[(actions.index(action) + 2) % 4])
                    
					# Calculate expected utility using Bellman equation
					expected_utility += probability * (rewards[next_state] + discount_rate * utilities[next_state])

				# Set action value to expected utility
				action_values[action] = expected_utility

			# Choose the action with the highest expected utility
			optimal_policy[state] = max(action_values, key=action_values.get)

	# Return optimal policy for all non-terminal states
	return optimal_policy

# Call optimize policy function based on estimated utilities
optimal_policy = optimize_policy(estimated_utilities, rewards)

# Print the optimal policy for all non-terminal states
print("Optimal Policy:")
for x in range(3): # 3 rows
    for y in range(4): # 4 columns
        state = (x, y)
        if state in optimal_policy: # These should be non-terminal states
            print(f"State {state}: {optimal_policy[state]}")
        else: # These should be terminal/block states
            print(f"State {state}: None")

# End of Task 2

















































