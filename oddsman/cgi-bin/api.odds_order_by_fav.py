#!/usr/bin/env python
import oddsman

print("Content-Type: text/plain")
print()


ow = oddsman.OddsWatcher()
# レースIDの表示
# later_race_ids = ow.get_later_race_ids()
# print(later_race_ids)

# odds = ow.get_nearest_odds()
# print(odds)

# 馬番順のオッズを返す
odds_list = ow.get_race_history_odds('201707030312')
print(odds_list)

# 馬番とオッズのリストがオッズでソートして返す
odds_list = ow.get_race_history_sorted_odds_list('201707030312')
print(odds_list)
