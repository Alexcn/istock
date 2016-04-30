import tushare as ts
import psycopg2
from sqlalchemy import create_engine


# connect_url = 'postgres://%s:%s@%s/%s' % (USER, PASSWORD, HOST, DATABASE)
engine = create_engine('postgres://light:1204516@localhost/stock_20160426')

# 一次获取全部日 K 线数据
t = ts.get_hist_data('600848')

# 获取沪深上市公司的基本情况
ts.get_stock_basics()

conn = psycopg2.connect(database='stock_20160426', user='stock', password='1204516')

cur = conn.cursor()

cur.execute('select code from stock_basics;')


