import PyPDF2
import csv
import re

# define constants
log_location = "crime_log.pdf"
page_num_exp = re.compile(r"Page \d+ of \d+")
print_date_exp = re.compile(r"Printed on [A-Z][a-z]{3,} \d{1,2}, \d{4}")
total_records_exp = re.compile(r"Total Records: \d+")
crime_id_exp = re.compile(r"(P|CSA)\d+\-\d+")
status_types = ['Closed', 'Closed - Arrest', 'Open - Arrest', 'Open - Pending Investigation',
                'CSA Victim Declined to Make Report', 'Unfounded']
csv_headers = ['case_num', 'reported_at', 'start_datetime', 'end_datetime', 'offenses', 'location', 'status']
ignorable = ['Made by ', 'Case Number', 'Date/Time', 'Reported', 'Date/Time Occurred', 'Offenses', 'General Location',
             'Dispostion', 'Start', 'End']



# helper methods
def clean_list(lst):
    while len(lst[0]) < 1:
        lst.pop(0)


# open PDF
file = open(log_location, 'rb')
pdf = PyPDF2.PdfFileReader(file)

# extract all page text and add it to a list
raw_text = []
for page in pdf.pages:
    raw_text += page.extractText().split("\n")
file.close()

print(raw_text)

# remove headers and other repeating page info from input text
cleaned_data = []
for line in raw_text:
    if line in ignorable:
        continue
    elif bool(page_num_exp.match(line)):
        continue
    elif bool(print_date_exp.match(line)):
        continue
    elif "Crime Log " in line:
        continue
    else:
        cleaned_data.append(line)

# begin conversion to csv
output_data = list()
output_data.append(csv_headers)

# additional data cleansing + adding to output data
while not bool(total_records_exp.match(cleaned_data[0])):
    clean_list(cleaned_data)
    crime_id = cleaned_data.pop(0)
    clean_list(cleaned_data)
    reported_at = cleaned_data.pop(0)
    start_time = cleaned_data.pop(0)
    end_time = cleaned_data.pop(0)
    if len(end_time) < 1:
        end_time = None
    # the offenses are a mess since they get split up into multiple strings. this tries to fix that
    end_idx = 0
    while cleaned_data[end_idx] not in status_types and \
            cleaned_data[end_idx] not in [''] \
            and "intersection" not in cleaned_data[end_idx].lower():
        end_idx += 1
    offenses = []
    if cleaned_data[end_idx + 1] in status_types:
        while (end_idx - 2) >= 0:
            offenses.append(cleaned_data.pop(0))
            end_idx -= 1
    else:
        while (end_idx - 1) >= 0:
            offenses.append(cleaned_data.pop(0))
            end_idx -= 1
    offenses = " ".join(offenses)
    clean_list(cleaned_data)
    location = []
    while cleaned_data[0] not in status_types:
        location.append(cleaned_data.pop(0))
    location = " ".join(location)
    clean_list(cleaned_data)
    status = cleaned_data.pop(0)
    data = [crime_id.strip(), reported_at.strip(), start_time.strip(), end_time, offenses.strip(),
            location.strip(), status.strip()]
    output_data.append(data)



# write output file
with open('crime_Data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(output_data)


