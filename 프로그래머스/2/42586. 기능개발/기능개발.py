import math 

def solution(progresses, speeds):
    
    result = []
    stack = []
    
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        
        if stack and day <= stack[-1]:
            result[-1] += 1
        else:
            result.append(1)
            stack.append(day)
                
    return result