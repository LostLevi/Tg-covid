from stopcov_db import covData
from bs4 import BeautifulSoup
import requests as req
from datetime import datetime, date, time
from transliterate import translit
import re

upd_time = datetime.now().hour


class getSiteData():

    url = r'https://xn--80aesfpebagmfblc0a.xn--p1ai/'
    cv = covData()

    def __init__(self, url = url, cv = cv):
        self.url = url
        self.cv = cv

    def data(self):
        resp = req.get(self.url)

        soup = BeautifulSoup(resp.text, 'html.parser')

        s_table = soup.find("div", attrs={ "class" : "d-map__list"})

        tr_table_item = s_table.find_all('tr')

        tr_table_list = []

        def slugify(s):
            pattern = r'[^\w+]'
            z = translit(s, 'ru', reversed=True).lower()
            return re.sub(pattern, '', z)

        for x in range(len(tr_table_item)):
            th_table_item = tr_table_item[x].find('th').text
            all_td_list = tr_table_item[x].find_all('td')
            tr_table_list.append([th_table_item, all_td_list[0].text, all_td_list[1].text, all_td_list[2].text])

        for tc in tr_table_list:
            trans_c = slugify(tc[0])
            tc.append(trans_c)

        for i in tr_table_list:
            self.cv.sql_deploy(i[4])
            self.cv.add_sql(i[0], i[1], i[2], i[3], i[4])

        return tr_table_list

    def getTotal(self):
        resp = req.get(self.url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        count_all = soup.find("div", attrs={ "class" : "cv-countdown"})
        count_target = count_all.find_all("div", attrs={ "class" : "cv-countdown__item-value"})
        count_data = count_all.find_all("span")
        final_data = []
        for i, n in enumerate(count_data):
            if i != 0:
                x = count_data[i].text
                final_data.append(x.replace(' ', ''))
        self.cv.add_sql_cov(final_data[0], final_data[1], final_data[2], final_data[3])
        return final_data

class all_cities():
    def get():
        f = getSiteData()
        site_data = f.data()
        callback = []
        for n in site_data:
            callback.append(n[4])
        return callback

f = getSiteData()
#d = all_cities()
f.data()
f.getTotal()
all_cities.get()
