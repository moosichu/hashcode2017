# definition of input data structures
class InputData:
    def __init__(self):
        self.data_name = ""
        self.num_videos = 0
        self.num_endpoints = 0
        self.num_requests = 0
        self.num_caches = 0
        self.cache_size = 0

        self.video_data = [] # list of video sizes (int)
        self.endpoint_data = [] # list of Endpoints
        self.requests = [] # list of Requests

class Endpoint:
    def __init__(self):
        """
        Contains dictionary indexing cacheids to latency
        """
        self.num_links = 0
        self.cache_links = {} # dictionary from int of cache id to cache latency

class Request:
    def __init__(self, num_requests, video_id, endpoint):
        self.num_requests = num_requests
        self.video_id = video_id
        self.endpoint = endpoint

# definition of output data structures
class OutputData:
    def __init__(self):
        self.num_used_servers = 0
        self.cache_to_video = {} # dictionary from cache ids to CacheData

class CacheData:
    def __init__(self):
        self.videos = [] # list of video ids used (int)

def getData(data_name):
    """
    Returns data in an InputData class
    """
    pass

def setData(data, implementation_name):
    """
    Outputs data to file, give it an OutputData class
    """
    pass
