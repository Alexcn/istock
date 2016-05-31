import tushare as ts
from yaml import load

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader


# code here


config_stream = open('../config/config.yml', 'r')
config = load(data_stream, Loader=Loader)
config_stream.close()



