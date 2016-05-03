from yaml import load

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader

data_stream = open('../config/database.yml', 'r')

db_config = load(data_stream, Loader=Loader)

print(db_config)

print(db_config['production']['port'])
