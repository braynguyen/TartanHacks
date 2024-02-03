from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# ===============================================================
from collections import defaultdict
import csv
from graph.node import HashtagNode
from graph.getCounts import get_count 

# Record start time
map_of_hashtags = get_count()

# Specify the path to your CSV file
paths = ['./csv_files/videohashtags.csv', './csv_files/videohashtags2.csv', './csv_files/paidvideohashtags.csv', './csv_files/paidvideohashtags2.csv']
# paths = ['csv_files/braydensample.csv']
def is_ascii(s):
    return all(ord(char) < 128 for char in s)

nodes = {}

def addNodes(hashtags):
    for i in range(len(hashtags)):
        hashtag = hashtags[i]
        
        # use valid letters only
        if is_ascii(hashtag) and map_of_hashtags[hashtag] >= 100:
            # create node if not already created and add video url
            if hashtag not in nodes:
                nodes[hashtag] = HashtagNode(hashtag)
            nodes[hashtag].add_video(row['webVideoUrl'])
            for j in range(i+1, len(hashtags)):
                hashtag2 = hashtags[j]
                if is_ascii(hashtag2) and map_of_hashtags[hashtag2] >= 100:
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
            hashtags = sorted(row['hashtags'].split())
            addNodes(hashtags)
                    
for key, val in nodes.items():
    print(key)
    print(val.get_edges())

output_nodes = []
def format_nodes(nodes):
    formatted_nodes = []

    for key, val in nodes.items():

        node_info = {
            "id": key,  # Assuming the ID is the hashtag itself
            "name": val.value,
            "val": val.edgeWeightIn  # Assuming 'val' represents the number of edges
        }
        formatted_nodes.append(node_info)

    return formatted_nodes

# Example usage:

# formatted nodes will be sent to the client
formatted_nodes = format_nodes(nodes)
print(formatted_nodes)
# for node in formatted_nodes:
#     print(node)
# ===============================================================




@app.route('/api/graph-data', methods=['GET'])
def get_graph_data():
    # Preparing the graph data
    # nodes = [
    #     {"id": "id1", "name": "#booger", "val": 400},
    #     {"id": "id2", "name": "#bogger", "val": 42},
    #     {"id": "id3", "name": "#logger", "val": 10},
    #     {"id": "id4", "name": "#jogger", "val": 15},
    #     {"id": "id5", "name": "#fogger", "val": 20},
    # ] + [{"id": f"id{i+6}", "name": f"#name{i+6}", "val": (i+6) * 10} for i in range(95)]

    # links = [
    #     {"source": "id1", "target": "id2", "distance": 100},
    #     {"source": "id1", "target": "id3", "distance": 150},
    #     {"source": "id2", "target": "id4", "distance": 80},
    #     {"source": "id3", "target": "id4", "distance": 120},
    #     {"source": "id4", "target": "id5", "distance": 50},
    # ] + [{"source": f"id{i+6}", "target": f"id{i+7}", "distance": (i+7) * 2} for i in range(94)]

    graph_data = {"nodes": nodes, "links": links}

    # Returning the graph data as JSON
    return jsonify(graph_data)

if __name__ == '__main__':
    app.run(debug=True)
