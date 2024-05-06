# Problem Introduction
# You are given a list of currencies 𝑐1, 𝑐2, . . . , 𝑐𝑛 together with a list of exchange
# rates: 𝑟𝑖𝑗 is the number of units of currency 𝑐𝑗 that one gets for one unit of 𝑐𝑖.
# You would like to check whether it is possible to start with one unit
# of some currency, perform a sequence of exchanges, and get more than one
# unit of the same currency. In other words, you would like to find currencies
# 𝑐𝑖1, 𝑐𝑖2, . . . , 𝑐𝑖𝑘 such that 𝑟𝑖1,𝑖2 · 𝑟𝑖2,𝑖3 · 𝑟𝑖𝑘−1,𝑖𝑘, 𝑟𝑖𝑘,𝑖1 > 1. 
#For this, you construct the following graph: vertices are currencies 𝑐1, 𝑐2, . . . , 𝑐𝑛, the weight of
# an edge from 𝑐𝑖 to 𝑐𝑗 is equal to − log 𝑟𝑖𝑗 . There it suffices to check whether is
# a negative cycle in this graph. Indeed, assume that a cycle 𝑐𝑖 → 𝑐𝑗 → 𝑐𝑘 → 𝑐𝑖
# has negative weight. This means that −(log 𝑐𝑖𝑗 + log 𝑐𝑗𝑘 + log 𝑐𝑘𝑖) < 0
# and hence log 𝑐𝑖𝑗 + log 𝑐𝑗𝑘 + log 𝑐𝑘𝑖 > 0. This, in turn, means that
# 𝑟𝑖𝑗.𝑟𝑗𝑘.𝑟𝑘𝑖 = 2^(log 𝑐𝑖𝑗) . 2^(log 𝑐𝑗𝑘) 2^(log 𝑐𝑘𝑖) = 2^(log 𝑐𝑖𝑗 + log 𝑐𝑗𝑘 + log 𝑐𝑘𝑖) > 1 .

def search_cycle (adj, stack, visited, length, initial, x):
    stack.append(x)

    while stack:
        node = stack.pop()
        visited.append(node)
        for List in adj:
            if List[0] == node:
                neighbor = List[1]
                if neighbor == initial:
                    if length+List[2] < 0:
                        return 1
                if neighbor not in visited:
                    length= length + List[2]
                    return search_cycle(adj, stack, visited, length, initial, neighbor)
    return 0



def negative_cycle(adj):
    n= adj[0][0]
    visited= [] *n
    adj= adj[1:]
    for i in range(1,n+1):
        length=0
        if i not in visited:
           stack = []
           if search_cycle (adj, stack, visited , length, i, i ) == 1:
               return 1
    return 0


if __name__ == '__main__':
    # Test case 1, expected result is : 1
    adj_1 = [
        [4,4],
        [1,2,-5],
        [4,1,2],
        [2,3,2],
        [3,1,1]
    ]
    result_1 = negative_cycle(adj_1)
    print("Result for test case 1:", result_1)

    # Test case 2, expected result is : 0
    adj_2 = [
        [4,4],
        [1,2,5],
        [4,1,2],
        [2,3,2],
        [3,1,1]
    ]
    result_2 = negative_cycle(adj_2)
    print("Result for test case 2:", result_2)