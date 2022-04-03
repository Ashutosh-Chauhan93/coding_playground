def dfs(node, adj_list, visited):
    visited[node - 1] = 1
    connected_nodes = adj_list[node - 1]
    for c_node in connected_nodes:
        if not visited[c_node - 1]:
            dfs(c_node, adj_list, visited)

def count_connected_components(adj_list, visited):
    count = 0
    for i in range(len(visited)):
        print(f"visited[{i}] == {visited[i]}")
        if visited[i] == 0:
            dfs(i+1, adj_list, visited)
            count += 1
    return count

def make_adj_list(num_nodes, edges):
    adj_list = [[] for _ in range(num_nodes)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    return adj_list


def dfs_single_source_shortest_path(node, distance, visited, distance_list, adj_list):
    visited[node - 1] = 1
    distance_list[node - 1] = distance

    for c_node in adj_list[node - 1]:
        if visited[c_node - 1] == 0:
            dfs_single_source_shortest_path(c_node, distance+1, visited, distance_list, adj_list)




# these examples are based on nodes starting from 1, so you will find me making a subtraction of 1 in the code
# TODO: Need to use proper graph representations using classes instead of lists
# dfs()
# if __name__ == "__main__":
#     adj_list = [[2],[1,3,4],[2],[2,5,6],[4],[4]]
#     visited = [0,0,0,0,0,0]
#     dfs(1, adj_list, visited)

# count_connected_components()
# if __name__ == "__main__":
#     adj_list = [[5],[5,8],[7],[6],[1,2,6],[5,8,4],[3],[2,6]]
#     visited = [0,0,0,0,0,0,0,0]
#     count = count_connected_components(adj_list, visited)

# if __name__ == "__main__":
#     adj_list = make_adj_list(6, [[1,2],[3,4],[4,5],[5,3]])
#     print(adj_list)

# if __name__ == "__main__":
#     adj_list = [[2],[1,3,4],[2],[2,5,6],[4],[4]]
#     visited = [0,0,0,0,0,0]
#     distance_list = [0,0,0,0,0,0]
#     start_node = 2
#     dfs_single_source_shortest_path(start_node, 0, visited, distance_list, adj_list)
#     print(distance_list)