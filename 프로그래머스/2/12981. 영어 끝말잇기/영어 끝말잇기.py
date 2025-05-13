def solution(n, words):
    
    m = len(words)
    person_idx = 0
    turn_idx = 1

    for i in range(m):
        
        person_idx += 1
            
        if i >= 1:
            if words[i-1][-1] != words[i][0]:
                return person_idx, turn_idx
        
        if words[i] in words[:i]:
            return person_idx, turn_idx
        

        if person_idx == n:
            person_idx = 0
            turn_idx += 1

    return 0,0