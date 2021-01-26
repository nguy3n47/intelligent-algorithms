import numpy as np
from queue import PriorityQueue
import math
import sys
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

class Graph(object):
    def __init__(self):
        self.N = 0
        self.Matrix = []
        self.SE = []
        with open("input.txt", "rt") as f:
            c = 0
            for line in f:
                if c == 0: self.N = int(line)
                if c == 1: SE=line.split()
                if c > 1 : self.Matrix.append(line.split())
                c+=1
        self.Matrix = np.array(self.Matrix).astype(dtype=int)
        self.SE = np.array(SE).astype(dtype=int)
    
    def drawGrap(self):
        G = nx.DiGraph(directed=True)
        for i in range(0, len(self.Matrix)):
            for j in range(0, len(self.Matrix[0])):
                if self.Matrix[i][j] != 0:
                    G.add_edges_from([(i,j)], weight=self.Matrix[i][j])


        edge_labels=dict([((u,v,),d['weight'])
                         for u,v,d in G.edges(data=True)])
        
        pos=nx.spring_layout(G)
        options = {
                'node_color': 'red',
                'node_size': 500,
                'width': 1.0,
                'arrowstyle': '-|>',
                'arrowsize': 5,
                }
        
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        nx.draw_networkx(G, pos, arrows=True, **options)
        plt.savefig('graph.png', dpi=255)
    
    #----------------------------------------------------------------
    #BFS
    def BFS(self, start, end):
        lens = len(self.Matrix)
        visited = [False]*(lens + 1) 
        path = np.zeros(lens, dtype=int)
        queue = []
        self.helperBFS(start, end, visited, path, queue)
        return path, visited
        
        
        
    def helperBFS(self, start, end, visited, path, queue):
        for i in range(0, len(self.Matrix[0])):
            if(visited[i] == False and self.Matrix[start][i] != 0):
                visited[i] = True
                path[i] = start
                queue.append(i)
        if len(queue) > 0:
            self.helperBFS(queue.pop(0), end, visited, path, queue)
        
    #---------------------------------------------------------------------------
    def print_road(self, array, SE):
        TE = SE.copy()
        road = "";
        fo = TE[1]
        road += str(fo) + '<-'
        while TE[0] != TE[1]:
            if(array[fo] == TE[0]):
                road += str(array[fo])
            else:
                road += str(array[fo]) + '<-'
            fo = array[fo]
            TE[1] = fo
        return road           

    #---------------------------------------------------------------------------
     
def main():
    g = Graph()
    g.drawGrap()
    
    
    if(g.SE[0] == g.SE[1]):
        with open("output.txt", "w") as f:
            f.write("BFS: " + str(g.SE[1]))

    else:
        arrayBFS, visitedBFS = g.BFS(g.SE[0], g.SE[1])
        with open("output.txt", "w") as f:
            if(visitedBFS[g.SE[1]] is False):
                print("Không tìm thấy đường đi")
                f.write("BFS: ")
            else:
                roadBFS = g.print_road(arrayBFS, g.SE)
                f.write("BFS: " + roadBFS)
    
if __name__ == '__main__':
    main()