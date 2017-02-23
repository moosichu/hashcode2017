"""
Greedy algorithm is greedy
"""

import copy

class GreedyEndpoint(object):
    """
    Greedy
    """
    def __init__(self, cache_links, video_requests):
        self.cache_links = cache_links
        self.video_requests = video_requests

class Cache(object):
    """
    Cache
    """
    def __init__(self, capacity):
        self.capacity = capacity

class Video(object):
    """
    Video
    """
    def __init__(self, size):
        self.size = size
