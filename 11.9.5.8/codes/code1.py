import numpy as np
import matplotlib.pyplot as plt

# Define the function y(n)
def y(n):
    return 3*n**2 + 13*n + 10

# Define the range of n
n_values = np.arange(0, 11)

# Compute y(n) for each value of n
y_values = y(n_values)

# Highlight the point at n=9
highlight_index = np.where(n_values == 9)[0][0]

# Plot stem plot for y(n)
plt.stem(n_values, y_values, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.xticks(np.arange(-10, 11, 1))  # Display only integer values on x-axis
plt.grid(True)

# Highlight point at n=9
plt.scatter(n_values[highlight_index], y_values[highlight_index], color='red', zorder=5)
plt.savefig('plot2.png')
plt.show()

