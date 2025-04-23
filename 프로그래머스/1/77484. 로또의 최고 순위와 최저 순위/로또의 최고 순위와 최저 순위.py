def solution(lottos, win_nums):
    
    # 1등 0개 불일치
    # 2 1개
    # 3 2개
    # 4 3개
    # 5 4개
    # 6 5개 6개
    
    count_zero = 0
    not_match = 0
    
    for lotto in lottos:
        if lotto not in win_nums:
            not_match += 1
        if lotto == 0:
            count_zero += 1
    
    best = 1 + (not_match - count_zero)
    worst = 1 + not_match
    if best > 6:
        best = 6
    if worst > 6:
        worst = 6
    
    return [best, worst]