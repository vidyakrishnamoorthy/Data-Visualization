# CSV: comma separated values

import csv
import matplotlib.pyplot as plt
from _datetime import datetime

# file_name = 'sitka_weather_2014.csv'
file_name = 'death_valley_2014.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [], [], []
    for row in reader:
        try:
            high = int(row[1])
            highs.append(high)
            low = int(row[3])
            lows.append(low)
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            dates.append(current_date)
        except ValueError:
            print("Missing value on date  " + str(current_date))

    print(highs)
    # for index, column_header in enumerate(header_row):
    #     print(index, header_row)

    fig = plt.figure(dpi=128, figsize=(6,6))
    plt.plot(dates, highs, color='red', alpha=0.5)
    plt.plot(dates, lows, color='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # plt.plot(dates, highs)
    fig.autofmt_xdate()

    plt.title("Temperature Highs")
    plt.ylabel('Temperature(F)', fontsize=10)
    plt.xlabel('Date', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
