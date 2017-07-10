from bs4 import BeautifulSoup
from urllib import request
from datetime import datetime, date

class OddsWatcher(object):
    def __get_request_via_get(self, url):
        source = request.urlopen(url)
        return source

    def __find_hid(self, td):
        # get hid
        for link in td.findAll('a'):
            url = link.attrs['href']
            if "/horse/" in link.attrs['href']:
                tmp = url.split('/')
                return tmp[4]
        return None

    def __find_rid(self, td):
        # get rid
        for link in td.findAll('a'):
            url = link.attrs['href']
            if "&" in url:
                tmp = url.split('&')
                tmp = tmp[1].split('=')
                return tmp[1][1:]
        return None

    def __extract_time(self, text):
        text = text.strip()
        time = text[:5]
        return time

    def __2dict(self, df, time_df):
        if len(df) != len(time_df):
            print("file length is different. void dictionalize")
            return
        dict = {}
        for (rid, time) in zip(df, time_df):
            dict[time] = rid
        return dict

    def __find_race_time(self, div):
        text = div.text
        time = self.__extract_time(text)
        if time is not None:
            return time
        return None

    def __scrape_race_info(self, source):
        soup = BeautifulSoup(source, "lxml")
        df = []
        # Extract status
        title = soup.find('h1')
        # print(title.text)
        self.title = title.text
        # if title.text is not correct (e.g. another race), remove
        table = soup.find(class_='race_table_old nk_tb_common')
        for tr in table.findAll('tr', ''):
            row = []
            for td in tr.findAll('td', ''):
                # get house status
                word = " ".join(td.text.rsplit())
                row.append(word)

                hid = self.__find_hid(td)
                if hid is not None:
                    row.append(hid)
            df.append(row)
        return df

    def __scrape_race_id(self, source):
        soup = BeautifulSoup(source, "lxml")
        df = []
        time_df = []
        body = soup.find(id="race_list_body")
        for col in body.findAll(class_='race_top_hold_list'):
            row = []
            times = []
            for div in col.findAll(class_='racename'):
                rid = self.__find_rid(div)
                if rid is not None:
                    row.append(rid)
            df.append(row)

            for div in col.findAll(class_='racedata'):
                time = self.__find_race_time(div)
                if time is not None:
                    times.append(time)
            time_df.append(times)
            dict = self.__2dict(row, times)
            yield dict

    def __formalize(self, str):
        return ('0'+str) if len(str) == 1 else str

    def __get_today_data(self):
        dt = datetime.now()
        month = self.__formalize(str(dt.month))
        day = self.__formalize(str(dt.day))
        return month + day

    def __get_now_time(self):
        dt = datetime.now()
        hour = self.__formalize(str(dt.hour))
        minute = self.__formalize(str(dt.minute))
        return hour + minute

    def __to_dict(self, list):
        dict = {}
        for i in range(len(list)):
            dict[i+1] = list[i]
        return dict

    def __get_later_race_ids(self, dict=None):
        if dict is None:
            today_data = self.__get_today_data()
            dict = self.get_race_ids(today_data)
        times_str = list(dict.keys())
        sorted_times_list = sorted(times_str, key=lambda x: x.replace(':', ''))
        now_time = self.__get_now_time()
        return [x for x in sorted_times_list if int(now_time) < int(x.replace(':', '') if(':' in x) else 0)]

    def __get_nearest_race_id(self):
        # race_idを持っているdictは一日で一回で良い?
        today_data = self.__get_today_data()
        for i in range(1, 7):
            data = str(int(today_data) + i)
            dict = self.get_race_ids(data)
            if 0 < len(dict):
                break
        else:
            # TODO
            print('[error] Could not find any race for a week')
            return None
        # このリストは時間によって変わるから
        list = self.__get_later_race_ids(dict=dict)
        if 0 < len(list):
            return dict[list[0]]

    def get_race_odds(self, race_id):
        url = 'http://race.netkeiba.com/?pid=race_old&id=c' + str(race_id)
        source = self.__get_request_via_get(url)
        self.df = self.__scrape_race_info(source)
        odds_list = [float(x[9]) for x in self.df if len(x) > 0]
        return odds_list

    def get_race_history_odds(self, race_id):
        url = 'http://race.netkeiba.com/?pid=race_old&id=c' + str(race_id)
        source = self.__get_request_via_get(url)
        self.df = self.__scrape_race_info(source)
        odds_list = [float(x[10]) for x in self.df if len(x) > 0]
        return odds_list

    def get_race_history_sorted_odds_list(self, race_id=None):
        # race_idの指定がない時は最新のレースidを持ってくる
        if race_id is None:
            # このrace_idはキャッシュしても良い。
            race_id = self.__get_nearest_race_id()
            odds_list = self.get_race_odds(race_id)
        else:
            odds_list = self.get_race_history_odds(race_id=race_id)
        dict = self.__to_dict(odds_list)
        return sorted(dict.items(), key=lambda x: x[1])

    def get_race_ids(self, date):
        # まだ開催されていないレースがc、開催終わってる日はp？？?
        url = 'http://race.netkeiba.com/?pid=race_list&id=c' + str(date)
        print('[info] request: ' + url)
        source = self.__get_request_via_get(url)
        dict = {}
        for d in self.__scrape_race_id(source):
            dict.update(d)
        return dict

    def get_sorted_race_ids(self, date):
        race_ids = self.get_race_ids(date)
        return sorted(race_ids.items(), key=lambda x: x[0])
