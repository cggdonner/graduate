# Catherine Donner
# CS 5013 Homework 5
# Task 3: Kmeans Clustering

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D # For 3D plot

# Load data 
# note we do not need label 
data = np.loadtxt('crimerate.csv', delimiter=',')
[n,p] = np.shape(data)
sample = data[:,0:-1]

# Pick a number of clusters - NOTE: CHANGE TO K = 2 TO PLOT FIGURE 3 OR TO K = 3 TO PLOT FIGURE 4
k = 3
# Set default convergence to false
convergence = False

# Implement the Kmeans clustering algorithm 
# First randomly initialize k cluster centers 
centers_idx = np.random.choice(n, k, replace=False)
centers = sample[centers_idx, :]

# Set number of iterations
iterations = 100

# Iteration loop for k-means clustering
for iteration in range(iterations):
	# Compute distances from centers and find closest centers
	distances = np.linalg.norm(sample[:, np.newaxis] - centers, axis=2)
	closest = np.argmin(distances, axis=1)

	# Update centers by calculating mean of all points in cluster
	new_centers = np.array([sample[closest == j].mean(axis=0) for j in range(k)])

	# Check if centers have changes, if not then convergence reached
	if np.allclose(centers, new_centers):
		converged = True
		break
	centers = new_centers # Continue updating if not

# when clustering is done, 
# store the clustering label in `label_cluster' 
# cluster index starts from 0 e.g., 
# label_cluster[0] = 1 means the 1st point assigned to cluster 1
# label_cluster[1] = 0 means the 2nd point assigned to cluster 0
# label_cluster[2] = 2 means the 3rd point assigned to cluster 2
label_cluster = closest # Set cluster labels to closest clusters

# the following code plot clustering results in a 2D space
pca_2d = PCA(n_components=2)
pca_2d.fit(sample)
sample_pca_2d = pca_2d.transform(sample)
idx = []
colors = ['blue','red','green','m']
cluster_labels = [f'Cluster {i+1}' for i in range(k)] # Add cluster labels to legend
for i in range(k):
     idx = np.where(label_cluster == i)
     plt.scatter(sample_pca_2d[idx,0],sample_pca_2d[idx,1],color=colors[i],facecolors='none',label=cluster_labels[i])

# Plot clusters with components
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.title(f'K-means Clustering with k={k} (2D)')
plt.legend()
plt.show()

# Now plot clusters in 3D plot
pca_3d = PCA(n_components=3)
pca_3d.fit(sample)
sample_pca_3d = pca_3d.transform(sample)
idx = []
colors = ['blue','red','green','m']
cluster_labels = [f'Cluster {i+1}' for i in range(k)] # Add cluster labels to legend

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(k):
     idx = np.where(label_cluster == i)
     ax.scatter(sample_pca_3d[idx,0],sample_pca_3d[idx,1],sample_pca_3d[idx,2],color=colors[i],facecolors='none',label=cluster_labels[i])

# Plot clusters with components
ax.set_xlabel('Component 1')
ax.set_ylabel('Component 2')
ax.set_zlabel('Component 3')
plt.title(f'K-means Clustering with k={k} (3D)')
plt.legend()
plt.show()

# End of Task 3




