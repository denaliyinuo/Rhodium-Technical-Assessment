import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def call_file(path):
    data = pd.read_csv(path, index_col=0)
    return pd.DataFrame(data)


path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/03_Coal_and_Natural_Gas_Electricity_Net_Generation.csv'

df = call_file(path)

print(df.columns)

fig, ax = plt.subplots(sharex=True, figsize=(10, 6))

lw = 3

m_size = 15
l_size = 12

source = 'Source: EIA'


ax.plot(df.loc[:, 'coal_MWh'] / 1e3, linewidth=lw, color='black')
ax.plot(df.loc[:, 'ng_MWh'] / 1e3, linewidth=lw, color='#0a8d8f')
ax.set_xlim([2005, 2019])
ax.set_ylim([0, 2050])

title = 'US Annual Coal and Natural Gas Electricity Generation\n'
ax.set_title(title, fontsize=20)
# ax.set_xlabel('Year')
ax.set_ylabel('Electricity Generation (TWh)\n', fontsize=m_size)

plt.xticks(fontsize=l_size)
plt.yticks(fontsize=l_size)
ax.set_xticks(np.arange(2005, 2021, 2))
ax.set_yticks(np.arange(0, 2500, 500))
ax.ticklabel_format(useOffset=False, style='plain')

ax.set_facecolor('#ECECEC')
fig.text(0.577, 0.72, 'coal', color='black', fontsize=m_size)
fig.text(0.54, 0.5, 'natural gas', color='#0a8d8f', fontsize=m_size)
plt.text(0.1045, 0.01, source, transform=plt.gcf().transFigure, fontsize=l_size)

plt.show()
