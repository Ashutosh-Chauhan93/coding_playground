class DetectCycleDirected:
    def __init__(self, adj_list) -> None:
        self.adj_list = adj_list
        self.visited = [0 for _ in range(len(self.adj_list))]
    
    def is_cycle_directed(self, node):
        # 0 means node is not visited
        # 1 means node is visited, but dfs cycle is in progress 
        node_index = node - 1
        self.visited[node_index] = 1

        for connected_node in self.adj_list[node_index]:
            connected_node_index = connected_node - 1
            if self.visited[connected_node_index] == 0:
                if self.is_cycle_directed(connected_node) is True:
                    return True
            else:
                # its a cycle if node is visited but dfs cycle is still in progress
                if self.visited[connected_node_index] == 1:
                    return True

        # 2 means node is visited as well as dfs cycle is complete    
        self.visited[node_index] = 2
        return False

    
if __name__ == '__main__':
    adj_list = [[2], [3], [4], [2,5], [4]]
    d = DetectCycleDirected(adj_list)
    assert d.is_cycle_directed(1) is True







