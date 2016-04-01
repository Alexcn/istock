#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import tushare as ts

ts.get_stock_basics()
ts.get_report_data(2014, 3)

