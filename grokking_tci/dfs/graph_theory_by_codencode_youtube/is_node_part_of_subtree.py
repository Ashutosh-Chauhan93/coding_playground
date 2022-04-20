from sklearn.metrics import adjusted_mutual_info_score


class CheckNodeIsPresentInSubTree:
    timer = 1
    def __init__(self, adj_list) -> None:
        self.adj_list = adj_list
        self.visited_list = [0 for _ in range(len(adj_list))]
        self.in_time_list = [0 for _ in range(len(adj_list))]
        self.out_time_list = [0 for _ in range(len(adj_list))]

    def dfs_with_in_out_time(self, node):
        print(node)
        node_index = node - 1
        self.visited_list[node_index] = 1
        self.in_time_list[node_index] = self.timer
        self.timer += 1

        for child in self.adj_list[node_index]:
            child_index = child - 1
            if self.visited_list[child_index] == 0:
                self.dfs_with_in_out_time(child)
        
        self.out_time_list[node_index] = self.timer
        self.timer += 1

    def is_node_present_in_subtree_of_node(self, parent_node, child_node):
        print(self.in_time_list)
        print(self.out_time_list)
        if self.in_time_list[parent_node - 1] < self.in_time_list[child_node - 1]:
            if self.out_time_list[parent_node - 1] > self.out_time_list[child_node - 1]:
                return True
        return False


if __name__ == '__main__':
    adj_list = [[2],[3,4],[2],[2,5],[4]]
    checknodeinsubtree = CheckNodeIsPresentInSubTree(adj_list)
    checknodeinsubtree.dfs_with_in_out_time(1)
    assert checknodeinsubtree.is_node_present_in_subtree_of_node(1,2) is True








        