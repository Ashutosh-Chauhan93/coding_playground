class Solution:
    
    def dfs(self, node, color):
        print(self.visited_arr, self.color_arr)
        self.visited_arr[node] = 1
        self.color_arr[node] = color
        
        for child in self.graph[node]:
            if self.visited_arr[child] == 0:
                if not self.dfs(child, color ^ 1):
                    return False
            else:
                if self.color_arr[node] == self.color_arr[child]:
                    return False
        
        return True
        
    def isBipartite(self, graph):
        self.graph = graph
        self.visited_arr = [0 for _ in range(len(graph))]
        self.color_arr = [0 for _ in range(len(graph))]
        
        for node in range(len(self.graph)):
            if self.visited_arr[node] == 0: 
                if not self.dfs(node, 0):
                    return False
        return True
            
if __name__ == '__main__':
    s = Solution()
    print(s.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))
