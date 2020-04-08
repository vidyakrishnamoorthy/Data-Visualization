from die import Die
import pygal

die = Die()

results_a = []
for roll_num in range(100):
    result = die.roll()
    results_a.append(result)
print(results_a)

results_b = []
for roll_num in range(1000):
    result = die.roll()
    results_b.append(result)
print(results_b)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results_b.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')