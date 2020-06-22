class Graph:

    def __init__(self):
        self.vertices = {}
        print(self.vertices)

    def add_double_vertices(self, v, u):
        if v not in self.vertices:
            self.vertices[v] = []
        if u not in self.vertices:
            self.vertices[u] = []
        else:
            pass

    def add_edge(self, v, u):
        self.vertices[v].append(u)
        print(str(u) + " appended to list of " + str(v))


total_cases = int(input())
print(total_cases)

for i in range(total_cases):

    line = input()
    print(line)
    m, n = [int(n) for n in line.strip().split()]
    g = Graph()
    for j in range(n):
        line = input()
        fromNode, toNode = [int(r) for r in line.strip().split(' ')]
        g.add_double_vertices(fromNode, toNode)
        g.add_edge(fromNode, toNode)






