"""
https://en.wikipedia.org/wiki/Topological_sorting

DFS
We loop through each node.
If we can visit a node without hitting a cycle,
we are good
"""
def topological_sort_dfs(numCourses, prerequisites):
    adj_list = [[] for i in range(numCourses)]
    for edge in prerequisites:
        adj_list[edge[0]].append(edge[1])

    permanent = {}
    temp = {}
    did_fail = {'val': False}
    result = []

    def visit(node):
        if did_fail['val']:
            return
        if node in permanent:
            return
        if node in temp:
            did_fail['val'] = True
            return
        temp[node] = True
        for child in adj_list[node]:
            visit(child)
        permanent[node] = True
        result.insert(0, node)

    for i in range(numCourses):
        visit(i)

    return not did_fail['val']

edges = [[1, 0]]
edges = [[0,2],[1,2],[2,0]]
print topological_sort_dfs(3, edges)