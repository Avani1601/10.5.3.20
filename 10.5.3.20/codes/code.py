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

# Use only integers on the x-axis
plt.stem(x_values, seq_gp, markerfmt='ro', linefmt='r-', basefmt='k-')
plt.xticks(np.arange(min(x_values), max(x_values) + 1, 1))

# Highlight the 6th term stem
highlight_index = 5  # 6th term (0-indexed)
plt.stem(x_values[highlight_index], seq_gp[highlight_index], linefmt='b-', markerfmt='bo', basefmt='k-')

plt.xlabel('n')
plt.ylabel('x(n)')

# Save the figure as 'graph_gp_integers_highlight_stem.png'
plt.savefig('graph.png')
plt.show()

