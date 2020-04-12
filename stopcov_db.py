import sqlite3 as sq
import os
from datetime import datetime, date, time


path = os.path.dirname(os.path.abspath(__file__)) + '\\'
date = date.today().strftime("%Y-%m-%d")

class covData(object):
    """docstring for covData."""

    def __init__(self):
        super(covData, self).__init__()

    def sql(self):
        conn = sq.connect(path + 'regCov.db')
        return conn

    def sql_deploy(self, trans_city):
        c = self.sql()
        c.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS {}(date PRIMARY KEY,city, ill, good, dead)".format(trans_city))
        c.close()
        #print('База обновленна, таблицы созданы')

    def add_sql(self, city, ill, good, dead, trans_city):
        c = self.sql()
        c.cursor()
        insert = [date, city, ill, good, dead]
        c.execute("INSERT OR IGNORE INTO {} VALUES(?,?,?,?,?)".format(trans_city), insert)
        c.commit()
        c.close()

    def sql_exec_city(self, trans_city, indate):
        c = self.sql().cursor()
        x = []
        for i in c.execute('SELECT * FROM {} WHERE date=:date'.format(trans_city), {'date': indate}):
            x.append(list(i))
        c.close()
        return x

    def sql_exec_full(self, indate):
        c = self.sql().cursor()
        l = []
        for i in c.execute('SELECT * FROM covid WHERE date=:date', {'date': indate}):
            l.append(list(i))
        c.close()
        return l

    def add_sql_cov(self, total_ill, today_ill, total_rec, total_dead):
        c = self.sql()
        c.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS covid(date PRIMARY KEY, total_ill, today_ill, total_rec, total_dead)")
        insert = [date, total_ill, today_ill, total_rec, total_dead]
        c.execute("INSERT OR IGNORE INTO covid VALUES(?,?,?,?,?)", insert)
        c.commit()
        print('Данные успешно добавлены')
        c.close()
