import requests
import csv

# define constants
google_api_key = ""
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


with open("osu_crimes.csv", "r+") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    print("case_num,reported_at,start_datetime,end_datetime,offenses,location,status,lat,lon")
    for row in csv_reader:
        print(",".join(row), end=",")
        data = get_geodata(row[5])
        print(str(data['latitude']), end=",")
        print(str(data['longitude']))

