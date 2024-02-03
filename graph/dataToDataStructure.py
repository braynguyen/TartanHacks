from collections import defaultdict
import csv
from node import HashtagNode

# Specify the path to your CSV file
# paths = ['../csv_files/videohashtags.csv','../csv_files/videohashtags2.csv', '../csv_files/paidvideohashtags.csv', '../csv_files/paidvideohashtags2.csv']
paths = ['csv_files/braydensample.csv']
def is_ascii(s):
    return all(ord(char) < 128 for char in s)

nodes = {}

def addNodes(hashtags):
    for i in range(len(hashtags)):
        hashtag = hashtags[i]
        
        # use valid letters only
        if is_ascii(hashtag):
            # create node if not already created and add video url
            if hashtag not in nodes:
                nodes[hashtag] = HashtagNode(hashtag)
            nodes[hashtag].add_video(row['webVideoUrl'])
            for j in range(i+1, len(hashtags)):
                hashtag2 = hashtags[j]
                if is_ascii(hashtag2):
                    # create node if not already created and add video url
                    if hashtag2 not in nodes:
                        nodes[hashtag2] = HashtagNode(hashtag2)
                    nodes[hashtag2].add_video(row['webVideoUrl'])
                    
                    # add the edge for both hashtag and hashtag2
                    nodes[hashtag].add_to(hashtag2)
                    nodes[hashtag2].add_to(hashtag)
                
                

for path in paths:
    csv_file_path = path
    # Open the CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        # Create a CSV DictReader object
        csv_reader = csv.DictReader(file)
        
        # Iterate through the rows in the CSV file
        for row in csv_reader:
            # Each 'row' is a dictionary with column names as keys
            hashtags = row['hashtags'].split()
            addNodes(hashtags)
                    
for key, val in nodes.items():
    print(key)
    print(val.get_edges())

        