import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/01_Coal_Prices_Electricity_Sector.csv'

df = call_file(path)

print(df.columns)

lw = 3
source = 'Source: EIA'

fig, ax = plt.subplots(sharex=True, figsize=(10, 5))

plt.plot(df.loc[1, '2008':'2019'], color='black', linewidth=lw)

ax.set_title('US Coal Prices Delivered to Power Sector\n', fontsize=20)
ax.set_ylabel('Price\n(USD / Short Ton)\n')
ax.set_xlim(['2008', '2019'])
ax.set_facecolor('#ECECEC')
plt.text(0.107, 0.03, source, fontsize=10, transform=plt.gcf().transFigure)

plt.show()
