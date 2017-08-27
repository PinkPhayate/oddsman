# Oddsman

## Overview
This is module implemented by python to display rate of house rasing.

Document is until not ready.


## Environment

- Python 3.5.1
- Dependent module are shown in requirement.txt

## install
enter below commands

```sudo pip install git+https://github.com/PinkPhayate/oddsman@master```

## useage
```
from oddsman import oddsman
ods = oddsman.OddsWatcher()
```

## Document of API
### get\_race\_ids(time: str)

* paramater

	time: str	日付

* feature
	
	パラメータで入力した日付のレースを確認し、あれば出走時刻をkeyとしたdicttionaryを返す

* example

```
from oddsman import OddsWatcher
odds_man = OddsWatcher()
todays_race_id = odds_man.get_race_ids('0625')
# => {'10:45': '201702010403', '10:55': '201705030803', '16:15': '201705030812', '12:35': '201702010406', '12:55': '201709030806', '12:45': '201705030806', '11:05': '201709030803', '10:05': '201709030801', '15:30': '201705030811', '13:35': '201702010408', '12:25': '201709030805', '13:15': '201705030807', '09:55': '201705030801', '10:15': '201702010402', '14:15': '201705030809', '14:50': '201705030810', '10:35': '201709030802', '14:05': '201702010409', '15:40': '201709030811', '16:30': '201709030812', '10:25': '201705030802', '12:15': '201705030805', '12:05': '201702010405', '16:05': '201702010412', '11:35': '201709030804', '14:40': '201702010410', '15:01': '201709030810', '15:20': '201702010411', '13:25': '201709030807', '13:45': '201705030808', '09:50': '201702010401', '13:05': '201702010407', '14:25': '201709030809', '11:15': '201702010404', '13:55': '201709030808', '11:25': '201705030804'}
```

### get\_race\_odds(race\_id: str)

* paramater

	race\_id: str	レースid

* feature
	
	オッズを調べたいレースのidを入力すると、オッズが返ってくる

* example

```
from oddsman import OddsWatcher
odds_man = OddsWatcher()
race_id = '201702010412'
odds_dict = odds_man.get_race_odds(race_id)
# => {津軽海峡特別: ['61.0', '93.9', '33.4', '69.3', '1.6', '7.9', '44.9', '11.3', '3.5', '22.1']}
```
