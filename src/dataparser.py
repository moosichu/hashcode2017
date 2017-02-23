import pprint

pp = pprint.PrettyPrinter(indent=4)

# definition of input data structures
class InputData:
    def __init__(self):
        self.data_name = ""
        self.num_videos = 0
        self.num_endpoints = 0
        self.num_request_descriptions = 0
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
        self.latency_to_data_centre = 0
        self.num_links = 0
        self.cache_links = {} # dictionary from int of cache id to cache latency

class Request:
    def __init__(self, num_requests, video_id, endpoint_id):
        self.num_requests = num_requests
        self.video_id = video_id
        self.origin_endpoint_id = endpoint_id

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

    path = "../data/" + data_name + ".in"
    f = open(path, 'r')

    # Set up an InputData object
    data = InputData()
    data.data_name = data_name

    # 1st line is:
    # x videos, y endpoints, z request descriptions, s cache xMB each.
    # 5 videos, 2 endpoints, 4 request descriptions, 3 caches 100MB each.
    line_1 = f.readline()
    # print(line_1)

    line_1_pieces = line_1.split(' ')


    data.num_videos = int(line_1_pieces[0])
    data.num_endpoints = int(line_1_pieces[1])
    data.num_request_descriptions = int(line_1_pieces[2])
    data.num_caches = int(line_1_pieces[3])
    data.cache_size = int(line_1_pieces[4])

    # 2nd line is a whole bunch of video sizes separated by spaces
    line_2 = f.readline()
    # print(line_2)

    data.video_data = map(int, line_2.split(' '))

    # Get the info for each endpoint
    for ep_index in range(0, data.num_endpoints):
        ep = Endpoint()
        endpoint_info = f.readline().split(' ')
        ep.latency_to_data_centre = int(endpoint_info[0])
        num_connected_cache_servers = int(endpoint_info[1])
        for cache_server_index in range(0, num_connected_cache_servers):
            cache_server_connection_info = f.readline().split(' ')
            cache_server_id = cache_server_connection_info[0]
            cache_server_latency = cache_server_connection_info[1]
            # Stor in the dictionary
            ep.cache_links[cache_server_id] = cache_server_latency
        data.endpoint_data.append(ep)

    # Get info about the request descriptions
    for r_index in range(0, data.num_request_descriptions):
        request_info = f.readline().split(' ')

        num_requests = request_info[2]
        video_id = request_info[0]
        origin_endpoint_id = request_info[1]

        r = Request(num_requests, video_id, origin_endpoint_id)
        data.requests.append(r)

    # Uncomment to see structure
    # pp.pprint(vars(data))
    return data


def setData(data, implementation_name):
    """
    Outputs data to file, give it an OutputData class
    """
    pass


getData("kittens")