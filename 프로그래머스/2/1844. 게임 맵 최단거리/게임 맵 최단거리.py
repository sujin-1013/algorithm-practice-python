from collections import deque

def solution(maps):
    
    start = (0,0)
    n = len(maps)
    m = len(maps[0])
    goal = (n-1, m-1)
    
    visited = [[False for _ in range(m)] for _ in range(n)]   
    dist = [[0 for _ in range(m)] for _ in range(n)]
    
    dr = [-1,+1,0,0]
    dc = [0,0,-1,+1]
    
    visited[0][0] = True
    dist[0][0] = 1
    q = deque([start])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            dx = x + dr[i]
            dy = y + dc[i]
        
            if 0 <= dx < n and 0 <= dy < m:
                if visited[dx][dy] == False and maps[dx][dy] == 1:
                    visited[dx][dy] = True
                    q.append((dx, dy))
                    dist[dx][dy] = dist[x][y] + 1
        
        if (x,y) == goal:
            return dist[x][y]
                
    return -1