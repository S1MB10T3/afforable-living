import datetime
import pandas as pd
import requests

# https://factfinder-api.herokuapp.com/

HOST = "https://api.census.gov/data"
dataset= "acs/acs5"

years = ["2018","2017","2016","2015","2014","2013","2012","2011"]
zip_code = "11221"

#
get_vars = ["B01003_001E", "B10010_001E"]

predicates = {}

predicates["key"] = ""
predicates["get"] = ",".join(get_vars)
predicates["for"] = "zip code tabulation area:" + zip_code

storage = []

for year in years:
    try:
        base_url = "/".join([HOST, year, dataset])
        r = requests.get(base_url, params=predicates)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    else:
        # print(r.json()[1])
        storage.append([year] + r.json()[1])

col_names = ["year", "total_pop", "avg_income", "zip"]

df = pd.DataFrame(columns=col_names, data=storage)

df["total_pop"] = df["total_pop"].astype(int)
df["avg_income"] = df["avg_income"].astype(int)

print(df.head())
