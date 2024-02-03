from collections import defaultdict
import csv

# Specify the path to your CSV file
paths = ['videohashtags.csv','videohashtags2.csv', 'paidvideohashtags.csv']

def is_ascii(s):
    return all(ord(char) < 128 for char in s)

map_of_hashtags = {}
for path in paths:
    csv_file_path = path
    # Open the CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        # Create a CSV DictReader object
        csv_reader = csv.DictReader(file)
        
        # Iterate through the rows in the CSV file
        for row in csv_reader:
            # Each 'row' is a dictionary with column names as keys
            hashtagString = row['hashtags'].split()
            for hashtag in hashtagString:
                if is_ascii(hashtag):
                    map_of_hashtags[hashtag] = map_of_hashtags.get(hashtag, 0) + 1


map_of_hashtags = dict(sorted(map_of_hashtags.items(), key=lambda x: x[1], reverse=True))

# Specify the CSV file path
csv_file_path = 'hashtags_counts.csv'

# Open the CSV file in write mode
with open(csv_file_path, 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Hashtag', 'Count'])

    # Write the values from the hashmap
    for hashtag, count in map_of_hashtags.items():
        csv_writer.writerow([hashtag, count])
        
        