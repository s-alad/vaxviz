#contains all functions from part 1

import csv
import json
import urllib

def max_value(data, key):
    return max([item[key] for item in data]) if bool(data) else ""

def init_dictionary(data, key):
    return {i : 0 for i in [item[key] for item in data if key in item]}

def sum_matches(lod, key, val, tgt):
    return sum([(item[tgt] if item[key] == val else 0) for item in lod])
    
def copy_matching(lod, key, val):
    return [item for item in lod if item[key] == val]