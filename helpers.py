from stopcovparse import all_cities, getSiteData, update_db
from stopcov_db import covData
from datetime import datetime, date, time

date = date.today().strftime("%Y-%m-%d")
db = covData()

class dbHelper():
    def return_city_today(city):
        for i in all_cities.get():
            if i == city:
                x = db.sql_exec_city(i, date)
                return x

    def return_full_day(date):
        update_db()
        x = db.sql_exec_full(date)
        return x


#print(dbHelper.return_city_today('moskva'))
