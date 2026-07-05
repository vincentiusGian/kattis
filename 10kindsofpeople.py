# Written by vncntgii - 05/07/2026 (DD/MM/YYYY)

# DFS on grid (first time!!)

# decimal = 1, binary = 0

r,c = map(int, input().split())
m = []

for _ in range(r):
    row = [int(ch) for ch in input().strip()]
    m.append(row)

n = int(input())

# use dfs to check connected component!
# check if dfs from (r1,c1) -> (r2,c2) connected

# intialize directions
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def dfs(r, c, grid, visited, curr_id):
    val = grid[r][c]
    st = [(r, c)]
    visited[r][c] = curr_id
    while st:
        cr, cc = st.pop()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if visited[nr][nc] == -1 and grid[nr][nc] == val:
                    visited[nr][nc] = curr_id
                    st.append((nr, nc))

visited = [[-1 for _ in range(c)] for _ in range(r)]
curr_id = 0
for i in range(r):
    for j in range(c):
        if visited[i][j] == -1:
            dfs(i, j, m, visited, curr_id)
            curr_id += 1

for _ in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1

    if m[r1][c1] != m[r2][c2]:
        print("neither")
    elif visited[r1][c1] == visited[r2][c2]:
        print("decimal" if m[r1][c1] == 1 else "binary")
    else:
        print("neither")


# Masih TLE, next update: ubah konsep dfs nya, dari dfs tiap iterasi jadi sekali aja!
# So nanti tinggal check vis[r1][c1] == vis[r2][c2]
