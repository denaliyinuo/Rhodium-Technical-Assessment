import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/06_november_generator_2020.csv'

df = call_file(path)

# print(df.columns)

# 'Nameplate Capacity (MW)'
# 'Technology'
# 'Retirement Year'

print(df['Technology'].value_counts())

df1 = df[df['Technology'] == 'Conventional Steam Coal']
df1 = df1[df1['Retirement Year'] >= 2005]


df1['Nameplate Capacity (MW)'] = df1['Nameplate Capacity (MW)'].replace(
    ',', '')

print(df1['Retirement Year'].describe())
df1 = df1.reset_index(drop=True)

year = np.arange(2005, 2021)
retire = np.zeros(len(year))

for i in range(len(df1)):
    n = df1.loc[i, 'Retirement Year']
    index = np.where(year == n)
    # print(index[0][0])
    # print(year[index[0][0]])
    capacity = df1.loc[i, 'Nameplate Capacity (MW)'].replace(',', '')
    # print(capacity, type(capacity))
    print(retire[index[0][0]], type(retire[index[0][0]]))
    # capacity = capacity.astype(np.float)
    # capacity = np.fromstring(capacity, dtype=np.float64, count=-1)

    retire[index[0][0]] = retire[index[0][0]] + float(capacity)


# year = df1['Retirement Year'].value_counts().sort_index()

print(retire)

fig, ax = plt.subplots(sharex=True, figsize=(10, 6))

lw = 3

m_size = 15
l_size = 12

source = 'Source: EIA           * 2020 Retirements as of Nov 2020'

ax.bar(year, retire / 1000, color='black')
ax.set_facecolor('#ECECEC')

title = 'US Annual Coal Capacity Retirements\n'
ax.set_title(title, fontsize=20)

ax.set_ylabel('Capacity Retirements (GW)',
              fontsize=m_size)

plt.xticks(fontsize=l_size)
plt.yticks(fontsize=l_size)

ax.set_xlim([2004.5, 2020.5])
ax.set_xticks(np.arange(2005, 2021, 1))

plt.text(0.128, 0.01, source, fontsize=l_size,
         transform=plt.gcf().transFigure)
plt.text(0.894, 0.085, '*', fontsize=10, transform=plt.gcf().transFigure)


plt.show()
