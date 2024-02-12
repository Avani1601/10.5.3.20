import numpy as np
import matplotlib.pyplot as plt

# Define the function y(n)
def y(n):
    return 3*n**2 + 13*n + 10

# Define the range of n
n_values = np.arange(0, 11)

# Compute y(n) for each value of n
y_values = y(n_values)

# Plot stem plot for y(n)
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='b-', use_line_collection=True)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.xticks(np.arange(-10, 11, 1))  # Display only integer values on x-axis
plt.grid(True)

# Highlight point at n=9 with red color
plt.stem(9, y(9), linefmt='r-', markerfmt='ro', basefmt='r-', use_line_collection=True)
plt.savefig('plot2.png')
plt.show()

