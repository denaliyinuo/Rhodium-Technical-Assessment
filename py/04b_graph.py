import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/04b_EIA_Henry_Hub_Natural_Gas_Price_Projections.csv'

df = call_file(path)

print(df.columns)

fig, ax = plt.subplots(sharex=True, figsize=(10, 5))

lw = 2
source = 'Source: EIA'

ax.set_facecolor('#ECECEC')
ax.plot(df.loc[0, '2010':'2019'], linewidth=lw, color='#0a8d8f')
# ax.plot(df.loc[1, '2019':'2040'], linewidth=lw)
# ax.plot(df.loc[2, '2019':'2040'], linewidth=lw)
ax.plot(df.loc[3, '2019':'2040'], linewidth=lw, color='red')
ax.plot(df.loc[4, '2019':'2040'], linewidth=lw, color='green')
# ax.plot(df.loc[5, '2019':'2040'], linewidth=lw)
# ax.plot(df.loc[6, '2019':'2040'], linewidth=lw)
ax.plot(df.loc[0, '2019':'2040'], linewidth=lw, color='#0a8d8f')
ax.axvline(x='2019', linestyle='--', color='grey')
ax.set_xticks(['2010', '2015', '2020', '2025', '2030', '2035', '2040'])


ax.set_xlim(['2010', '2040'])
# ax.set_ylim([0, 3.5])
title = 'EIA Projected Annual Henry Hub Natural Gas Price\n'
ax.set_title(title, fontsize=20)
ax.set_ylabel('2019 USD per Million Btu')
ax.fill_between(['2018', '2039'], df.loc[4, '2019':'2040'],
                df.loc[3, '2019':'2040'])
plt.text(0.107, 0.03, source, fontsize=10, transform=plt.gcf().transFigure)


plt.show()
