def solution(n,a,b):
    idx = 0     
    
    while True:
        a = (a+1)//2
        b = (b+1)//2

        idx += 1
        
        if a == b:
            break

    return idx