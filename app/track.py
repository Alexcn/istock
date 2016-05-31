import tushare as ts
from yaml import load

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader


# code here


data_stream = open('../config/database.yml', 'r')
db_config = load(data_stream, Loader=Loader)
data_stream.close()