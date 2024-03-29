import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Plot the first subplot
ax1.plot(x, y1, color='blue', label='sin(x)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()

# Plot the second subplot
ax2.plot(x, y2, color='red', label='cos(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()

# Save the figure as a PNG file
fig.savefig('plot.png')
