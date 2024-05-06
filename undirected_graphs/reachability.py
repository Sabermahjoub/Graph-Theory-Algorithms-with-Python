# Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.
# return 1 if there is, else 0

def reach(adj, x, y):

    adj= adj[1:]
    visited = set()
    stack = [x]
    
    while stack:
        current_vertex = stack.pop()
        # print("Stacked element is "+str(current_vertex))
        if current_vertex == y:
            return 1
        for List in adj:
            # print(*List)
            if current_vertex in List:
                # print("The curr vertex is in : "+"List : "+str(List[0])+", "+str(List[1]))
                index = 1 - List.index(current_vertex)
                if List[index] not in visited:
                    # print("Element to be pushed is : "+str(List[index]))
                    stack.append(List[index])
        visited.add(current_vertex)
    return 0

# main function for testing purpose
def main():

    # The first line is a list containing 
    #the number of vertices and the number of edges
    # the other lines contain undirected edges betweens nodes : 
    # for example [1,2] means there's an edge between 1 and 2

   # Test case 1, expected result is : 0
    adj_1 = [
        [4,4],
        [1,2],
        [3,2]
    ]
    result_1 = reach(adj_1,1,4)
    print("Result for test case 1:", result_1)

    # Test case 2, expected result is : 1
    adj_2 = [
        [4,4],
        [1,2],
        [3,2],
        [4,3],
        [1,4]
    ]
    result_2 = reach(adj_2,1,4)
    print("Result for test case 2:", result_2)

if __name__ == "__main__":
    main() 