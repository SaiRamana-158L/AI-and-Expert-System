def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=" ")
    visited.add(start)
    for nei in graph[start]:
        if nei not in visited:
            dfs(graph, nei, visited)

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
dfs(graph,'A')
