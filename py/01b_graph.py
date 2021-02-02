import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


file = ['01_Coal_shipments_to_the_electric_power_sector__heat_content_by_plant_state.csv',
        '01_Coal_shipments_to_the_electric_power_sector__price_by_plant_state.csv',
        '01_Coal_shipments_to_the_electric_power_sector__quantity_by_plant_state.csv']

path = []

for i in range(3):
    path.append('/Users/nathanoliver/Desktop/Python/Rhodium/csv/' + file[i])

df1 = call_file(path[0])
df2 = call_file(path[1])
df3 = call_file(path[2])

print(df1.columns)
print(df2.columns)
print(df3.columns)

lw = 3
source = 'Source: EIA'

fig, ax = plt.subplots(sharex=True, figsize=(10, 8))

color = ['']

for i in range(5):
    if i == 0:
        plt.plot(df2.loc[i, '2008':'2019'], color='black', linewidth=lw)
    else:
        plt.plot(df2.loc[i, '2008':'2019'], linewidth=lw)

ax.set_title('US Coal Prices Delivered to Power Sector\n', fontsize=20)
ax.set_ylabel('Price\n(USD / Short Ton)\n')
ax.set_xlim(['2008', '2019'])
ax.set_facecolor('#ECECEC')
plt.text(0.107, 0.03, source, fontsize=10, transform=plt.gcf().transFigure)

plt.show()
