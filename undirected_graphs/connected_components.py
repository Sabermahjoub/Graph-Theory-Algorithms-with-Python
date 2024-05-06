import sys

def DFS(adj, stack, visited):
    while stack:
        v = stack.pop()
        if v not in visited:
            for List in adj:
                if v in List:
                    index= 1-List.index(v)
                    if List[index] not in visited:
                        stack.append(List[index])
            visited.add(v)        

def number_of_components(adj):
    n = adj[0][0]
    visited = set()
    adj_2 = adj[1:]
    stack= [adj[0][0]]
    result = 0
    for current_index in range(1,n+1):
        testExist=False
        if current_index not in visited:
            for List in adj_2:
                if current_index in List:
                    testExist=True
                    index= 1-List.index(current_index)
                    if List[index] not in visited:
                        stack.append(List[index])
            if testExist == False: 
                result=result+1
            visited.add(current_index)
        if stack :
            DFS(adj_2,stack,visited)
            result=result+1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
