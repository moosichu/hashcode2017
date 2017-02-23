"""
Greedy algorithm is greedy
"""
from dataparser import OutputData, CacheData
from functools import reduce

import collections
from collections import deque

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
    def __init__(self, capacity, cache_id):
        self.capacity = capacity
        self.videos = []
        self.cache_id = cache_id

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
    def __init__(self, size, video_id):
        self.size = size
        self.video_id = video_id

def get_endpoints(input_data):
    videos = [Video(video_size, video_id) for video_id, video_size in enumerate(input_data.video_data)]
    caches = [Cache(input_data.cache_size, cache_id) for cache_id in range(input_data.num_caches)]

    def greedy_endpoint_from_data_endpoint(endpoint):
        return GreedyEndpoint(
            [(caches[int(cache_id)], latency) for cache_id, latency in endpoint.cache_links.items()]
        )

    endpoints = [greedy_endpoint_from_data_endpoint(endpoint) for endpoint in input_data.endpoint_data]

    for request in input_data.requests:
        endpoints[int(request.origin_endpoint_id)] \
            .video_requests \
            .append((videos[int(request.video_id)], request.num_requests))

    for endpoint in endpoints:
        endpoint.cache_links.sort(key=lambda cache_link: cache_link[1])
        endpoint.video_requests.sort(
            key=lambda video_requests: video_requests[1],
            reverse=True
        )

    return (caches, endpoints)

def fill_caches_from_endpoints(endpoints):
    q_endpoints = deque(endpoints)
    while len(q_endpoints) > 0:
        endpoint = q_endpoints.popleft()
        if len(endpoint.video_requests) == 0: continue
        video = endpoint.video_requests.pop(0)[0]
        for cache_link in endpoint.cache_links:
            cache = cache_link[0]
            if cache.remaining_capacity() >= video.size:
                cache.add_video(video)
                q_endpoints.append(endpoint)
                break

def caches_to_output_data(caches):
    output_data = OutputData()

    for cache in caches:
        if len(cache.videos) > 0:
            output_data.num_used_servers += 1
            output_data.cache_to_video[str(cache.cache_id)] = CacheData(
                [video.video_id for video in cache.videos]
            )

    return output_data


def greed_alg(input_data):
    """
    Greedy Alg
    """
    (caches, endpoints) = get_endpoints(input_data)
    fill_caches_from_endpoints(endpoints)
    return caches_to_output_data(caches)

    