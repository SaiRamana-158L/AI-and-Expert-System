from collections import deque

def is_valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m==0 or m>=c)

def bfs():
    start = (3,3,1)   # M, C, boat on left
    goal = (0,0,0)
    q = deque([(start, [])])
    visited = set()

    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    while q:
        state, path = q.popleft()
        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path+[state]

        m, c, boat = state

        for dm, dc in moves:
            if boat == 1:  
                new = (m-dm, c-dc, 0)
            else:          
                new = (m+dm, c+dc, 1)

            m2, c2, _ = new
            m1, c1 = 3-m2, 3-c2

            if is_valid(m2,c2) and is_valid(m1,c1):
                q.append((new, path+[state]))

solution = bfs()
print("\nSolution Steps:")
for s in solution:
    print(s)
