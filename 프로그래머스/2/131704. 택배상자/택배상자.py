def solution(order):
    answer = 0
    stack = []
    order_idx = 0
    
    for box in range(1, len(order)+1):
        if box == order[order_idx]:
            answer += 1
            order_idx += 1
        else:
            stack.append(box)
        
        while stack and stack[-1] == order[order_idx]:
            stack.pop()
            answer += 1
            order_idx += 1

    return answer