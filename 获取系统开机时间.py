# -*- coding: utf-8 -*-
import datetime
import psutil

# 获取系统开机时间
time = psutil.boot_time()
date = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")
print '开机时间是：'
print date
