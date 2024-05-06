from Priority_queue import PriorityQueue

def dijkstra (adj, pq, visited, distances, parent):
    while not pq.is_empty():
        node = pq.pop()
        node+=1
        visited.append(node)
        for List in adj:
            if List[0] == node:
                neighbor = List[1]
                if neighbor not in visited:
                    if distances[neighbor-1] > distances[node-1] + List[2]:
                        distances[neighbor-1] = distances[node-1] + List[2]
                        parent[neighbor-1] = node
                        pq.remove(neighbor-1)
                        pq.push(neighbor-1, distances[neighbor-1])

def dijkstra_call (adj, s, t) : 
    n = adj[0][0]
    adj=adj[1:]
    visited = [] * n
    parent = [None] * n
    distances= [float('inf')] * n
    distances[s-1] = 0

    #Initiliazing the priority queue
    pq = PriorityQueue()
    for i in range(n):
        pq.push(i,distances[i])

    dijkstra(adj, pq, visited, distances, parent)

    return distances[t-1]

def main():

    # The first line is a list containing 
    # the number of vertices and the number of edges
    # the other lines contain directed edges betweens nodes as well as the corresponding weight : 
    # for example [1,2,3] means there's an edge from 1 to 2 with a weight of 3

    # Test case 1, the minimum total weight of a path from 1 to 3
    # expected result is : 3
    adj_1 = [
        [4,4],
        [1,2,1],
        [4,1,2],
        [2,3,2],
        [1,3,5],
    ]
    result_1 = dijkstra_call(adj_1,1,3)
    print("Result for test case 1:", result_1)

    # Test case 2, the minimum total weight of a path from 1 to 5
    # expected result is : 6
    adj_2 = [
        [5, 9],
        [1, 2, 4],
        [1, 3, 2],
        [2, 3, 2],
        [3, 2, 1],
        [2, 4, 2],
        [3, 5, 4],
        [5, 4, 1],
        [2, 5, 3],
        [3, 4, 4]
    ]
    result_2 = dijkstra_call(adj_2,1,5)
    print("Result for test case 2:", result_2)

    # Test case 3, the minimum total weight of a path from 3 to 2
    # expected result is : inf (because there is no path from 3 to 2)
    adj_3 = [
        [3, 3],
        [1, 2, 7],
        [1, 3, 5],
        [2, 3, 2],
    ]
    result_3 = dijkstra_call(adj_3,3,2)
    print("Result for test case 3:", result_3)


if __name__ == "__main__":
    main() 