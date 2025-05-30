def solution(n, left, right):
    
    arr = []
    
    for idx in range(left, right+1):
        j = idx % n 
        i = idx // n
        
        arr.append(max(i,j) + 1)
        
    return arr