# import matplotlib.pyplot as plt

# # Create a bar graph with custom width
# x = ['A', 'B', 'C', 'D']
# y = [1, 3, 2, 4]
# width = 0.5  # custom width
# plt.bar(x, y, width=width)

# # Display the graph
# plt.show()

import matplotlib.pyplot as plt

# Create a bar graph with custom y-axis range
x = ['A', 'B', 'C', 'D']
y = [1, 3, 2, 4]
plt.bar(x, y)

# Set the y-axis range to 0 to 5
plt.ylim([0, 5])

# Display the graph
plt.show()

