# This function allows you to determine whether an undirected graph is bipartite or not .
# An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the
# graph joins to vertices from different parts. Bipartite graphs arise naturally in applications where a graph
# is used to model connections between objects of two different types (say, boys and girls; or students and
# dormitories).
# An alternative definition is the following: a graph is bipartite if its vertices can be colored with two colors
# (say, black and white) such that the endpoints of each edge have different colors

import queue


def bipartite(adj):
    n= adj[0][0]
    group_1 = []
    group_2 = []
    adj=adj[1:]
    Q=queue.Queue(maxsize=n)
    for i in range(1,n+1):
        if i not in group_1 and i not in group_2: 
            Q.put(i)
            group_1.append(i)
            while not Q.empty():
                node = Q.get()
                for List in adj:
                        if node in List:
                            index= 1-List.index(node)
                            if List[index] in group_1 or List[index] in group_2:
                                if node in group_1:
                                    if List[index] in group_1:
                                        return 0
                                elif node in group_2:
                                    if List[index] in group_2:
                                        return 0
                            else: #not yet discovered
                                if node in group_1:
                                    group_2.append(List[index])
                                else:
                                    group_1.append(List[index])
                                Q.put(List[index])
    return 1

# main function for testing purpose
def main():

    # The first line is a list containing 
    # the number of vertices and the number of edges
    # the other lines contain undirected edges betweens nodes : 
    # for example [1,2] means there's an edge between 1 and 2

   # Test case 1, expected result is : 0
    adj_1 = [
        [4,4],
        [1,2],
        [4,1],
        [2,3],
        [3,1]
    ]
    result_1 = bipartite(adj_1)
    print("Result for test case 1:", result_1)

    # Test case 2, expected result is : 1
    adj_2 = [
        [5,4],
        [5,2],
        [4,2],
        [3,4],
        [1,4]
    ]
    result_2 = bipartite(adj_2)
    print("Result for test case 2:", result_2)

    # Test case 3, expected result is : 1
    adj_3 = [
        [7,10],
        [1,3],
        [2,4],
        [2,5],
        [2,1],
        [4,7], 
        [4,8],
        [5,3],
        [5,7],
        [6,8],
        [6,7]
    ]
    result_3 = bipartite(adj_3)
    print("Result for test case 3:", result_3)

if __name__ == "__main__":
    main() 
