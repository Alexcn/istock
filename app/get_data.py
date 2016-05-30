import tushare as ts
import psycopg2
from sqlalchemy.dialects.postgresql import *

from yaml import load

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader
data_stream = open('../config/database.yml', 'r')
db_config = load(data_stream, Loader=Loader)
data_stream.close()

USER = db_config['production']['username']
HOST = db_config['production']['host']
PASSWORD = db_config['production']['password']
DATABASE = db_config['production']['database']




engine = 'postgres://%s:%s@%s/%s' % (USER, PASSWORD, HOST, DATABASE)


conn = psycopg2.connect(host=db_config['production']['host'], database=db_config['production']['database'], user=db_config['production']['username'], password=db_config['production']['password'])

cur = conn.cursor()


# 获取历史数据,存到数据库
hist_data_type = {
    'date': DATE,
    'code': CHAR(6)
}
cur.execute('select distinct code from stock_basics;')

r = cur.fetchall()

for row in r:
    print('获取 ' + row[0] + ' 的历史行情')
    d = ts.get_hist_data(row[0])
    d['code'] = row[0]
    d.to_sql('hist_data', engine, if_exists='append', dtype=hist_data_type)



