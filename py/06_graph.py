import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/06_november_generator_2020_active.csv'
path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/06_december_generator_2019_active.csv'


df = call_file(path)

print(df.columns)

# print(df['Technology'].value_counts())
# print(df['Operating Year'].value_counts())

df = df[df['Technology'] == 'Conventional Steam Coal']

# print(df['Technology'].value_counts())
# print(df['Operating Year'].value_counts())

df1 = df.copy()

df = df[df['Operating Year'] > 2000]

# print(df['Technology'].value_counts())
# print(df['Operating Year'].value_counts())


df = df.reset_index(drop=True)

df['Nameplate Capacity (MW)'] = df['Nameplate Capacity (MW)'].replace(
    ',', '', regex=True)
df['Nameplate Capacity (MW)'] = df['Nameplate Capacity (MW)'].astype(float)

print('2040 Coal Capacity (MW): ', sum(df['Nameplate Capacity (MW)']))


# print(df1['Technology'].value_counts())
# print(df1['Operating Year'].value_counts())


df1 = df1.reset_index(drop=True)

df1['Nameplate Capacity (MW)'] = df1['Nameplate Capacity (MW)'].replace(
    ',', '', regex=True)
df1['Nameplate Capacity (MW)'] = df1['Nameplate Capacity (MW)'].astype(float)

print('2020 Coal Capacity (MW): ', sum(df1['Nameplate Capacity (MW)']))

coal_capacity_2020 = sum(df1['Nameplate Capacity (MW)'])
coal_capacity_2040 = sum(df['Nameplate Capacity (MW)'])

total_elec_2020 = 3964656
coal_elec_2020 = 958732
ng_elec_2020 = 1477042

total_elec = total_elec_2020
ng_elec = ng_elec_2020

for yr in range(2020, 2041):
    total_elec = total_elec * (1.01)
    ng_elec = ng_elec * (1.008)

print('Total Electricity 2040:       ', total_elec)
print('Natural Gas Electricity 2040: ', ng_elec)

print('Electricity Ratio 2040/2020:          ', total_elec / total_elec_2020)
print('NG Electricity Ratio 2040/2020:       ', ng_elec / ng_elec_2020)

coal_elec_2040 = coal_capacity_2040 * coal_elec_2020 / coal_capacity_2020

share_ng_elec_2040 = ng_elec / total_elec
share_coal_elec_2040 = coal_elec_2040 / total_elec
share_other_elec_2040 = (total_elec - coal_elec_2040 - ng_elec) / total_elec

ff_elec_2040 = ng_elec + coal_elec_2040

share_ff_coal_elec_2040 = coal_elec_2040 / ff_elec_2040
share_ff_ng_elec_2040 = ng_elec / ff_elec_2040

print(print('Coal Gas Electricity 2040: ', coal_elec_2040))

print('Coal Electricity Share 2040: ', share_coal_elec_2040)
print('Natural Gas Electricity Share 2040: ', share_ng_elec_2040)
print('Other Electricity Share 2040: ', share_other_elec_2040)

elec1 = [share_ng_elec_2040, share_coal_elec_2040, share_other_elec_2040]
elec2 = [share_ff_ng_elec_2040, share_ff_coal_elec_2040]

colors = ['#2b81d3', '#84848c', '#fcc43c']
labels = ['Natural Gas', 'Coal', 'Other']

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, figsize=(10, 6))

title = '     2040 US Electricity Share Projection\n'

fig.suptitle(title, fontsize=20)

ax1.set_title('All Sources of Energy', fontsize=15)
ax2.set_title('Natural Gas and Coal Only', fontsize=15)


ax1.pie(elec1, colors=colors, labels=labels,
        autopct='%1.0f%%', textprops={'fontsize': 13})

ax2.pie(elec2, colors=['#2b81d3', '#84848c'], labels=[
        'Natural Gas', 'Coal'], autopct='%1.0f%%', textprops={'fontsize': 13})

plt.subplots_adjust(wspace=0.4)


plt.show()
