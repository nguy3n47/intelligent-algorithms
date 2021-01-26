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
        self.MatrixCoor = []
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
        
        pos=nx.spring_layout(G, scale= 10)
        options = {
                'node_color': 'red',
                'node_size': 500,
                'width': 1.0,
                'arrowstyle': '-|>',
                'arrowsize': 2,
                }
        
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        nx.draw_networkx(G, pos = pos, arrows=True, **options)
        plt.savefig('graph.png', dpi=255)
    
    
  
    # get Coordinates of matrix
    def getCoordinates(self):
        G = nx.DiGraph(directed=True)
        for i in range(0, len(self.Matrix)):
            for j in range(0, len(self.Matrix[0])):
                if self.Matrix[i][j] != 0:
                    G.add_edges_from([(i,j)], weight=self.Matrix[i][j])
        
        pos=nx.spring_layout(G)
        return pos
    
    #euclidean distance
    def euclideanDistance(self, coordinates1, coordinates2):
        return math.sqrt(math.pow(coordinates2[0] - coordinates1[0], 2) 
                + math.pow(coordinates2[1] - coordinates1[1], 2))
    
    #A*
    def A_Star1(self, start, end):
        lens = len(self.Matrix)
        visited = [False]*(lens + 1)
        pq = []
        pos = self.getCoordinates();
        for i in range(0, len(self.Matrix[0])):
            if(self.Matrix[start][i] != 0):
                visited[i] = True
                distance = self.euclideanDistance(pos[start], pos[i])
                pq.append([self.Matrix[start][i] + distance, str(start) + str(i), self.Matrix[start][i]])
    
        pq.sort()
        while len(pq) > 0 and int(pq[0][1][-1]) != end:
            temp = pq.pop(0)
            for i in range(0, len(self.Matrix[0])):
                if(self.Matrix[int(temp[1][-1])][i] != 0):
                    visited[i] = True
                    t = temp.copy()
                    distance = self.euclideanDistance(pos[int(t[1][-1])], pos[i])
                    t[2] = t[2] + self.Matrix[int(temp[1][-1])][i]
                    t[0] = t[2] + distance
                    t[1] = t[1] + str(i)
                    pq.append(t)
            pq.sort()
            
        if len(pq) == 0:
            return -1
        return pq.pop(0)
    
    
     #A*
    def A_Star2(self, start, end):
        lens = len(self.Matrix)
        visited = [False]*(lens + 1)
        pq = []
        for i in range(0, len(self.Matrix[0])):
            if(self.Matrix[start][i] != 0):
                visited[i] = True
                distance = 0;
                for j in range(0, len(self.Matrix[0])):
                     if(self.Matrix[i][j] != 0):
                         distance += self.Matrix[i][j]
                
                pq.append([self.Matrix[start][i] + distance, str(start) + str(i), self.Matrix[start][i]])
    
        pq.sort()
        
        while len(pq) > 0 and int(pq[0][1][-1]) != end:
            temp = pq.pop(0)
            for i in range(0, len(self.Matrix[0])):
                if(self.Matrix[int(temp[1][-1])][i] != 0):
                    visited[i] = True
                    t = temp.copy()
                    distance = 0;
                    for j in range(0, len(self.Matrix[0])):
                        if(self.Matrix[i][j] != 0):
                            distance += self.Matrix[i][j]
                            
                    t[2] = t[2] + self.Matrix[int(temp[1][-1])][i]
                    t[0] = t[2] + distance
                    t[1] = t[1] + str(i)
                    pq.append(t)
            pq.sort()
            
        if len(pq) == 0:
            return -1
        return pq.pop(0)
     
     
     
def main():
    g = Graph()                
    with open("A_Start1.txt", "w") as f:
        arr = g.A_Star1(g.SE[0], g.SE[1])
        if(arr == -1):
            f.write("Weight: ")
            f.write("\n")
            f.write("Path: ")
        else:
            f.write("Weight: " + str(arr[2]))
            f.write("\n")
            f.write("Path: ")
            for i in range(0, len(arr[1])):
                if(i == len(arr[1]) - 1):
                    f.write(arr[1][i])
                else:
                    f.write(arr[1][i] + '->')


    with open("A_Start2.txt", "w") as f:
        arr = g.A_Star2(g.SE[0], g.SE[1])
        if(arr == -1):
            f.write("Weight: ")
            f.write("\n")
            f.write("Path: ")
        else:
            f.write("Weight: " + str(arr[2]))
            f.write("\n")
            f.write("Path: ")
            for i in range(0, len(arr[1])):
                if(i == len(arr[1]) - 1):
                    f.write(arr[1][i])
                else:
                    f.write(arr[1][i] + '->')
if __name__ == '__main__':
    main()
