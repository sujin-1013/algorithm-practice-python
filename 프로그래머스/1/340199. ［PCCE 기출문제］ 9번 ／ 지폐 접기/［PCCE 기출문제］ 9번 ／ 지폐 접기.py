def solution(wallet, bill):
    answer = 0
    w, h = bill

    while not (
        (w <= wallet[0] and h <= wallet[1]) or
        (h <= wallet[0] and w <= wallet[1])
    ):
        if w >= h:
            w = w // 2
        else:
            h = h // 2
        answer += 1

    return answer
