import os
import requests
import json
import pandas as pd

def grab_series(series_id = "DJIA", start="2013-04-01", end="2013-05-01"):
    base = "http://api.stlouisfed.org/fred/series/observations"
    series = "?series_id=%s" % series_id
    api_key = os.environ["FED_API_KEY"]
    url = "%s%s&api_key=%s&file_type=json" % (base, series, api_key)
    r =  requests.get(url).content
    obs = json.loads(r)
    return pd.DataFrame(obs['observations'])
    
    
    


