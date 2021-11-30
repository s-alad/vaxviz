#contains all functions from part 2, 3

import csv
import json
import urllib.request


def dic_list_gen(keys, vals):
    return [dict(zip(keys, vals)) for vals in vals]

def read_values(file):
    return [row for row in csv.reader(open(file))][1:]

def make_lists(keys, lod):
    return [[item[key] for key in keys] for item in lod]

def write_values(file, lol):
    csv.writer(open(file, 'a+', newline='')).writerows(lol)

def json_loader(url):
    return json.loads(urllib.request.urlopen(url).read())

def make_values_numeric(keys, dic):
    for key in keys:
        if key in dic: dic[key] = float(dic[key])
    return dic  

def save_data(keys, dic, file):
    writer = csv.writer(open(file, 'w+', newline=''))
    writer.writerow(keys)
    for item in dic: writer.writerow([item[key] for key in keys])

def load_data(f):
    l = []
    reader = csv.reader(open(f, "r"))
    header = next(reader)
    for row in reader:
        d = {}
        for i in range(len(header)): d[header[i]] = row[i]
        l.append(d)
    return l