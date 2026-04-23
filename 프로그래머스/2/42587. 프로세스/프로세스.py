def solution(priorities, location):
    
    queue_list = [ (priorities[i], i) for i in range(len(priorities))]
    cnt = 0
    
    while queue_list:
        
        cur = queue_list.pop(0)
        
        if any(cur[0] < q[0] for q in queue_list):
            queue_list.append(cur)
        else:
            cnt += 1
            if cur[1] == location:
                return cnt
    
    return cnt