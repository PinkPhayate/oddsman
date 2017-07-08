from oddsman import oddsman


ow = oddsman.OddsWatcher()
later_race_ids = ow.get_later_race_ids()
print(later_race_ids)
odds = ow.get_nearest_odds()
print(odds)
