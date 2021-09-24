import pandas as pd

weather = pd.read_csv('./weather.csv')
print(weather.head())
print(weather.shape)

melt_data = weather.melt(id_vars=['id', 'year', 'month', 'element'], var_name='day', value_name='temp')

print(melt_data.head())

data_tidy = melt_data.pivot_table(index=['id', 'year', 'month', 'day'], columns='element', values='temp')

print(data_tidy.head())

data_reset = data_tidy.reset_index()

print(data_reset.head())

data_reset.to_csv('weathercleandata.csv', index= False)
