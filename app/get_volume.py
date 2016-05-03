import tushare as ts
import psycopg2
from sqlalchemy import create_engine
from yaml import load

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader
data_stream = open('../config/database.yml', 'r')
db_config = load(data_stream, Loader=Loader)


# connect_url = 'postgres://%s:%s@%s/%s' % (USER, PASSWORD, HOST, DATABASE)
engine = create_engine('postgres://light:1204516@localhost/stock_20160426')

# 一次获取全部日 K 线数据
t = ts.get_hist_data('600848')

# 获取沪深上市公司的基本情况
ts.get_stock_basics()

conn = psycopg2.connect(host=db_config['production']['host'], database=db_config['production']['database'], user=db_config['production']['username'], password=db_config['production']['password'])

cur = conn.cursor()

cur.execute('select code from stock_basics;')

r = cur.fetchall()

for row in r:
    print(row[0])
