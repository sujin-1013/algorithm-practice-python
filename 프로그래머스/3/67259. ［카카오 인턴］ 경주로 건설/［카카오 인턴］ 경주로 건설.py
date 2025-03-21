from collections import deque

def solution(board):
    n = len(board)
    visited = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs():
        queue = deque()
        for i in range(4):
            visited[0][0][i] = 0
            queue.append((0, 0, i, 0))  # x, y, 방향, 비용

        while queue:
            x, y, direction, cost = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    new_cost = cost + (100 if direction == i else 600)

                    if visited[nx][ny][i] > new_cost:
                        visited[nx][ny][i] = new_cost
                        queue.append((nx, ny, i, new_cost))

    bfs()
    return min(visited[n-1][n-1])
