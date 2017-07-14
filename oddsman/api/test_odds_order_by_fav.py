import oddsman
ow = oddsman.OddsWatcher()
odds_list = ow.get_race_odds('201707030312')
print(odds_list)
