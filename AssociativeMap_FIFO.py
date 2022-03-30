#FIFO ASSOCIATIVITY MAPPING

cache_requests=[1,2,8,10,11,8,3,2,6,5,
                16,18,20,21,5,16,8,11,15,
                32,31,26,21,16,8,11,15,25,
                36,22,13,25,15,11,16,18,20
                ,13,25,11,18,25,36,40,41]

'''
cache_requests=[1,2,8,10,11,8,3,2,6,5,
                16,18,20,21,5,16,8,11,15,
                32,31,26,21,16,8,11,15,25,
                36,22,13,25,15,11,16,18,20
                ,13,25,11,18,25,36,40,41,23,34,23,12,45,34,
                34,46,3,4,2,77,5,45,89,76,44,67,95,34,78,90,
                65,43,23,56]
'''
'''
cache_requests=[5, 12, 13, 17, 4,
                12, 13, 17, 2, 13,
                19, 13, 43, 61, 19]
'''
'''
cache_requests=[0, 255, 1, 4, 3,
                8, 133, 159, 216,
                129, 63, 8, 48, 32,
                73, 92, 155]
'''
def cache_Associative_map_FIFO(request_sequence,cache_blocksize=8):
    cache=[]
    #cache_blocksize=8
    cache_hit=0
    i=0
    while len(cache)<cache_blocksize:
            if request_sequence[i]  in cache:
                cache_hit+=1
                pass
            else:
                cache.append(request_sequence[i])
            i+=1
    #print(cache,"\n",cache_requests[i:])
    for j in request_sequence[i:]:
        if j in cache:
            cache_hit+=1
        else:
            cache.pop(0)
            cache.append(j)
        print(cache)
    return cache_hit

print("Cache Hit : ",cache_Associative_map_FIFO(cache_requests,8),"\nCache Hit Ratio : ",cache_Associative_map_FIFO(cache_requests,8)/len(cache_requests))
def directmapping(request_sequence,cache_blocksize=8):
    cache=[0]*cache_blocksize
    cache_hit=0
    i=0
    cache_in=0
    while i<len(request_sequence):
        if request_sequence[i] in cache:
            cache_hit+=1
            pass
        else:
            cache.insert(request_sequence[i]%cache_blocksize,request_sequence[i])
            cache_in+=1
            cache.pop(request_sequence[i]%cache_blocksize+1)
        i+=1
        print(cache)
    print(cache_hit)
    return cache_hit

directmapping(cache_requests,4)
def set_associativemap(request_sequence,setsize,cache_blocksize=8):
    cache=[[0]*(cache_blocksize//setsize) for i in range(setsize)]
    cache_hit=0
    i=0
    print(cache)
    while i<len(request_sequence):
        if request_sequence[i] in cache[request_sequence[i]%setsize]:
            cache_hit+=1
            pass
        else:
            cache[request_sequence[i]%setsize].insert(0,request_sequence[i])
            cache[request_sequence[i]%setsize].pop(-1)
        #if len(cache)*setsize==cache_blocksize:
           # break
        i+=1
        print(cache)
        print(cache_hit)
#set_associativemap(cache_requests,4,16)
