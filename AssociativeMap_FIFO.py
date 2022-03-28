#FIFO ASSOCIATIVITY MAPPING

cache_requests=[1,2,8,10,11,8,3,2,6,5,
                16,18,20,21,5,16,8,11,15,
                32,31,26,21,16,8,11,15,25,
                36,22,13,25,15,11,16,18,20
                ,13,25,11,18,25,36,40,41]

'''
cache_requests=[5, 12, 13, 17, 4,
                12, 13, 17, 2, 13,
                19, 13, 43, 61, 19]
'''
def cache_Associative_map_FIFO(request_sequence,cache_blocksize=8):
    cache=[]
    #cache_blocksize=8
    cache_hit=0
    i=0
    while len(cache)<cache_blocksize:
            if cache_requests[i]  in cache:
                cache_hit+=1
                pass
            else:
                cache.append(cache_requests[i])
            i+=1
    print(cache,"\n",cache_requests[i:])
    for j in cache_requests[i:]:
        if j in cache:
            cache_hit+=1
        else:
            cache.pop(0)
            cache.append(j)
        print(cache)
    return cache_hit

print("Cache Hit : ",cache_Associative_map_FIFO(cache_requests,8),"\nCache Hit Ratio : ",cache_Associative_map_FIFO(cache_requests,8)/len(cache_requests))
