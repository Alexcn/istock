#!/usr/bin/env python
# coding=utf-8

import tushare as ts

stock_basic_info = ts.get_stock_basics()

hist = ts.get_k_data()
