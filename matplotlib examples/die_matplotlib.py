from die import Die
import matplotlib.pyplot as plt

die_1 = Die()

die_roll = 1000
results = []
for value in range(die_roll):
    result = die_1.roll()
    results.append(result)

frequencies = []
for value in range(1, 7):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = [1, 2, 3, 4, 5, 6]

# plt.plot(x_values, frequencies)
# plt.bar(x_values, frequencies)
plt.barh(x_values, frequencies)

plt.xlabel("Results")
plt.ylabel("Frequency of results")
plt.title("Count of die rolled "+ str(die_roll) +" times")

plt.show()
