import tushare as ts

connect_url = 'postgres://%s:%s@%s/%s' % (USER, PASSWORD, HOST, DATABASE)

# 一次获取全部日 K 线数据
t = ts.get_hist_data('600848')

# 获取沪深上市公司的基本情况
ts.get_stock_basics()
