from collections import deque


def solution(maps):
    
    n,m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    idx = 1
    pos = (0,0,idx)
    visited[pos[0]][pos[1]] = True
    q.append(pos)
    
    while q:
        x, y, idx = q.popleft()
        
        if x == n-1 and y == m-1:
            return idx
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,idx+1))
    
    return -1