Given N nodes and E edges of a graph. The task is to do depth first traversal of the graph.

Note: Use recursive approach.

Input:
First line of input contains number of testcases T. For each testcase. First line of each testcase contains number of nodes and edges seperated by space and next line contains N pairs of integers (X and Y each) where X Y means an edge from X to Y.

Output:
For each testcase, print the nodes while doing DFS starting from node 0.

Your task:
The task is to complete the function dfs() which should do the depth first traversal of given graph and prints the node in DFS order.

Constraints:
1 <= T <= 100
1 <= N <= 200

Example:
Input:
2
5 4
0 1 0 2 0 3 2 4
4 3
0 1 1 2 0 3

Output:
0 1 2 4 3    // dfs from node 0
0 1 2 3

import atexit
import io
import sys
from collections import defaultdict
#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        g = Graph(N)
        edges = list(map(int,input().strip().split()))
        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)
        dfs(g.graph,N) # print bfs of graph
        print()
def dfs(g,N):
    visited = [False] * (len(g)) 
    def DFSUtil(g,v, visited):
        visited[v] = True
        print(v, end = ' ') 
        for i in g[v]: 
            if visited[i] == False: 
                DFSUtil(g,i, visited) 
    DFSUtil(g,0, visited)
    
    
    
 Another way of doing it
 
 
 from collections import defaultdict 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
        
    
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def DFSUtil(self, v, visited): 
  
        # Mark the current node as visited  
        # and print it 
        visited[v] = True
        print(v, end = ' ') 
  
        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self, v): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Call the recursive helper function  
        # to print DFS traversal 
        self.DFSUtil(v, visited)


for i in range(int(input())):
    E_V=input().rstrip().split()
    V=input().rstrip().split()
    g=Graph()
    for k in range(0,len(V)-1):
        g.addEdge(int(V[k]),int(V[k+1]))
    g.addEdge(int(V[len(V)-1]),int(V[len(V)-1]))    
    g.DFS(0)






