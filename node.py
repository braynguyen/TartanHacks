class HashtagNode:
    def __init__(self, value):
        # string of the hashtag being stored (also id)
        self.value = value

        # to and weights are parralel arrays that we add values to to[i] means Node to Node_i has weight of weights[i]
        self.to = []
        self.weights = []
        # sum of the edgeWeights into this node
        self.edgeWeightIn = 0;

        # videos associated with the hashtag
        self.videos = [];

    # adds videos to the video list associated with this node
    def add_video(self, videolink):
        self.videos.append(videolink)