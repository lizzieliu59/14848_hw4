#! /usr/bin/python
import sys

cur_date = None

for line in sys.stdin:
    line = line.strip()
    date, temperature = line.split('\t')
    try:
        temperature = int(temperature)
    except ValueError:
        continue
    if cur_date == None:
        cur_date = date
        max_temp = temperature
    elif cur_date == date:
        max_temp = max(max_temp, temperature)
    else:
        print('%s\t%s' % (cur_date, max_temp))
        cur_date = date
        max_temp = temperature
if cur_date == date:
    print('%s\t%s' % (date, temperature))
