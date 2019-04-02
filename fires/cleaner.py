import csv

new_headers = ['datetime', 'reported', 'building', 'cause', 'explanation', 'property_damage', 'injuries', 'deaths']
with open("fire_data.csv", "r") as input_file:
    reader = csv.reader(input_file)
    with open("output.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(new_headers)
        next(reader)
        for row in reader:
            new_row = [' '.join([row[0], row[1]])] + row[2:6] + [row[6][1:]] + row[7:]
            writer.writerow(new_row)
