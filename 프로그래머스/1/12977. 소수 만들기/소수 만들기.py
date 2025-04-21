import itertools

def solution(nums):
    answer = 0
    
    combi = list(itertools.combinations(nums, 3))
    
    for i in range(len(combi)):
        check_num = sum(combi[i])
        prime = 0
        for j in range(1, int(check_num ** 0.5) + 1):
            if check_num % j == 0:
                prime += 1
                if j != check_num // j:
                    prime += 1
        if prime == 2:
            answer += 1
        
    return answer