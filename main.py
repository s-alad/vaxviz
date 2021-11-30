import bottle
import json
import data 
import processing 
import os

def load_data( ):
   csv_file = 'saved_data.csv'
   if not os.path.isfile(csv_file):
        url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
        info = data.json_loader(url)
        heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
        data.save_data(heads, info, 'saved_data.csv')


@bottle.route('/')
def index():
        return bottle.static_file('index.html', root='.')

@bottle.route('/viz.js/')
def viz():
        return bottle.static_file('viz.js', root='.')

@bottle.route("/bar")
def bar():
        print()

@bottle.route("/pie")
def pie():
        print()

@bottle.route("/line")
def line():
        print()


@bottle.post("/vacByDate")
def vacByDate():
        print("x")

@bottle.route("/vacByLoc")
def vacByLoc():
        print("y")

bottle.run(debug=True)

