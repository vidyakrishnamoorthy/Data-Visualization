import matplotlib.pyplot as plt

input_values = [0, 1,2,3,4,5,6]
squares = [0, 1, 4, 9, 16, 25, 36]
plt.plot(input_values, squares, linewidth = 5)

plt.title("square numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)

plt.tick_params(axis = 'both', labelsize = 14)
plt.show()
