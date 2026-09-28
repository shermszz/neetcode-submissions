class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
            a --> b --> c: This also means a and c are indirectly connected
            GOAL: Find all the distinct provinces

            We are given an adjacency matrix
            City 0 : [0, 1]
            City 1 : [1, 0]
            City 2 : [2]
            Here City 0 and 1 are connected, but City 2 is not. 

            This is an undirected graph problem
            Idea:
                - We can create an adjacnecy list out of this adjancey matrix first
                - Then, once we have the adj_list, we need a visited list to track the cities that we have visited
                - For every city, if not yet visited, we will visit it and add the province count by 1.
                - Then, within that city, we are going to do a dfs all the way until we visit all its direct and indirect neighbours
        """

        adj_list = defaultdict(list)
        n = len(isConnected)

        # Building the adjancency list first
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
        
        # print(adj_list)
        
        visited = [False for _ in range(n)] # Because we have n cities
        provinces = 0 

        def dfs(city: int) -> None:
            if visited[city]:
                return
            visited[city] = True
            for neighbour in adj_list[city]:
                dfs(neighbour)
                
        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
        return provinces  




                    