import matplotlib.pyplot as plt

# Create some data
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 8, 10,12]

# Create a figure and axispio
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Plot Title')

# Show the plot
plt.show()
