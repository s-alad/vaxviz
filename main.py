import bottle
import json
import data 
import processing 
import os

file = 'data.csv'

def create_data(file):
   if not os.path.isfile(file):
        info = data.json_loader('https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27')
        heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
        data.save_data(heads, info, file)

create_data(file)
info = data.load_data(file)

@bottle.route('/')
def index():
        return bottle.static_file('index.html', root='.')

@bottle.route('/viz.js')
def viz():
        return bottle.static_file('viz.js', root='.')

@bottle.route('/styles.css')
def styles():
        return bottle.static_file('styles.css', root='.')

@bottle.route("/bar")
def bar():
    max_date = processing.max_value(info, 'date')
    max_date_info = processing.copy_matching(info, 'date', max_date)
    [data.make_values_numeric(['series_complete_pop_pct'], i) for i in max_date_info]

    x = processing.init_dictionary(max_date_info, 'location')
    y = processing.init_dictionary(max_date_info, 'series_complete_pop_pct')

    items = {'x': list(x.keys()), 'y': list(y.keys())}
    return json.dumps(items)

@bottle.route("/pie")
def pie():
    types = ["administered_janssen", "administered_pfizer", "administered_moderna", "administered_unk_manuf"]
    max_date = processing.max_value(info, 'date')
    max_date_info = processing.copy_matching(info, 'date', max_date)
    [data.make_values_numeric(types, i) for i in max_date_info]

    jansen = processing.sum_matches(max_date_info, 'date', max_date, types[0])
    pfizer = processing.sum_matches(max_date_info, 'date', max_date, types[1])
    modern = processing.sum_matches(max_date_info, 'date', max_date, types[2])
    unkown = processing.sum_matches(max_date_info, 'date', max_date, types[3])

    return json.dumps({"values":[jansen, pfizer, modern, unkown]})

@bottle.post("/line")
def line():
    location = bottle.request.body.read().decode()
    location_info = processing.copy_matching(info, 'location', location)
    location_info.sort(key = lambda x:x['date'])

    x = processing.init_dictionary(location_info, 'date')
    y = processing.init_dictionary(location_info, 'series_complete_pop_pct')

    items = {'x': list(x.keys()), 'y': list(y.keys())}
    return json.dumps(items)
    
bottle.run(debug=True)

