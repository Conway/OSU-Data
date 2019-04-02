# Locations

This sub-repository contains locations of buildings at The Ohio State University's Columbus campus. The data was taken from [OSU's official map](https://www.osu.edu/map/buildingindex.php), and matched to data from the Google Maps geocode API.

## File description

|file|decription|
|:--|:--|
|[locations.csv](https://github.com/Conway/OSU-Data/blob/master/locations/locations.csv)|the dataset itself|
|[cleaner.py](https://github.com/Conway/OSU-Data/blob/master/locations/cleaner.py)|the script used to transform `raw_text.txt` to `locations.csv`|
|[raw_data.txt](https://github.com/Conway/OSU-Data/blob/master/locations/raw_data.txt)|the data fed into the script to be cleaned and matched to coordinates|

## Data Description

|field|description|
|:--|:--|
|`building_num`|The code that OSU uses to reference this building internally|
|`building_name`|The name of the building|
|`building_code`|Used as a prefix for classrooms and offices|
|`lat`|The building's latitude|
|`long`|The building's longitude|
