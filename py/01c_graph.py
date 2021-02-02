import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def call_file(path):
    data = pd.read_csv(path, index_col='year')
    return pd.DataFrame(data)


path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/01b_Coal_Prices_Electricity_Sector.csv'

df = call_file(path)

print(df.columns)

lw = 3
source = 'Source: EIA'

colors = ['#e15759', '#f28e2b', '#edc948',
          '#59a14f', '#76b7b2', '#4e79a7', '#b07aa1']

fig, ax = plt.subplots(sharex=True, figsize=(12, 6))

ax.plot(df.loc[:, 'delivered'], color='black', linewidth=lw)
ax.plot(df.loc[:, 'transportation'], color=colors[0], linewidth=lw)
# ax.plot(df.loc[:, 'delivered'] - df.loc[:, 'transportation'],
#         color=colors[1], linewidth=lw)

m_size = 15
l_size = 12

ax.set_title('US Coal Prices Delivered to Power Sector\n', fontsize=20)
ax.set_ylabel('USD per Short Ton\n', fontsize=m_size)
ax.set_xlim([2008, 2019])
ax.set_ylim([0, 60])
plt.xticks(fontsize=l_size)
plt.yticks(fontsize=l_size)
ax.set_facecolor('#ECECEC')
plt.text(0.1045, 0.01, source, fontsize=l_size,
         transform=plt.gcf().transFigure)
plt.text(0.49, 0.78, 'Total Coal Price', fontsize=m_size,
         transform=plt.gcf().transFigure)
plt.text(0.4275, 0.4, 'Average Transportation Cost',
         fontsize=m_size, color=colors[0], transform=plt.gcf().transFigure)
# plt.text(0.107, 0.03, 'Non-Transportation ', fontsize=10, transform=plt.gcf().transFigure)

plt.show()
