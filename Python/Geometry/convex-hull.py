
from scipy.spatial import ConvexHull
import numpy as np

# 30 random points in 2-D
np.random.seed(1234)
points = np.random.rand(30, 2)

# Compute the convex hull of a set of points
hull = ConvexHull(points)

# Print the indices of points forming the vertices of the convex hull
print(hull.vertices)  # [18  7  0 16 23  9 27 26  1  2]
