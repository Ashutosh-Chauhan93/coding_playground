
class DetectCycle:
    def __init__(self, adj_list) -> None:
        self.adj_list = adj_list
        self.visited = [0 for _ in range(len(adj_list))]

    def is_cycle_present(self, node, parent):
        # Note that the node value starts from 1 whereas adj_list,visited are 0-indexed
        # hence whenever we want to access index we will need to do node-1
        node_index = node - 1
        self.visited[node_index]  = 1

        for connected_node in self.adj_list[node_index]:
            connected_node_index = connected_node - 1
            if self.visited[connected_node_index] == 0:
                if self.is_cycle_present(connected_node, node):
                    return True
            else:
                if connected_node != parent:
                    return True
        
        return False


if __name__ == '__main__':
    adj_list = [[2],[1,3,4],[2,4],[3,2,5],[4]]
    d = DetectCycle(adj_list)
    assert d.is_cycle_present(1,-1) is True

    adj_list = [[2],[1,3,4],[2],[2]]
    d = DetectCycle(adj_list)
    assert d.is_cycle_present(1,-1) is False


