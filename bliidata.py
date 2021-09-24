import pandas as pd

bill_data = pd.read_csv('./billboard.csv')
# print(bill_data.head())
# print(bill_data.columns)
bill_melt = bill_data.melt(id_vars=['year', 'artist', 'track', 'time', 'date.entered'], var_name='week',
                           value_name='rating')

# print(bill_melt.head())

bill_songs = bill_melt[['year', 'artist', 'track', 'time']]

bill_songs = bill_songs.drop_duplicates()

# print(bill_songs.head())
print(bill_songs.shape)

bill_songs['id'] = range(len(bill_songs))

print(bill_songs.head())

bill_rate = bill_melt.merge(bill_songs, on=['year', 'artist', 'track', 'time'])

print(bill_rate.head())

bill_rate.to_csv('billrating.csv', index= False)
