# Crime

This sub-repository contains OSU crime data from the OSU [daily crime log](http://dailycrimelog.osu.edu/Daily_Crime_Log_-_Columbus.pdf) from January 29, 2019 to March 30, 2019. 

The data was scraped from the PDF, and converted to a .csv using Python. Some manual data adjustment was required due to formatting inconsistencies in the PDF. 

Latitude and Longitude was pulled from the Google Maps geocode API.

## Data Description

|field|description|
|:--|:--|
|`case_num`|The internal case number|
|`reported_at`|The datetime that the crime was reported to OSU PD|
|`start_datetime`|The start time of the crime, or the time the crime was reported if unknown|
|`end_datetime`|The end time of the crime|
|`offenses`|A summary of what occurred|
|`location`|The building or general location the crime happened|
|`status`|One of `['Closed', 'Closed - Arrest', 'Open - Arrest', 'Open - Pending Investigation', 'CSA Victim Declined to Make Report', 'Unfounded']`|
|`lat`|The latitude of the location (0.0 if unavailable).|
|`lon`|The longitude of the location (0.0 if unavailable).|


