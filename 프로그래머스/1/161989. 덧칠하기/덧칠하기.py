def solution(n, m, section):
    answer = 0
    
    k = len(section)
    i = 0
    
    while i < k:
        start_roller = section[i]
        answer += 1
        
        while i < k and section[i] < start_roller + m:
            i += 1
                
    return answer