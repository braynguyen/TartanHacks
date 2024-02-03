from community import community_louvain
import networkx as nx

# returns Louvain best partition;
# dict mapping Node.value to cluster for all nodes in G
# clusters are numbered
def get_clusters(nodes):
    G = nx.Graph()

    for key, val in nodes.items():
        for neighbor, weight in val.get_edges().items():
            # print(neighbor, weight)

            # reminder: val.get_edges() returns a dictionary of string, int pairs
            G.add_edge(key, neighbor, weight=weight)

    # clustering_coefficient = nx.average_clustering(G)
    # compute the best partition
    clusters = community_louvain.best_partition(G)
    # print(clusters)

    return clusters