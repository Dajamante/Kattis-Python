class TarjanSolver:

    def __init__(self, graph):
        self.graph = graph.vertices


        self.id = 0
        self.connected_components = 0

        # initialization of ids
        # -1 stands for unvisited
        self.ids = [-1] * graph.size()

        # low link id, or the lowest id reachable from our node
        self.low_link = [0] * graph.size()

        # on stack and one boolean stack to be able to use Tarjan
        self.stack = []
        self.currently_on_stack = [False] * graph.size()

        print(self.ids)
        print(self.low_link)

    def findStronglyConnectedComponents(self):
        for i in range(len(self.graph)):
            if(self.ids[i] == -1):
                self.dfs(i)
        return self.low_link

    def dfs(self, atNode):
        # push the current node on the stack
        self.stack.append(atNode)
        # and mark it as being on the stack
        self.currently_on_stack[atNode] = True
        self.id += 1
        # increment the id number like a color and increment the low link index
        self.ids[atNode] = self.id
        self.low_link[atNode] = self.id

        #checking the neighbors
        print(list(self.graph)[atNode])
        print("self graph")
        print(self.graph)

        for to in self.graph.get(atNode):
            toNode = self.graph.get(to)
            # if the neighbor has not been visited yet
            if self.ids[to] == -1:
                self.dfs(to)
            # now we are back from the dfs, so if toNode is on stack do the following=assign
            # it the minimum value between the previous or the "parent" and itself.
            if self.currently_on_stack[to]:
                self.low_link[to] = min(self.low_link[to], self.low_link[to])

        # are we at the start of a strongly connected
        if self.ids[atNode]== self.low_link[atNode]:
            for node in self.stack:
                self.currently_on_stack[node] = False
                self.low_link[node] = self.ids[atNode]
                if node == atNode: break
            self.connected_components = self.connected_components + 1


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

    def size(self):
        return len(self.vertices)


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

    tarjan = TarjanSolver(g)
    tarjan_solution = tarjan.findStronglyConnectedComponents()
    print(tarjan_solution.connected_components
)

'''
2
4 0
3 2
1 2
1 3

1
3 2
1 2
1 3
'''
