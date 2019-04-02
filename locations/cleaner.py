import csv
import re
import requests

building_exp = re.compile(r"\((\d{0,4})\)\s+([A-Za-z0-9,\-\s']+)\s+(\([A-Z]+\))?")
google_api_key = "" # add your own key here
city_search_data = " Columbus, OH"

def get_geodata(search_str):
    if search_str is None or len(search_str) < 1 or "unknown" in search_str.lower():
        return {"latitude": 0.0, "longitude": 0.0}
    data = {"address": search_str + city_search_data, "key": google_api_key}
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    try:
        response = requests.get(url, params=data)
        jrsp = response.json()['results']
        return {"latitude": jrsp[0]['geometry']['location']['lat'], "longitude": jrsp[0]['geometry']['location']['lng']}
    except:
        return {"latitude": 0.0, "longitude": 0.0}


with open("raw_data.txt", "r") as file:
    lines = file.readlines()

with open("output.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerow(["building_num", "building_name", "building_code", "lat", "long"])
    for line in lines:
        group = building_exp.findall(line)
        line = [group[0][0], group[0][1].strip(), ""]
        if len(group[0][2]) > 0:
            line[2] = group[0][2][1:len(group[0][2])-1]
        geo_data = get_geodata(group[0][1])
        line.append(geo_data['latitude'])
        line.append(geo_data['longitude'])
        writer.writerow(line)

