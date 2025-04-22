from collections import Counter

def solution(X, Y):
    n = Counter(X)
    m = Counter(Y)
    
    result = []

    for i in range(10):
        digit = str(i)
        if digit in n and digit in m:
            result.append(digit * min(n[digit], m[digit]))
    
    if not result:
        return "-1"
    
    answer = ''.join(sorted(result, reverse=True))   
    
    if answer[0] == "0":
        return "0"
    
    return answer