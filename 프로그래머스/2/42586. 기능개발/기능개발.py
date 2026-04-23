import math

def solution(progresses, speeds):
    answer = []
    
    n = len(progresses)
    days = []
    
    for i in range(n):
        day = math.ceil((100 - progresses[i])/speeds[i])
        days.append(day)
        
    finish = 1
    today = days[0]
    
    for i in range(1, len(days)):

        if days[i] > today:
            answer.append(finish)
            today = days[i]
            finish = 1
        else:
            finish += 1

    answer.append(finish)
        
    return answer