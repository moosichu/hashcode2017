class Data:
    def __init__(self):
        self.num_videos = 0
        self.num_endpoints = 0
        self.num_requests = 0
        self.num_caches = 0
        self.cache_size = 0

        self.video_data = []
        self.endpoint_data = [] # list of Endpoints
        self.requests = []

class Endpoint:
    def __init__(self):
        """
        Contains dictionary indexing cacheids to latency
        """
        self.num_links = 0
        self.cache_links = {}

class Reqjest:
    def __init__(self, num_requests, video_id, endpoint):
        self.num_requests = num_requests
        self.video_id = video_id
        self.endpoint = endpoint

def getData(arg):
    pass
