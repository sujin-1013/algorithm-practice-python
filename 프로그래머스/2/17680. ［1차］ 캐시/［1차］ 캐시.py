def solution(cacheSize, cities):
    answer = 0
    
    n = len(cities)

    
    if cacheSize == 0:
        return n*5
    
    cache = []
    time = 0
        
    for i in range(n):
        city = cities[i].lower()
                
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                del cache[0]
                cache.append(city)
            time += 5
        
    return time