from flask import Flask, jsonify
from flask_cors import CORS
import networkx as nx
from collections import defaultdict
import csv
from graph.node import HashtagNode
from graph.getCounts import get_count 

map_of_hashtags = get_count(['csv_files/videohashtags.csv','csv_files/videohashtags2.csv', 'csv_files/paidvideohashtags.csv', 'csv_files/paidvideohashtags2.csv'])
map_of_user_hashtags = get_count(['csv_files/brayhashtags.csv'])

# paths = ['./csv_files/videohashtags.csv', './csv_files/videohashtags2.csv', './csv_files/paidvideohashtags.csv', './csv_files/paidvideohashtags2.csv']
paths = ['csv_files/brayhashtags.csv']
def is_ascii(s):
    return all(ord(char) < 128 for char in s)

# userPath = 'csv_files/ShreyTags.csv'
nodes = {}
user1Nodes = {}

def addNodes(hashtags):
    for i in range(len(hashtags)):
        hashtag = hashtags[i]
        if hashtag == 'fyp' or hashtag == 'foryou' or hashtag == 'viral' or hashtag == 'foryoupage' or hashtag == 'fy' or hashtag == 'trending':
            # print(hashtag)
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
                    # print(hashtag)
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
        # if hashtag == 'fyp' or hashtag == 'foryou' or hashtag == 'viral' or hashtag == 'foryoupage' or hashtag == 'fy' or hashtag == 'trending':
        #     # print(hashtag)
        #     continue
        
        # use valid letters only
        
        if is_ascii(hashtag):
            # create node if not already created and add video url
            if hashtag not in user1Nodes:
                user1Nodes[hashtag] = HashtagNode(hashtag)
            user1Nodes[hashtag].add_video('N/A')
            for j in range(i+1, len(hashtags)):
                hashtag2 = hashtags[j]
                # if hashtag2 == 'fyp' or hashtag2 == 'foryou' or hashtag2 == 'viral' or hashtag2 == 'foryoupage' or hashtag2 == 'fy' or hashtag2 == 'trending':
                #     # print(hashtag)
                #     continue
                if is_ascii(hashtag2):
                    # create node if not already created and add video url
                    if hashtag2 not in user1Nodes:
                        user1Nodes[hashtag2] = HashtagNode(hashtag2)
                    user1Nodes[hashtag2].add_video('N/A')
                    
                    # add the edge for both hashtag and hashtag2
                    user1Nodes[hashtag].add_to(hashtag2)
                    user1Nodes[hashtag2].add_to(hashtag)  

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
            addUserNodes(hashtags)


def format_nodes(nodes):
    formatted_nodes = []

    for key, val in nodes.items():
        style = "None"
        if key in user1Nodes.keys():
            style = "User1"

        node_info = {
            "id": key,  # Assuming the ID is the hashtag itself
            "name": f"#{key}",
            "val": val.get_weight(),  # Assuming 'val' represents the number of edges
            "style": style
        }
        formatted_nodes.append(node_info)

    return formatted_nodes

def get_graph_data():
    G = nx.Graph()

    for key, val in user1Nodes.items():
        for neighbor in val.get_edges():
            G.add_edge(key, neighbor)

    clustering_coefficient = nx.average_clustering(G)

    formatted_nodes = format_nodes(user1Nodes)
    formatted_links = []
    for key, val in user1Nodes.items():
        formatted_links += val.get_user_links()

    graph_data = {"nodes": formatted_nodes, "links": formatted_links, "clustering_coefficient": clustering_coefficient}

    return jsonify(graph_data)

get_graph_data()
