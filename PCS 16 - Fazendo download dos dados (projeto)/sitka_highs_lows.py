from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path("sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extrai as temperaturas máximas
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plota as temperaturas máximas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# Formata o gráfico
ax.set_title("Daily High and Low Temperatures", fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()
