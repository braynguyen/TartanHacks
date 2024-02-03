class Graph:
    def __init__(self):
        self.nodes = []
        self.weights = {}

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)
        return node

    def add_edge(self, node1, node2, weight):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_edge(node2, weight)