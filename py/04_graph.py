import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/04_EIA_Henry_Hub_Natural_Gas_Price_Projections.csv'

df = call_file(path)

print(df.columns)

fig, ax = plt.subplots(sharex=True, figsize=(10, 5))

lw = 3
source = 'Source: EIA'

ax.set_facecolor('#ECECEC')
ax.plot(df.loc[0, '2021':'2040'], linewidth=lw, color='#0a8d8f')
ax.set_xlim(['2021', '2040'])
# ax.set_ylim([0, 3.5])
title = 'EIA Projected Annual Henry Hub Natural Gas Price\n'
ax.set_title(title, fontsize=20)
ax.set_ylabel('2019 USD per Million Btu')
plt.text(0.107, 0.03, source, fontsize=10, transform=plt.gcf().transFigure)


plt.show()
