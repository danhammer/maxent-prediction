import os
import requests
import json
import pandas as pd
import datetime
import matplotlib.pyplot as plt

def grab_series(series_id = "DJIA", start = "1970-01-01"):
    base = "http://api.stlouisfed.org/fred/series/observations"
    series = "?series_id=%s" % series_id
    api_key = "&api_key=%s" % os.environ["FED_API_KEY"]
    date = "&observation_start=%s" % start
    url = "%s%s%s%s&file_type=json" % (base, series, date, api_key)
    r =  requests.get(url).content
    obs = json.loads(r)
    return pd.DataFrame(obs['observations'])
    
    
def plot_series(series_id = "UNRATENSA"):
    # Plots the observations associated with the supplied series id,
    # another popular id is `CPIAUCSL`.
    data = grab_series(series_id)
    def convert(date):
        return datetime.datetime.strptime(date, '%Y-%m-%d')
    
    data[['date']] = data[['date']].applymap(convert)
    data = data.set_index('date')

    # filter out null values
    data = data[data.value != "."]

    data['value'].plot()
    plt.show()
    return data

def search_fred(*terms):
    base = "http://api.stlouisfed.org/fred/series/search"
    search = "?search_text=%s" % "+".join(terms)
    api_key = "&api_key=%s" % os.environ["FED_API_KEY"]
    url = "%s%s%s&file_type=json" % (base, search, api_key)
    r =  requests.get(url).content
    obs = json.loads(r)
    
    def _process(d):
        return {'id': d['id'], 'title': d['title'], 'freq':d['frequency']}

    return map(_process, obs['seriess'])

def print_search(n = 10, *terms):
    res = search_fred(*terms)
    for x in res[0:n]:
        print "%s: %s (%s)" %(x['id'], x['title'], x['freq'])
