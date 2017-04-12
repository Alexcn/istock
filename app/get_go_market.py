#!/usr/bin/env python
# coding=utf-8

import tushare as ts

all_stock = ts.get_stock_basics()

print(len(all_stock))
