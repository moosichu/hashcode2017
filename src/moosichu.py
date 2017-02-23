from dataparser import *
"""
pseudo-code

> we can look at each cache individually

foreach(endpoint):



"""
data = getData("kittens")

testData = OutputData()
testData.num_used_servers = 3
testData.cache_to_video = {
    0: CacheData(videos=[2]),
    1: CacheData(videos=[3, 1]),
    2: CacheData(videos=[0, 1])
}

setData(testData, "file_identifier")
