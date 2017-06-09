#!/usr/bin/env python
# coding=utf-8

import tushare as ts

stock_basic_info = ts.get_stock_basics().index

for item in stock_basic_info:
    print(item)

# hist = ts.get_k_data()


