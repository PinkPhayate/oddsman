#!/usr/bin/env python3
import oddsman

ow = oddsman.OddsWatcher()
# レースIDの表示
# later_race_ids = ow.get_later_race_ids()
# print(later_race_ids)

# odds = ow.get_nearest_odds()
# print(odds)


odds_list = ow.get_race_history_odds('201707030312')
print(odds_list)
