from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# ===============================================================
from collections import defaultdict
import csv
from graph.node import HashtagNode
from graph.getCounts import get_count 
import json
from graph.get_clusters import get_clusters
import random


def addNodes(hashtags):
    for i in range(len(hashtags)):
        hashtag = hashtags[i]
        if hashtag == 'fyp' or hashtag == 'foryou' or hashtag == 'viral' or hashtag == 'foryoupage' or hashtag == 'fy' or hashtag == 'trending':
            continue
        
        # use valid letters only
        
        if is_ascii(hashtag) and map_of_hashtags[hashtag] >= 5:
            # create node if not already created and add video url
            if hashtag not in nodes:
                nodes[hashtag] = HashtagNode(hashtag)
            nodes[hashtag].add_video(row['webVideoUrl'])
            for j in range(i+1, len(hashtags)):
                hashtag2 = hashtags[j]
                if hashtag2 == 'fyp' or hashtag2 == 'foryou' or hashtag2 == 'viral' or hashtag2 == 'foryoupage' or hashtag2 == 'fy' or hashtag2 == 'trending':
                    continue
                if is_ascii(hashtag2) and map_of_hashtags[hashtag2] >= 5:
                    # create node if not already created and add video url
                    if hashtag2 not in nodes:
                        nodes[hashtag2] = HashtagNode(hashtag2)
                    nodes[hashtag2].add_video(row['webVideoUrl'])
                    
                    # add the edge for both hashtag and hashtag2
                    nodes[hashtag].add_to(hashtag2)
                    nodes[hashtag2].add_to(hashtag)
                
def addUserNodes(hashtags):
    for i in range(len(hashtags)):
        hashtag = hashtags[i]
        if hashtag == 'fyp' or hashtag == 'foryou' or hashtag == 'viral' or hashtag == 'foryoupage' or hashtag == 'fy' or hashtag == 'trending':
            continue
        
        # use valid letters only
        
        if is_ascii(hashtag):
            # create node if not already created and add video url
            if hashtag not in user1Nodes:
                user1Nodes[hashtag] = HashtagNode(hashtag)
            user1Nodes[hashtag].add_video('N/A')
            for j in range(i+1, len(hashtags)):
                hashtag2 = hashtags[j]
                if hashtag2 == 'fyp' or hashtag2 == 'foryou' or hashtag2 == 'viral' or hashtag2 == 'foryoupage' or hashtag2 == 'fy' or hashtag2 == 'trending':
                    continue
                if is_ascii(hashtag2):
                    # create node if not already created and add video url
                    if hashtag2 not in user1Nodes:
                        user1Nodes[hashtag2] = HashtagNode(hashtag2)
                    user1Nodes[hashtag2].add_video('N/A')
                    
                    # add the edge for both hashtag and hashtag2
                    user1Nodes[hashtag].add_to(hashtag2)
                    user1Nodes[hashtag2].add_to(hashtag)      



def get_inverted_clusters(clusters):
    inverted_clusters = {}
    for name, number in clusters.items():
        inverted_clusters.setdefault(number,[]).append(name)
    top_3_numbers = sorted(inverted_clusters, key=lambda x: len(inverted_clusters[x]), reverse=True)[:3]
    topOne = inverted_clusters[top_3_numbers[0]]
    topTwo = inverted_clusters[top_3_numbers[1]]
    topThree = inverted_clusters[top_3_numbers[2]]
    return (topOne, topTwo, topThree)


def generate_random_color():
    # Generate random values for the RGB components within a certain range
    r = random.randint(50, 205) 
    g = random.randint(0, 255)  
    b = random.randint(0, 255)  
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)  # Format the color code


# returns an array of clusters that nodes are part of
# example output: [1, 4, 39]
def get_cluster_number_for_nodes(nodes):
    # we do not want duplicates of cluster ids
    outSet = {}
    for key, val in nodes.items():
        name = val.get_value()
        
        # name starts with '#'
        hashtag = name[1:]
        
        # the dataset we are loading did not hold these
        # if hashtag == 'fyp' or hashtag == 'foryou' or hashtag == 'viral' or hashtag == 'foryoupage' or hashtag == 'fy' or hashtag == 'trending':
        #     continue
        
        if hashtag in clusters:
            outSet[clusters[hashtag]] = outSet.get(clusters[hashtag], 0) + 1

    sorted_outSet = dict(sorted(outSet.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_outSet.keys())[0:10]




def format_nodes(nodes):
    formatted_nodes = []
    min_value = 0.01
    max_value = 320
    target_min = 5
    target_max = 25000

    for key, val in nodes.items():
        style = ""
        color = "#FF5733"
        if key in clusters:
            clusterId = clusters[key]
            color = colors[clusterId]

                    
        if key in user1Nodes.keys():
            style += "User1"
            # no toggle for time being --> new request with different params required from front end to load user. Quentin knows what this means
            color = "#FF5733"
        
        normalized_value = (val.get_weight() - min_value) / (max_value - min_value)
        scaled_value = target_min + normalized_value * (target_max - target_min)

        node_info = {
            "id": key,  # Assuming the ID is the hashtag itself
            "name": f"#{key}",
            "val": scaled_value,  # Assuming 'val' represents the number of edges
            "color": color,
            "style": style,
            "video_links": val.get_videos(),
        }

        formatted_nodes.append(node_info)

    return formatted_nodes



def format_user_nodes(nodes, user1Nodes):
    formatted_nodes = []
    allKeys = get_cluster_number_for_nodes(user1Nodes)
    min_value = 0.01
    max_value = 320
    target_min = 5
    target_max = 25000
    
    for key, val in nodes.items():
        color = '#000000'
        style = ""

        if key in clusters:
            if clusters[key] in allKeys:
                clusterId = clusters[key]
                color = colors[clusterId]
                style = "User1" 
            else:
                color = '#000000'
            style = ""
        else:
            color = '#000000'
            style = ""

        normalized_value = (val.get_weight() - min_value) / (max_value - min_value)
        scaled_value = target_min + normalized_value * (target_max - target_min)

        node_info = {
            "id": key,  # Assuming the ID is the hashtag itself
            "name": f"#{key}",
            "val": scaled_value,  # Assuming 'val' represents the number of edges
            "color": color,
            "style": style,
            "video_links": val.get_videos(),
        } 

        formatted_nodes.append(node_info)
    
    return formatted_nodes

# map_of_hashtags = get_count(['csv_files/videohashtags.csv','csv_files/videohashtags2.csv', 'csv_files/paidvideohashtags.csv', 'csv_files/paidvideohashtags2.csv', 'csv_files/scrapedhashtags.csv'])
# map_of_user_hashtags = get_count(['csv_files/brayhashtags.csv'])

# # Specify the path to your CSV file
# paths = ['./csv_files/videohashtags.csv', './csv_files/videohashtags2.csv', './csv_files/paidvideohashtags.csv', './csv_files/paidvideohashtags2.csv']
# # paths = ['csv_files/braydensample.csv']
# def is_ascii(s):
#     return all(ord(char) < 128 for char in s)

# userPath = 'csv_files/brayhashtags.csv'
# nodes = {}
# user1Nodes = {}

# for path in paths:
#     csv_file_path = path
#     # Open the CSV file
#     with open(csv_file_path, 'r', encoding='utf-8') as file:
#         # Create a CSV DictReader object
#         csv_reader = csv.DictReader(file)
        
#         # Iterate through the rows in the CSV file
#         for row in csv_reader:
#             # Each 'row' is a dictionary with column names as keys
#             hashtags = sorted(row['hashtags'].split())
#             addNodes(hashtags)



# with open(userPath, 'r', encoding='utf-8') as file:
#     # Create a CSV DictReader object
#     csv_reader = csv.DictReader(file)
    
#     # Iterate through the rows in the CSV file
#     for row in csv_reader:
#         # Each 'row' is a dictionary with column names as keys
#         hashtags = sorted(row['hashtags'].split())
#         addUserNodes(hashtags)
    

# clusters = get_clusters(nodes) # clusters: name --> cluster_number
# numClusters = max(clusters.values())

# colors = [generate_random_color() for _ in range(numClusters + 1)]


# formatted_links = []       
# for key, val in nodes.items():
#     formatted_links += val.get_links()

# # USER
# user_formatted_links = []       
# for key, val in user1Nodes.items():
#     user_formatted_links += val.get_user_links() # links in this sense are edges

# formatted_nodes = format_nodes(nodes)
# user_formatted_nodes = format_user_nodes(nodes, user1Nodes)



@app.route('/api/graph-user-data', methods=['GET'])
def get_graph_user_data():
    # graph_data = {"nodes": user_formatted_nodes, "links": formatted_links}

    file_path = "./graph/graph_user_data.json"
    with open(file_path, "r") as json_file:
        json_data = json_file.read()

    graph_data_from_file = json.loads(json_data)

    # json_data = json.dumps(graph_data, indent=4)
    # with open(file_path, "w") as json_file:
    #     json_file.write(json_data)

    # Returning the graph data as JSON
    return jsonify(graph_data_from_file)


@app.route('/api/graph-data', methods=['GET'])
def get_graph_data():
    # Preparing the graph data
    # graph_data = {"nodes": formatted_nodes, "links": formatted_links}

    file_path = "./graph/graph_data.json"
    with open(file_path, "r") as json_file:
        json_data = json_file.read()

    graph_data_from_file = json.loads(json_data)

    # json_data = json.dumps(graph_data, indent=4)
    # with open(file_path, "w") as json_file:
    #     json_file.write(json_data)


    # Returning the graph data as JSON
    return jsonify(graph_data_from_file)




if __name__ == '__main__':
    app.run(ssl_context='adhoc')
