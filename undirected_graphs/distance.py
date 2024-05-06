# This function allows you to calculate the 
# distance between two different nodes of an undirected graph
# when there's no edge between the two nodes, -inf is returned
# else the minimum path length

import queue


def distance(adj, s, t):
    n= adj[0][0]
    ancestor= [None] * n
    distances= [float('-inf')] * n
    distances[s-1] = 0
    adj=adj[1:]
    Q=queue.Queue(maxsize=n)
    Q.put(s)
    while not Q.empty():
        node = Q.get()
        for List in adj:
                if node in List:
                    index= 1-List.index(node)
                    if ancestor[List[index]-1] == None: #not yet discovered
                        ancestor[List[index]-1]= node
                        distances[List[index]-1] = 1+ distances[node-1]
                        Q.put(List[index])
    return distances[t-1]

# main function for testing purpose
def main():

    # The first line is a list containing 
    # the number of vertices and the number of edges
    # the other lines contain undirected edges betweens nodes : 
    # for example [1,2] means there's an edge between 1 and 2

   # Test case 1, the distance between 2 and 4, expected result is : 2
    adj_1 = [
        [4,4],
        [1,2],
        [4,1],
        [2,3],
        [3,1]
    ]
    result_1 = distance(adj_1,2,4)
    print("Result for test case 1:", result_1)

    # Test case 2, the distance between 1 and 5, expected result is : -inf
    adj_2 = [
        [5,4],
        [5,2],
        [1,3],
        [3,4],
        [1,4]
    ]
    result_2 = distance(adj_2,1,5)
    print("Result for test case 1:", result_2)


if __name__ == "__main__":
    main() 
