from math import sqrt
from math import pow
from queue import PriorityQueue


class AStarSearch:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heuristic_cost = 0
        self.adjNode = []

    def heuristicCost(self, cost):
        self.heuristic_cost = cost

    def addAdjNode(self, destination, cost):
        temp = [destination, cost]
        self.adjNode.append(temp)


# end of class

def HeuristicCost(x1, y1, x2, y2):
    cost = sqrt(pow((x1-x2), 2)+pow((y1-y2), 2))
    return cost


#  A* search function
def A_star_serach(graph, source, destination):
    parent = {}
    pq = PriorityQueue()
    f = graph[source].heuristic_cost + 0.0
    node = source
    g = 0
    pq.put((f, node, g, source))
    total_cost = 0
    while not pq.empty():
        item = pq.get()
        node = item[1]
        currentCost = item[2]
        p = item[3]
        parent[node] = p
        temp = graph[node]
        if(node is destination):
            total_cost = currentCost
            break
        for neibour in temp.adjNode:

            name = neibour[0]
            cost = neibour[1]

            g = currentCost+cost
            f = graph[name].heuristic_cost  + g
            pq.put((f, name, g, node))

    parent["COST"] = total_cost
    return parent


"Main function"

graph = {}
allNodes = []
n = 0
edge = 0
source_Value = None
destination_Value = None

# read data from user
with open("input.txt", "r") as f:
    n = int(f.readline())
    for i in range(n):
        vertex, x, y = f.readline().split()
        x = int(x)
        y = int(y)
        allNodes.append(vertex)
        graph[vertex] = AStarSearch(x, y)

    edge = int(f.readline())
    for i in range(edge):
        source, destination, c = f.readline().split()
        c = int(c)
        graph[source].addAdjNode(destination, c)
    source_Value = f.readline()
    destination_Value = f.readline()

x2 = graph[destination_Value[0]].x
y2 = graph[destination_Value[0]].y
for i in allNodes:
    x1 = graph[i].x
    y1 = graph[i].y
    graph[i].heuristic_cost  = HeuristicCost(x1, y1, x2, y2)

result = A_star_serach(graph, "S", "G")
path = []
total_cost = result["COST"]

path.append(destination_Value[0])
destination = destination_Value[0]

while(True):
    p = result[destination]
    path.append(p)
    destination = p
    if(source_Value[0] == p):
        break

path.reverse()
print("Path : ", p, end="")
for i in path:
    if i is not p:
        print("-->", i, end="")
print("")
print("cost : ", total_cost)