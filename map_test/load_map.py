import json

import csv

MAP = 'maps/map1.csv'




reader = csv.reader(open(MAP), delimiter=',', quotechar='"')
map1 = ([x for x in reader])
