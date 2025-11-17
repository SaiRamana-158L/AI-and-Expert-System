from collections import deque

def water_jug(a, b, target):
    visited = set()
    q = deque([ (0,0) ])

    while q:
        x, y = q.popleft()

        if (x,y) in visited:
            continue
        visited.add((x,y))

        print(x, y)

        if x == target or y == target:
            print("Solved!")
            return

        # possible operations
        states = [
            (a, y),  # fill a
            (x, b),  # fill b
            (0, y),  # empty a
            (x, 0),  # empty b
            (x - min(x, b-y), y + min(x, b-y)),  # a→b
            (x + min(y, a-x), y - min(y, a-x))   # b→a
        ]

        for s in states:
            if s not in visited:
                q.append(s)

water_jug(4,3,2)
