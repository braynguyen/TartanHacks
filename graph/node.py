class HashtagNode:
    def __init__(self, value):
        # string of the hashtag being stored (also id)
        self.value = value

        # node to weights
        self.nodeToWeight = {}

        # sum of the edgeWeights into this node
        self.edgeWeightIn = 0

        # videos associated with the hashtag
        self.videos = []

    def add_to(self, node):
        self.nodeToWeight[node] = self.nodeToWeight.get(node, 0) + 1
        self.edgeWeightIn += 1


    # adds videos to the video list associated with this node
    def add_video(self, videolink):
        self.videos.append(videolink)
        
    def get_value(self):
        return self.value
    
    def get_edges(self):
        return self.nodeToWeight

    def get_weight(self):
        return self.edgeWeightIn / 100

    def get_links(self):
        linklist = []
        for key, weight in self.nodeToWeight.items():
            # if key == 'fyp' or key == 'foryou' or key == 'viral' or key == 'foryoupage' or key == 'fy' or key == 'trending':
            #     continue
            if weight > 20 and len(linklist) <= 5:
                link = {
                    "source": self.value,
                    "target": key,
                    "distance": weight * 1000
                }
                linklist.append(link)
        return linklist
            
