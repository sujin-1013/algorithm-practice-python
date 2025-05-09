import collections

def solution(k, tangerine):
    answer = 0
    
    cnt = collections.Counter(tangerine) 
    
    new_cnt = sorted(cnt.items() , key=lambda x: x[1], reverse=True)
    tangerine_cnt = 0
    
    for idx, t_cnt in new_cnt:
        
        tangerine_cnt += t_cnt
        answer += 1
        
        if k <= tangerine_cnt:
            return answer
    
    return answer