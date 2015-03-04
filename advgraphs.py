'''
Created on Feb 6, 2015

@author: Tim
'''
from graphs import basicgraphs as bg
from graphs.basicgraphs import graph

def createPath(n):
    G=bg.graph(n)
    for i in range(1, n):
        G.addedge(G[i-1], G[i])
    return G

def createCycle(n):
    G=bg.graph(n)
    for i in range(1, n):
        G.addedge(G[i-1], G[i])
    G.addedge(G[n-1], G[0])
    return G

def createCompleteGraph(n):
    G=bg.graph(n)
    AList = []
    for i in range(n):
        for j in range(n):
            if j != i and j not in AList:
                G.addedge(G[i], G[j])
            AList.append(i)
    return G

def disjointunion(G, H):
    vmap = {}
    K = bg.graph()
    for v in G.V() + H.V():
        vmap[v] = K.addvertex()
    for e in G.E() + H.E():
        K.addedge(vmap[[e.tail()]], vmap[e.head()])
    return K
        
        
        
        
        
        