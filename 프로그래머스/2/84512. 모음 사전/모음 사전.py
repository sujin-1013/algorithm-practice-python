def solution(word):
    answer = 0
    
    dic = ["A", "E", "I", "O", "U"]
    
    weights = []
    for i in range(5):
        weight = sum([5 ** j for j in range(4 - i, -1, -1)])
        weights.append(weight)
            
    for i in range(len(word)):
        idx = dic.index(word[i])
        answer += idx * weights[i] + 1
            
    return answer