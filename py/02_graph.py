import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/02_Henry_Hub_Natural_Gas_Spot_Price.csv'

df = call_file(path)

print(df.columns)

fig, ax = plt.subplots(sharex=True, figsize=(12, 6))

colors = ['#e15759', '#f28e2b', '#edc948',
          '#59a14f', '#76b7b2', '#4e79a7', '#b07aa1']

m_size = 15
l_size = 12

source = 'Source: EIA'

ax.plot(df['year'], df['price'], linewidth=3, color='#0a8d8f')

ax.set_title('Average Annual Henry Hub Natural Gas Price\n', fontsize=20)
# ax.set_xlabel('Year', fontsize=m_size)
ax.set_ylabel('USD per Million Btu\n', fontsize=m_size)
ax.set_xlim([2005, 2020])
ax.set_ylim([0, 9])
plt.xticks(fontsize=l_size)
plt.yticks(fontsize=l_size)
ax.set_xticks(np.arange(2005, 2021, 2))
ax.set_facecolor('#ECECEC')
plt.text(0.1045, 0.01, source, fontsize=l_size,
         transform=plt.gcf().transFigure)

plt.show()
