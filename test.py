from oddsman import oddsman

ow = oddsman.OddsWatcher()
dict = ow.get_race_ids('0701')
dict = ow.get_sorted_race_ids('0701')
print(dict)
