from Priority_queue import PriorityQueue
from cyclicity import search_cycle
from dijkstra import dijkstra

def shortest_paths(adj,s):
    n= adj[0][0]
    adj= adj[1:]
    parent=[None]*n
    visited= [] *n
    visited.append(s)
    distances=[float('inf')] * n
    distances[s-1] = 0
    stack=[]
    
    pq = PriorityQueue()
    pq.push(s-1,0)
    visited.append(s)
    for List in adj:
        if List[0] == s:
            neighbor = List[1]
            if neighbor not in visited:
                if search_cycle (adj, stack, visited , 0, neighbor, neighbor ) == 0:
                    visited.remove(neighbor)
                    pq.push(neighbor-1,distances[neighbor-1])

    dijkstra(adj, pq, visited, distances, parent)
    for i in range(1,n+1):
        if i not in visited:
            distances[i-1]='*'
    return distances

if __name__ == '__main__':
    # Test case 1, expected result is : [0, 10, inf, inf, inf, '*']
    adj_1 = [
        [6, 7],
        [1, 2, 10],
        [2,3, 5],
        [1, 3, 100],
        [3, 5, 7],
        [5, 4, 10],
        [4, 3, -18],
        [6, 1, -1]

    ]
    result_1 = shortest_paths(adj_1,1)
    print("Result for test case 1 :", result_1)

    # Test case 2, expected result is : [inf, inf, inf, 0, '*']
    adj_2=[
        [5, 4],
        [1, 2, 1],
        [4, 1, 2],
        [2, 3, 2],
        [3, 1, -5]
    ]
    result_2 = shortest_paths(adj_2,4)
    print("Result for test case 2 :", result_2)