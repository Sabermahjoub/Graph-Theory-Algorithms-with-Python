# To compute the strongly connected components of a given graph, we follow this algorithm : 
# 1- We perform a DFS on the original graph, we create a list A to :
# 2- book-keep all the finished times of each vertex in a descending order
# 3- We perform a second DFS on the reverse graph (transpose) for each element of the list A
    

# the first and second step of the algorithm
def dfs(stack,adj, visited, finish_times, x,timer):
    stack.append(x)
    test=False
    while stack:
        v=stack.pop()
        visited.append(v)
        timer+=1
        for List in adj:
            if List[0]==v and List[1] not in visited:
                test=True
                timer=1+dfs(stack,adj,visited,finish_times,List[1],timer)
        if not test:
            timer+=1
        finish_times[v-1] = timer
    return timer
        
# the second step of the algorithm
def getOrderedVertices(finish_times):
    n = len(finish_times)
    order = []
    treated = [False] * n  # To keep track of treated vertices
    for _ in range(n):
        max_val = float('-inf')  # Initialize max_val to negative infinity
        max_index = -1
        for i in range(n):
            if not treated[i] and finish_times[i] > max_val:
                max_val = finish_times[i]
                max_index = i
        order.append(max_index + 1)  # Append the vertex with the maximum finish time
        treated[max_index] = True  # Mark the vertex as treated
    return order

# The third step of the algorithm
def dfs_reverse(stack,adj, visited, x,result):
    stack.append(x)
    while stack:
        test=False
        v=stack.pop()
        visited.append(v)
        #print("while Pooping "+ str(v) + " result is "+ str(result))
        for List in adj:
            if List[0]==v and List[1] not in visited:
                #print ("discovered : "+str(List[1])+ " from : "+ str(v))
                test=True
                result=dfs_reverse(stack,adj,visited,List[1],result)
        if not test:
            result=result+1
            #print("updating for v : "+str(v) + " result is :"+ str(result))
    return result


# used for the third step of the algorithm
def reverse_graph(adj):
    adjR = [] * len(adj)
    for list in adj:
        adjR.append(list[::-1])
    return adjR


# The algorithm 
def number_of_strongly_connected_components(adj):
    n= adj[0][0]
    adj=adj[1:]
    timer=0
    result = 0
    stack=[]
    visited=[]* n
    finish_times= [0] * n

    for i in range(1,n+1):
        if i not in visited:
            timer=dfs(stack,adj,visited, finish_times,i, timer)
    order=getOrderedVertices(finish_times)
    reverse = reverse_graph(adj)

    stack= []
    visited=[]
    for i in order:
        if i not in visited:
            result=dfs_reverse(stack, reverse, visited, i, result)
    return result

# main function for testing purpose
def main():

    # Test case 1, expected result : 2
    adj_1 = [
        [4,4],
        [1,2],
        [4,1],
        [2,3],
        [3,1]
    ]
    print("Number of strongly connected components of test case 1 is : "+ str(number_of_strongly_connected_components(adj_1)))

    # Test case 2, expected result : 5
    adj_2 = [
        [5,7],
        [2,1],
        [3,2],
        [3,1],
        [4,3],
        [4,1],
        [5,2],
        [5,3]
    ]
    print("Number of strongly connected components of test case 2 is : "+ str(number_of_strongly_connected_components(adj_2)))


    # Test case 3, expected result : 5
    adj_3 = [
        [7,6],
        [1,2],
        [2,5],
        [5,1],
        [6,5],
        [3,4],
        [7,4]
    ]
    print("Number of strongly connected components of test case 3 is : "+ str(number_of_strongly_connected_components(adj_3)))

if __name__ == "__main__":
    main() 
