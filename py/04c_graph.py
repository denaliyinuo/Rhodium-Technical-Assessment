import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def call_file(path):
    data = pd.read_csv(path, index_col=0)
    return pd.DataFrame(data)


y1 = [2.57,
      2.46,
      2.38,
      2.27,
      2.22,
      2.24,
      2.41,
      2.61,
      2.67,
      2.67,
      2.64,
      2.6,
      2.59,
      2.61,
      2.63,
      2.63,
      2.61,
      2.63,
      2.65,
      2.65,
      2.66,
      2.66]
y2 = [2.57,
      2.62,
      2.83,
      2.96,
      3.1,
      3.31,
      3.68,
      3.97,
      4.16,
      4.35,
      4.49,
      4.56,
      4.65,
      4.81,
      4.96,
      5.06,
      5.09,
      5.16,
      5.24,
      5.33,
      5.4,
      5.47]

x = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029,
     2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040]

path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/04b_EIA_Henry_Hub_Natural_Gas_Price_Projections.csv'

df = call_file(path)

print(df.columns)

fig, ax = plt.subplots(sharex=True, figsize=(10, 6))

lw = 2

m_size = 15
l_size = 12

source = 'Source: EIA'

ax.set_facecolor('#ECECEC')
ax.plot(df.loc[2010:2020, 'historical'], linewidth=lw, color='#0a8d8f')
# ax.plot(df.loc[1, '2019':'2040'], linewidth=lw)
# ax.plot(df.loc[2, '2019':'2040'], linewidth=lw)
ax.plot(df.loc[2019:2040, 'high_oil_and_gas_supply'],
        linewidth=lw, color='black', linestyle='--')
ax.plot(df.loc[2019:2040, 'low_oil_and_gas_supply'],
        linewidth=lw, color='black', linestyle='--')
# ax.plot(df.loc[5, '2019':'2040'], linewidth=lw)
# ax.plot(df.loc[6, '2019':'2040'], linewidth=lw)
ax.plot(df.loc[2019:2040, 'reference'], linewidth=lw,
        color='#0a8d8f', linestyle='--')
# ax.axvline(x=2019, linestyle='--', color='grey')
ax.set_xticks(np.arange(2010, 2045, 5))
plt.xticks(fontsize=l_size)
plt.yticks(fontsize=l_size)
x2 = 0.53

ax.set_xlim([2010, 2040])
# ax.set_ylim([0, 3.5])
title = 'EIA Annual Energy Outlook 2020\nProjected Annual Henry Hub Natural Gas Price'
ax.set_title(title, fontsize=20)
ax.set_ylabel('USD per Million Btu', fontsize=m_size)
ax.fill_between(x, y1, y2, alpha=0.2)
plt.text(0.1045, 0.01, source, fontsize=l_size,
         transform=plt.gcf().transFigure)
plt.text(x2, 0.79, 'Low Oil and Gas Supply',
         fontsize=m_size, transform=plt.gcf().transFigure)
plt.text(x2, 0.425, 'Reference Case',
         fontsize=m_size, color='#0a8d8f', transform=plt.gcf().transFigure)
plt.text(0.16, 0.64, 'Historical Price',
         fontsize=m_size, color='#0a8d8f', transform=plt.gcf().transFigure)
plt.text(x2, 0.29, 'High Oil and Gas Supply',
         fontsize=m_size, transform=plt.gcf().transFigure)


plt.show()
