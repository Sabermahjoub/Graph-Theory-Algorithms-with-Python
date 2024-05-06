# This is a useful data structure for implementing 
# a counter that counts the time.
class DFSTimeCounter:
    def __init__(self):
        self.count = 0
    
    def reset(self):
        self.count = 0
    
    def increment(self):
        self.count = self.count + 1
        
    def get(self):
        return self.count 
    
class UndirectedGraph:
    
    # n : number of vertices
    # we will label the vertices from 0 to self.n -1 
    # We will store the outgoing edges for each node using a set data structure initialized to empty adjacency list
    def __init__(self, n):
        self.n = n
        self.adj_list = [ set() for i in range(self.n) ]
        
    def add_edge(self, i, j):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j and from j to i since we're dealing with undirected graphs
        self.adj_list[i].add(j)
        self.adj_list[j].add(i)
        
    # get all vertices that 
    # are neighbors of the
    # vertex i
    def get_neighboring_vertices(self, i):
        assert 0 <= i < self.n
        return self.adj_list[i]
    
    # The DFS visit of a graph.
    # We use a list to store discovery times and finish times.
    # Arguments :
    #  i --> id of the vertex being visited.
    #  dfs_timer --> An instance of DFSTimeCounter structure provided.
    #  discovery --> discovery time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be visited.
    #  finish --> finish time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be finished.
    #  dfs_tree_parent --> the parent for for each node 
    #                       if we visited node j from node i, then j's parent is i.
    #  dfs_back_edges --> a list of back edges.
    #                     (a back edge is an edge from i to j wherein
    #                     DFS has already discovered j when i is discovered 
    #                                     but not finished j)
    
    def dfs_visit(self, i, dfs_timer, discovery_times, finish_times, 
                        dfs_tree_parent, dfs_back_edges):
        assert 0 <= i < self.n
        assert discovery_times[i] == None
        assert finish_times[i] == None
        discovery_times[i] = dfs_timer.get()
        dfs_timer.increment()
        neighbors = self.get_neighboring_vertices(i)
        for neighbor in neighbors :
            if discovery_times[neighbor] != None and finish_times[neighbor] == None:
                dfs_back_edges.append([i,neighbor])
            if discovery_times[neighbor] == None:
                if dfs_tree_parent[neighbor] == None:
                    dfs_tree_parent[neighbor] = i
                self.dfs_visit(neighbor,dfs_timer, discovery_times, finish_times, 
                               dfs_tree_parent, dfs_back_edges)

        finish_times[i]=dfs_timer.get()
        dfs_timer.increment()
        
    
    # Traverse the entire graph.
    def dfs_traverse_graph(self):
        dfs_timer = DFSTimeCounter()
        discovery_times = [None]*self.n
        finish_times = [None]*self.n
        dfs_tree_parents = [None]*self.n
        dfs_back_edges = []
        for i in range(self.n):
            if discovery_times[i] == None:
                self.dfs_visit(i,dfs_timer, discovery_times, finish_times, 
                               dfs_tree_parents, dfs_back_edges)
        # Modify the back edges so that if (i,j) is a back edge then j cannot
        # be i's parent.
        non_trivial_back_edges = [(i,j) for (i,j) in dfs_back_edges if dfs_tree_parents[i] != j]
        return (dfs_tree_parents, non_trivial_back_edges, discovery_times, finish_times)

#This a function used to perform DFS using a stack, just for the purpose of 
#calculating the total number of connected components
def dfs(stack,visited,i,adj):
    while stack :
        v = stack.pop()
        visited.add(v)
        for neighbor in adj[v]:
            if neighbor not in visited:
                stack.append(neighbor)
def num_connected_components(g): # g is an UndirectedGraph class
    number=0
    adj = g.adj_list
    visited= set()
    stack=[]
    for i in range(g.n) : 
        if adj[i] == None:
            number=number+1
        elif i not in visited:
            stack=[i]
            dfs(stack,visited,i,adj)
            number=number+1
    print(str(number))
    return number
                
# Function that returns a set of all nodes that form a cycle, 
#using the non-trivial back edges.
def find_all_nodes_in_cycle(g): 
    set_of_nodes = set()
    result= g.dfs_traverse_graph()
    back_edges = result[1]
    for back_edge in back_edges :
        i = back_edge[0]
        j= back_edge[1]
        set_of_nodes.add(i)
        set_of_nodes.add(i)
        for neighbor in g.adj_list[i]:
            if neighbor not in set_of_nodes:
                set_of_nodes.add(neighbor)
    #sorting the set
    sorted_list = sorted(set_of_nodes)
    set_of_nodes = set(sorted_list)
    return set_of_nodes


#Testing

g = UndirectedGraph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)

assert num_connected_components(g) == 1, f' Test A failed: g must have 1 connected component. Your code returns {num_connected_components(g)}'
