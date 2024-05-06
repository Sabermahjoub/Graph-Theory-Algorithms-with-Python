def dfs(stack,adj, used, order, x):
    stack.append(x)
    while stack:
        v=stack.pop()
        used.append(v)
        for List in adj:
            if List[0]==v and List[1] not in used:
                dfs(stack,adj,used,order,List[1])
        order.append(v)

def toposort(adj):
    n,m = adj[0]
    adj=adj[1:]
    used = [0] * len(adj)
    order = []
    stack=[]
    for elt in adj:
        if elt[0] not in used:
            dfs(stack,adj,used,order,elt[0])
    for i in range(1,n+1):
        if i not in used:
            order.append(i)
    order.reverse()
    return order

# main function for testing purpose
def main():

    # Test case 1, expected result is : 3 4 1 2 or 4 3 1 2
    adj_1 = [
        [4,3],
        [1,2],
        [4,1],
        [3,1]
    ]
    print("Test case 1 :")
    order_1 = toposort(adj_1)
    for x in order_1:
        print(x, end=' ')
    print()

    #Test case 2, expected result 2 4 3 1 or 2 3 1 4 or 4 2 3 1
    adj_2 = [
        [4,1],
        [3,1]
    ]
    print("Test case 2 :")
    order_2 = toposort(adj_2)
    for x in order_2:
        print(x, end=' ')  
    print()

    # Test case 3, expected result : 5 4 3 2 1 
    adj_3 = [
        [5,7],
        [2,1],
        [3,2],
        [3,1],
        [4,3],
        [4,1],
        [5,2],
        [5,3]
    ]
    print("Test case 3 :")
    order_3 = toposort(adj_3)
    for x in order_3:
        print(x, end=' ')

if __name__ == "__main__":
    main() 