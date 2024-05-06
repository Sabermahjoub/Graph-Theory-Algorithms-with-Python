# This function performs DFS from a given vertex 
# return 1 when a cycle was detected
def DFS(adj, vertex, stack, visited):
    while stack:
        v = stack.pop()
        if v not in visited:
            for List in adj:
                if v==List[0]:
                    if List[1] == vertex:
                        return 1
                    elif List[1] not in visited:
                        stack.append(List[1])
            visited.add(v)        


def acyclic(adj):
    visited= set()
    n = adj[0][0]
    adj_2= adj[1:]
    for i in range(1,n+1):
        stack = [i]
        if DFS(adj_2,i,stack,visited) == 1:
            return 1
    return 0

# main function for testing purpose
def main():

    # The first line is a list containing 
    #the number of vertices and the number of edges
    
    # Test case 1, expected result is : 0
    adj_1 = [
        [5,7],
        [1,2],
        [1,3],
        [2,3],
        [3,4],
        [1,4],
        [2,5],
        [3,5]
    ]
    result_1 = acyclic(adj_1)
    print("Result for test case 1:", result_1)

    # Test case 2, expected result is : 1
    adj_2 = [
        [4,4],
        [1,2],
        [4,1],
        [2,3],
        [3,1]
    ]
    result_2 = acyclic(adj_2)
    print("Result for test case 2:", result_2)

if __name__ == "__main__":
    main() 