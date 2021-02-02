import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/03_Coal_and_Natural_Gas_Electricity_Net_Generation.csv'

df = call_file(path)

print(df.columns)

fig, ax = plt.subplots(sharex=True, figsize=(10, 6))

lw = 3

m_size = 15
l_size = 12

source = 'Source: EIA'


ax.plot(df.loc[0, '2005':'2019'], linewidth=lw, color='black')
ax.plot(df.loc[1, '2005':'2019'], linewidth=lw, color='#0a8d8f')
ax.set_xlim(['2005', '2019'])
ax.set_ylim([0, 2.05e6])

title = 'US Annual Coal and Natural Gas Electricity Generation\n'
ax.set_title(title, fontsize=20)
# ax.set_xlabel('Year')
ax.set_ylabel('Electricity Generation (MWh)\n')

plt.xticks(fontsize=l_size)
plt.yticks(fontsize=l_size)
ax.set_xticks(np.arange(2005, 2019, 2))

ax.set_facecolor('#ECECEC')
fig.text(0.577, 0.72, 'coal', fontsize=14, color='black')
fig.text(0.54, 0.5, 'natural gas', fontsize=14, color='#0a8d8f')
plt.text(0.107, 0.03, source, fontsize=10, transform=plt.gcf().transFigure)

plt.show()
