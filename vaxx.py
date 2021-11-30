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
    #return {key: float(val) if key in keys else val for key, val in dic.items()}
    for key in keys:
        if key in dic: dic[key] = float(dic[key])
    return dic  


def save_data(keys, dic, file):
    writer = csv.writer(open(file, 'w+', newline=''))
    writer.writerow(keys)
    for item in dic: writer.writerow([item[key] for key in keys])

def load_data(f):
    #return [dict(zip((next(csv.reader(open(f)))), (row[0].split(',')[0], row[1].split(',')[0]) )) for row in csv.reader(open(f))][1:]
    l = []
    reader = csv.reader(open(f, "r"))
    header = next(reader)
    print(header)
    for row in reader:
        d = {}
        for i in range(len(header)):
            d[header[i]] = row[i]
        l.append(d)
    return l


if (__name__ == "__main__"):
    data = [ 
        {'date': '2021-05-02T00:00:00.000', 'location': 'FL', 'administered_janssen': 555456, 'administered_moderna': 6733913, 'administered_pfizer': 8177075, 'administered_unk_manuf': 25210, 'series_complete_pop_pct': '29.9'},
        {'date': '2021-02-10T00:00:00.000', 'location': 'MI', 'administered_janssen': 0, 'administered_moderna': 475593, 'administered_pfizer': 883331, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '0'},
        {'date': '2021-01-07T00:00:00.000', 'location': 'WA', 'administered_janssen': 0, 'administered_moderna': 45562, 'administered_pfizer': 75768, 'administered_unk_manuf': 24, 'series_complete_pop_pct': '0'},
        {'date': '2021-07-28T00:00:00.000', 'location': 'MA', 'administered_janssen': 303420, 'administered_moderna': 3604736, 'administered_pfizer': 5194315, 'administered_unk_manuf': 211, 'series_complete_pop_pct': '63.7'},
        {'date': '2021-09-14T00:00:00.000', 'location': 'LTC', 'administered_janssen': 28413, 'administered_moderna': 2029626, 'administered_pfizer': 5883197, 'administered_unk_manuf': 7156, 'series_complete_pop_pct': '0'},
        {'date': '2021-03-12T00:00:00.000', 'location': 'WI', 'administered_janssen': 2870, 'administered_moderna': 885833, 'administered_pfizer': 1055899, 'administered_unk_manuf': 166, 'series_complete_pop_pct': '11.9'},
        {'date': '2021-01-31T00:00:00.000', 'location': 'MA', 'administered_janssen': 0, 'administered_moderna': 262495, 'administered_pfizer': 316671, 'administered_unk_manuf': 15, 'series_complete_pop_pct': '0'},
        {'date': '2021-04-16T00:00:00.000', 'location': 'DD2', 'administered_janssen': 60244, 'administered_moderna': 1098234, 'administered_pfizer': 1295112, 'administered_unk_manuf': 399, 'series_complete_pop_pct': '0'},
        {'date': '2021-01-08T00:00:00.000', 'location': 'GA', 'administered_janssen': 0, 'administered_moderna': 44572, 'administered_pfizer': 74517, 'administered_unk_manuf': 29, 'series_complete_pop_pct': '0'},
        {'date': '2021-06-07T00:00:00.000', 'location': 'MS', 'administered_janssen': 52118, 'administered_moderna': 845228, 'administered_pfizer': 892736, 'administered_unk_manuf': 891, 'series_complete_pop_pct': '27.5'},
        {'date': '2021-05-26T00:00:00.000', 'location': 'GU', 'administered_janssen': 2591, 'administered_moderna': 60250, 'administered_pfizer': 92455, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '42.3'},
        {'date': '2021-07-06T00:00:00.000', 'location': 'WY', 'administered_janssen': 17466, 'administered_moderna': 204625, 'administered_pfizer': 208822, 'administered_unk_manuf': 233, 'series_complete_pop_pct': '35.4'},
        {'date': '2020-12-22T00:00:00.000', 'location': 'KY', 'administered_janssen': 0, 'administered_moderna': 6, 'administered_pfizer': 7323, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '0'},
        {'date': '2021-08-21T00:00:00.000', 'location': 'DE', 'administered_janssen': 48617, 'administered_moderna': 443240, 'administered_pfizer': 637452, 'administered_unk_manuf': 957, 'series_complete_pop_pct': '54.3'},
        {'date': '2021-05-05T00:00:00.000', 'location': 'HI', 'administered_janssen': 21959, 'administered_moderna': 446155, 'administered_pfizer': 702262, 'administered_unk_manuf': 93760, 'series_complete_pop_pct': '37'},
        {'date': '2021-08-21T00:00:00.000', 'location': 'MH', 'administered_janssen': 1439, 'administered_moderna': 36386, 'administered_pfizer': 0, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '31.1'},
        {'date': '2020-12-21T00:00:00.000', 'location': 'AL', 'administered_janssen': 0, 'administered_moderna': 0, 'administered_pfizer': 6452, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '0'},
        {'date': '2020-12-28T00:00:00.000', 'location': 'MH', 'administered_janssen': 0, 'administered_moderna': 0, 'administered_pfizer': 0, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '0'},
        {'date': '2021-08-28T00:00:00.000', 'location': 'NE', 'administered_janssen': 75753, 'administered_moderna': 785799, 'administered_pfizer': 1188017, 'administered_unk_manuf': 4193, 'series_complete_pop_pct': '51.7'},
        {'date': '2021-07-13T00:00:00.000', 'location': 'MO', 'administered_janssen': 175197, 'administered_moderna': 1981544, 'administered_pfizer': 3066501, 'administered_unk_manuf': 498, 'series_complete_pop_pct': '39.8'},
        {'date': '2021-03-16T00:00:00.000', 'location': 'UT', 'administered_janssen': 22020, 'administered_moderna': 489949, 'administered_pfizer': 518661, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '8.6'},
        {'date': '2021-06-12T00:00:00.000', 'location': 'MP', 'administered_janssen': 323, 'administered_moderna': 7291, 'administered_pfizer': 43514, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '42.2'},
        {'date': '2021-07-19T00:00:00.000', 'location': 'MS', 'administered_janssen': 61671, 'administered_moderna': 932935, 'administered_pfizer': 1075150, 'administered_unk_manuf': 987, 'series_complete_pop_pct': '33.8'},
        {'date': '2021-06-18T00:00:00.000', 'location': 'MH', 'administered_janssen': 403, 'administered_moderna': 31017, 'administered_pfizer': 0, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '25.2'},
        {'date': '2021-03-09T00:00:00.000', 'location': 'CT', 'administered_janssen': 11205, 'administered_moderna': 557040, 'administered_pfizer': 677426, 'administered_unk_manuf': 16, 'series_complete_pop_pct': '9.7'},
        {'date': '2021-06-08T00:00:00.000', 'location': 'MH', 'administered_janssen': 385, 'administered_moderna': 30235, 'administered_pfizer': 0, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '24.2'},
        {'date': '2021-09-27T00:00:00.000', 'location': 'NV', 'administered_janssen': 150415, 'administered_moderna': 1212462, 'administered_pfizer': 2015657, 'administered_unk_manuf': 119, 'series_complete_pop_pct': '50.6'},
        {'date': '2021-05-11T00:00:00.000', 'location': 'BP2', 'administered_janssen': 3529, 'administered_moderna': 64097, 'administered_pfizer': 96162, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '0'},
        {'date': '2021-04-13T00:00:00.000', 'location': 'CO', 'administered_janssen': 129317, 'administered_moderna': 1611283, 'administered_pfizer': 1722461, 'administered_unk_manuf': 958, 'series_complete_pop_pct': '23.1'},
        {'date': '2021-03-12T00:00:00.000', 'location': 'SC', 'administered_janssen': 10601, 'administered_moderna': 545831, 'administered_pfizer': 935920, 'administered_unk_manuf': 1024, 'series_complete_pop_pct': '10.6'},
        {'date': '2021-09-11T00:00:00.000', 'location': 'NV', 'administered_janssen': 147212, 'administered_moderna': 1191843, 'administered_pfizer': 1939017, 'administered_unk_manuf': 23, 'series_complete_pop_pct': '49'},
        {'date': '2021-02-22T00:00:00.000', 'location': 'MD', 'administered_janssen': 0, 'administered_moderna': 547224, 'administered_pfizer': 563714, 'administered_unk_manuf': 591, 'series_complete_pop_pct': '0'},
        {'date': '2021-01-04T00:00:00.000', 'location': 'SC', 'administered_janssen': 0, 'administered_moderna': 4883, 'administered_pfizer': 56721, 'administered_unk_manuf': 11, 'series_complete_pop_pct': '0'},
        {'date': '2021-03-05T00:00:00.000', 'location': 'VT', 'administered_janssen': 0, 'administered_moderna': 96066, 'administered_pfizer': 83355, 'administered_unk_manuf': 159, 'series_complete_pop_pct': '9.7'},
        {'date': '2021-01-20T00:00:00.000', 'location': 'WY', 'administered_janssen': 0, 'administered_moderna': 13218, 'administered_pfizer': 16083, 'administered_unk_manuf': 8, 'series_complete_pop_pct': '0'},
        {'date': '2021-06-23T00:00:00.000', 'location': 'NY', 'administered_janssen': 924391, 'administered_moderna': 8601943, 'administered_pfizer': 11815978, 'administered_unk_manuf': 4821, 'series_complete_pop_pct': '52.5'},
        {'date': '2021-07-22T00:00:00.000', 'location': 'IH2', 'administered_janssen': 27010, 'administered_moderna': 779437, 'administered_pfizer': 669788, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '32.5'},
        {'date': '2021-02-13T00:00:00.000', 'location': 'WV', 'administered_janssen': 0, 'administered_moderna': 174009, 'administered_pfizer': 202104, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '0'},
        {'date': '2021-07-09T00:00:00.000', 'location': 'UT', 'administered_janssen': 125900, 'administered_moderna': 1169724, 'administered_pfizer': 1594653, 'administered_unk_manuf': 0, 'series_complete_pop_pct': '38'},
        {'date': '2021-07-03T00:00:00.000', 'location': 'CT', 'administered_janssen': 174538, 'administered_moderna': 1707771, 'administered_pfizer': 2539822, 'administered_unk_manuf': 540, 'series_complete_pop_pct': '60.9'} 
    ]

    def main():
        print('-')
        #print(max_value(data, 'series_complete_pop_pct'))
        #print(init_dictionary(data, 'location'))
        #print(sum_matches(data, 'location', 'NY', 'administered_moderna'))
        #print(copy_matching(data, 'location', 'NY'))
        #print(dic_list_gen(['Example','Other lengths'], [['Made-Up','Possible']]))
        #print(dic_list_gen(['Second'], [['Example'],['Also fake']]))
        #print(read_values("smallDataFile.csv"))
        #print(make_lists(['Example'], [{'Example': 'Made-up', 'Extra Keys' : 'Possible'}]))
        #print(write_values("pretend.csv", [['2021-08-07' ,'NY']]))
        #print(write_values("emp.csv", [['Hello There'], ['Embed , Comma']]))
        print(make_values_numeric(['number'], {'name' : 'ValJean', 'number' : '24601'}))
        #print(save_data(['date', 'location'], dl, 'bore.csv'))
        #print(load_data('sample.csv'))
        #print(make_values_numeric(["administered_moderna"], {"date": "2021-02-28T00:00:00.000", "location": "WI", "administered_janssen": "0", "administered_moderna": "636559", "administered_pfizer": "833889", "administered_unk_manuf": "122", "series_complete_pop_pct": "0"}))
        print(make_values_numeric(["series_complete_pop_pct", "administered_pfizer", "administered_moderna"], {"date": "2020-12-13T00:00:00.000", "location": "LTC", "administered_janssen": "0", "administered_moderna": "0", "administered_pfizer": "0", "administered_unk_manuf": "0", "series_complete_pop_pct": "0"}))
        print({"date": "2020-12-13T00:00:00.000", "location": "LTC", "administered_janssen": "0", "administered_moderna": 0.0, "administered_pfizer": 0.0, "administered_unk_manuf": "0", "series_complete_pop_pct": 0.0})
    main()