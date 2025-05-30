from collections import Counter

def solution(topping):
    answer = 0
    
    n = len(topping)
    
    left = set()
    right = Counter(topping)
    
    for i in range(n-1):
        t = topping[i]
        
        left.add(t)
        
        right[t] -= 1
        if right[t] == 0 :
            del right[t]
                
        if len(left) == len(right):
            answer += 1

    return answer