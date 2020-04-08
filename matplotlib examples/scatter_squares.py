import matplotlib.pyplot as plt

# plt.scatter(0,0)
# plt.scatter(1,1)
# plt.scatter(2,4, s=200)
# plt.scatter(3,9)
# plt.scatter(4,16)
# plt.scatter(5,25)
# plt.scatter(6,36)

# x_values = [0,1,2,3,4,5,6]
# y_values = [0,1,4,9,16,25,36]

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c='red', edgecolor = 'none',s = 40)
# plt.scatter(x_values, y_values, c=(0,0.8,0.8), edgecolor = 'none',s = 40)
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues,
            edgecolor = 'none',s = 40)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which = 'major', labelsize=14)

plt.axis([0,1100,0,1100000])

plt.savefig('squares_scatter_plt.png', bbox_inches = 'tight')
plt.show()