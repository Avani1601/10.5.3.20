import matplotlib.pyplot as plt
import numpy as np

# Read data from the 'data.dat' file
data_file = 'data.dat'
data = np.loadtxt(data_file, skiprows=1)  # Skip the header line

# Extract values for x and y
x_values = data[:, 0].astype(int)
seq_gp = data[:, 1]

# Plotting the geometric progression sequence with integer x-axis ticks
plt.figure()
plt.stem(x_values, seq_gp, markerfmt='ro', linefmt='r-', basefmt='k-')
plt.xlabel('n')
plt.ylabel('x(n)')

# Set x-axis ticks to integers
plt.xticks(np.unique(x_values))

# Save the figure as 'graph_gp_integers.png'
plt.savefig('graph_gp_integers.png')
plt.show()

