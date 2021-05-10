#!/usr/bin/env python
# weather_test.py

from extract import json_extract

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2  # used to make web calls to weather APIs

import json

url_str = "https://api.weather.gov//stations/KSJT/observations/latest"

try:
    conditions = urllib2.urlopen(url_str)
except urllib2.HTTPError as e:
    e.msg = "{} (Did you set the API key?)".format(e.msg)
    raise (e)

json_string = conditions.read()                 # load into a json string
parsed_cond = json.loads(json_string.decode())  # parse the string into a json catalog
conditions.close()

print(parsed_cond['properties']['dewpoint']['value'])