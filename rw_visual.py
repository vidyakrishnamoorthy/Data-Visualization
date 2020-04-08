import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50050)
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10,6))

    point_numbers = list(range(rw.num_points))

    # plt.scatter(rw.x_values, rw.y_values, s=15)
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor = (0,0.3,0.8), s=15)
    plt.scatter(0, 0, c='green', edgecolor=(0, 0.8, 0.8), s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor=(0, 0, 0.8), s=100)
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap =plt.cm.Blues, edgecolor='none', s=1)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? y/n")
    if keep_running == 'n':
        break