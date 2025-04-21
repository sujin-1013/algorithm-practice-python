def solution(s):
    answer = 0
    
    check_s = s[0]
    cnt_same = 0
    cnt_diff = 0
    
    for i in range(len(s)):
        
        if check_s == s[i]:
            cnt_same += 1
        else:
            cnt_diff += 1
        
        if cnt_same == cnt_diff:
            if i+1 < len(s):
                check_s = s[i+1]
            cnt_same = 0
            cnt_diff = 0
            answer += 1
        else:
            if i+1 == len(s):
                answer += 1
        
        # print(s[i], s[:i+1], cnt_same, cnt_diff,answer)
        
    return answer