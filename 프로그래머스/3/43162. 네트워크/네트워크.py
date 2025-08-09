from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False] * n 
    q = deque()
    
    q.append(0)
    
    for start in range(n):
        if not visited[start]:
            q = deque()
            q.append(start)
            visited[start] = True 
            answer += 1
    
        while q:
            idx = q.popleft()

            for i in range(n):
                if computers[idx][i] == 1 and not visited[i]:
                    visited[i] = True
                    q.append(i)
    
    return answer