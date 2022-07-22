from math import sqrt
from math import pow
from queue import PriorityQueue

#saving node information
class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hcost = 0         # h(n) this is for hurestic cost/value
        self.adjNode = []      # for neighbour node
    def h(self,cost):
        self.hcost = cost      # saving hurestic cost/value
    def addAdjNode(self,d,cost):
        temp = [d,cost]        # adding child node
        self.adjNode.append(temp)
    def printAll(self):        # this is for debug purpose
        print(self.x,self.y)
        print(self.hcost)
        print(self.adjNode)


# finding Heuristic cost for each node
def HeuristiCost(x1,x2,y1,y2):
    cost = sqrt(pow((x1-x2),2)+pow((y1-y2),2))  # Finding euclidean distance
    return cost


# Function for A* search
def A_star_serach(graph,s,d):
    parent = {}                       # for saving parent to find the path using backtrack
    pq = PriorityQueue()              # built-in priorityqueue auto min heap
    f = graph[s].hcost + 0.0 #f(n)
    node = s
    g = 0
    pq.put((f,node,g,s))       # inserting in pq in this order f(n),node,g(n),parent
    total_cost = 0
    while not pq.empty():
        item = pq.get()       # taking top  value and pop the value from the pq
        node = item[1]        # node name
        currentCost = item[2] #g(n)
        p = item[3]           # parent of current node
        parent[node] = p      # saving clid parent relation
        temp = graph[node]    # taking all information  of current node
        if(node is d):        # if we find the destination then take break form the operation
            total_cost = currentCost
            break            # base condition
        for nebour in temp.adjNode:   # taking the all child node of current node
            name = nebour[0]          # all child details save like lis [["name",cost], .... .]
            cost = nebour[1]
            g = currentCost+cost      # update the path cost of current child node ,, source to child path cost
            f = graph[name].hcost + g #f(n) = h(n)+g(n)
            pq.put((f,name,g,node))   # puting neighbour node information in the PQ
    parent["COST"] = total_cost   # for return purpose we save the total cost in the parent then we only return the parent
    return  parent                # in parent value has all information  like cost and path



"This is main Function-----------------"
graph = {}         # creating a dictionary for saving the graph
allNode = []       # creating a list for saving all node this is mainly for h() finding
n = 0              # for total number of node
edge = 0           # for total number of edge
source = None
destination = None

#read data from file
with open("input.txt","r") as f:
    n = int(f.readline())       # reading 1st line the make it int becouse this is number of node
    #print(n)
    for i in range(n):
        v,x,y = f.readline().split()  # node_name ,  x, y
        x = int(x)           # making x int type
        y = int(y)           # making y like x
        allNode.append(v)    # adding node name in allNode
        graph[v] = Node(x,y) # creating a new node int graph dictionary

    edge = int(f.readline()) # reading number of edge
    for i in range(edge):
        s,d,c = f.readline().split() # Source, Destination , Cost
        c = int(c)               # making cost as int
        graph[s].addAdjNode(d,c)  # adding node in source
    source = f.readline()  #taking source as list
    destination = f.readline()     # taking destination s list
# print(s)
#print(destination)


#adding Hurestic Value
x2 = graph[destination[0]].x
y2 = graph[destination[0]].y
for i in allNode:
    x1 = graph[i].x
    y1 = graph[i].y
    graph[i].hcost = HeuristiCost(x1,x2,y1,y2)


# #printing all information for debug purpose
result = A_star_serach(graph,"S","G")   # calling a* search function
path = []    # for saving actual path
total_cost = result["COST"]
path.append(destination[0]) # from destination we backtrack the source then we find the actual path
d = destination[0]
#print(result)
while(True):
    p = result[d]
    path.append(p)
    d = p
    if(source[0]==p):
        break

path.reverse()  # after backtracking we reverse the path list then we find the actual path
print("Solution path :",p,end="")
for i in path:
    if i is not p: print(" -->", i, end="")
print("")
print("Solution cost :",total_cost)






#[graph[i].printAll() for i in allNode]