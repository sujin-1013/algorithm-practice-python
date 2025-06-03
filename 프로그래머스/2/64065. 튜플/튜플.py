def solution(s):
    answer = []
    
    s = s[2:-2].split("},{")
        
    s = sorted(s, key=lambda x: len(x))
        
    answer.append(int(s[0]))
                      
    for i in range(1, len(s)):
        li_s = s[i].split(",")
        for str_s in li_s:
            if int(str_s) not in answer:
                  answer.append(int(str_s))    
        
    return answer