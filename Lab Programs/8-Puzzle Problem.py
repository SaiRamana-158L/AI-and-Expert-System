import heapq

goal_state = "123456780"

def manhattan(state):
    dist = 0
    for i, val in enumerate(state):
        if val == '0': continue
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_state.index(val), 3)
        dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

def get_neighbors(state):
    neighbors = []
    zero = state.index('0')
    x, y = divmod(zero, 3)
    moves = [(1,0),(-1,0),(0,1),(0,-1)]

    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_zero = nx*3 + ny
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append("".join(new_state))
    return neighbors

def solve(start):
    pq = [(manhattan(start), 0, start, [])]
    visited = set()

    while pq:
        h, g, state, path = heapq.heappop(pq)
        if state == goal_state:
            return path + [state]

        if state in visited: 
            continue
        visited.add(state)

        for nxt in get_neighbors(state):
            heapq.heappush(pq, (g+1+manhattan(nxt), g+1, nxt, path+[state]))

start = "123405786"
solution = solve(start)

print("\nSolution Steps:")
for s in solution:
    for i in range(0,9,3):
        print(s[i:i+3])
    print()

