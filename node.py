class HashtagNode:
    def __init__(self, value):
        # string of the hashtag being stored (also id)
        self.value = value

        # node to weights
        self.nodeToWeight = {}

        # sum of the edgeWeights into this node
        self.edgeWeightIn = 0;

        # videos associated with the hashtag
        self.videos = [];

    def add_to(self, node, weight):
        if node in nodeToWeight:
            nodeToWeight[node] += weight
        else:
            nodeToWeight[node] = weight


    # adds videos to the video list associated with this node
    def add_video(self, videolink):
        self.videos.append(videolink)