"""
Greedy algorithm is greedy
"""

class NoCapacityException(Exception):
    """
    Exception for when a cache runs out of space
    """

class GreedyEndpoint(object):
    """
    Greedy
    """
    def __init__(self, cache_links):
        self.cache_links = cache_links
        self.video_requests = []

class Cache(object):
    """
    Cache
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.videos = []

    def filled_capacity(self):
        return reduce(
            lambda sum, video: sum + video.size,
            self.videos,
            0
        )

    def remaining_capacity(self):
        return self.capacity - self.filled_capacity()

    def add_video(self, video):
        if video.size > self.remaining_capacity():
            raise NoCapacityException()
        
        if video in self.videos:
            return

        self.videos.append(video)

class Video(object):
    """
    Video
    """
    def __init__(self, size):
        self.size = size

def get_endpoints(input_data):
    videos = [Video(video_size) for video_size in input_data.video_data]
    caches = [Cache(input_data.cache_size) for _ in input_data.num_caches]
    endpoints = [
        GreedyEndpoint(
            [(caches[cache_id], latency) for cache_id, latency in endpoint.cache_links]
        )
        for endpoint in range(input_data.endpoint_data)
    ]

    for request in input_data.requests:
        endpoints[request.endpoint] \
            .video_requests \
            .append((videos[request.video_id], request.num_requests))

    return (videos, caches, endpoints)

def greed_alg(input_data):
    """
    Greedy Alg
    """
    (videos, caches, endpoints) = get_endpoints(input_data)

    

