'''
Created on Feb 18, 2015

@author: Tim
'''
from graphs.basicgraphs import graph
from graphs.graphIO import readgraph, writeDOT, loadgraph
from time import time

#wit #hardloopswag 0

def mergeSort(L):
    if len(L)>1:
        pivot = len(L)//2
        left = L[:pivot]
        right = L[pivot:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                L[k]=left[i]
                i=i+1
            else:
                L[k]=right[j]
                j=j+1
            k=k+1

        while i<len(left):
            L[k]=left[i]
            i=i+1
            k=k+1

        while j<len(right):
            L[k]=right[j]
            j=j+1
            k=k+1

def initcolorize(G):
    G.i = 0
    colormap = {}
    max = -1
    for v in G.V():
        if v.deg() > max:
            max = v.deg()
        v.colornum = v.deg()
        if colormap.get(v.colornum) is None:
            colormap[v.colornum] = [v] 
        else:
            colormap[v.colornum].append(v)
    G.colormap = colormap
    G.i = max    
    buildNeighbours(G)
    #for color in colormap:
    #    vertices = colormap.get(color)
    #    for v in vertices:
    #        for u in vertices:
    #            if not v.neighbourMap == u.neighbourMap:
    #                G.i += 1
    #                v.colornum = i
    #                buildNeighbours(G)
                    
def editcolorMap(G, item):
    my_dict = G.colormap
    temp = my_dict.copy()
    for key, value in my_dict.items():
        if value is not None and item in value: #my_dict.get(entry).get(item) is not None:
            if len(value) > 1: #vertex uit de lijst van value bij deze kleur halen
                value.remove(item)
            else: #hoort niet te gebeuren, omdat bij len(entry.value) == 1 we al blij zijn (dan is er maar 1 kleur waarop deze heen kan)
                del temp[key]
            if temp.get(item.colornum) is None: #als deze kleur nog niet bestaat, deze toevoegen aan de map
                temp[item.colornum] = [item] 
                #temp.update({item.colornum:[item]})
                buildNeighbours(G)
            else:
                temp[item.colornum].append(item) #anders kun je deze gewoon toevoegen aan de kleur
                buildNeighbours(G)
    G.colormap = temp.copy()
                    
def buildNeighbours(G):
    for v in G.V():
        v.neighbourMap = []
        for neigh in v.nbs():
            v.neighbourMap.append(neigh.colornum)
        v.neighbourMap.sort(key=None, reverse=False)
        
def recolorize(G):
    changed = 1
    done = True
    for color in G.colormap:
        if len(G.colormap.get(color)) > 1:
            done = False
            break
    for color in G.colormap:
        vertices = G.colormap.get(color)
        
        if done:
            break
        if len(vertices) == 1:
            continue
        for v in vertices:
            for u in vertices:
                if v.neighbourMap != u.neighbourMap and len(vertices) > 1:
                    G.i += 1
                    v.colornum = G.i
                    editcolorMap(G, v)
                    buildNeighbours(G)
                    changed = 0
                    break
                else:
                    changed += 1
    if changed < 3 and not done:
        recolorize(G)
        
def iRefinement(G, H):
    done = True
    color = -1
    for colorTemp in G.colormap:
        if len(G.colormap.get(colorTemp)) > 1:
            color = colorTemp
            done = False
            break
    if not done:
        gNodesMap = G.colormap.get(color)
        hNodesMap = H.colormap.get(color)
        oldG = G.i
        oldH = H.i
        for i in range(len(G.colormap.get(color))):
            node1 = G.V()[i]
            for j in range(len(H.colormap.get(color))):
                node2 = H.V()[j]
                G.i += 1
                H.i += 1
                
                node1.colornum = G.i
                editcolorMap(G, node1)
                node2.colornum = H.i
                editcolorMap(H, node2)
                print("CHECKEN")
                if isIsomorphViacolor(G, H, refinement=False):
                    return True
                else:
                    G.i = oldG
                    H.i = oldH
                    for g in G.V():
                        if g in gNodesMap:
                            g.colornum = color
                            editcolorMap(G, g)
                    for h in H.V():
                        if h in hNodesMap:
                            h.colornum = color
                            editcolorMap(H, h)
                #print("Is the same:",isIsomorphViacolor(G2, H2))
                #print("isDone:",G2.isDoneWithColoring())
                #if isIsomorphViacolor(G2, H2):
                #    return True
                #if G2.isDoneWithColoring():
                #    break
        
def colorize(G,init=True):
    #initcolorize(G)
    recolorize(G)
    
def isIsomorphViacolor(G, H,refinement=True):
    if (len(G.V()) != len(H.V())) or (len(G.E()) != len(H.E())):# or G.getDegrees() != H.getDegrees():
        print("The degrees, amount of vertices, or the amount of edges differ between these graphs.")
        return False
    colorize(G,init=False)
    colorize(H,init=False)
    print(G.isDoneWithColoring(),"yo")
    if G.isDoneWithColoring():
        return G.isEqualIncolor(H)
    elif refinement:
        iRefinement(G, H)
    else:
        return False
    
    
#G=graph(6)
#for i in range(5):
#    G.addedge(G[i-1], G[i])
#G.addedge(G[4], G[2])
#colorize(G)
#print("colors of G after colorizing:", G.colormap)
#F=graph(4)
#F.addedge(F[0], F[1])
#F.addedge(F[1], F[2])
#F.addedge(F[2], F[3])
#F.addedge(F[3], F[0])
#F.addedge(F[3], F[1])
#H=graph(4)
#H.addedge(H[3], H[2])
#H.addedge(H[2], H[1])
#H.addedge(H[1], H[0])
#H.addedge(H[0], H[3])
#H.addedge(H[1], H[3])
#H.addedge(H[0], H[2])
#print(isIsomorphViacolor(H, F))
#print("F:",F.colormap)
#print("H:",H.colormap)
start = time()
gfs = loadgraph("graphFiles/crefBM_4_9.grl", readlist=True)[0]
G = gfs[0]
H = gfs[1]
F = gfs[2]
K = gfs[3]
initcolorize(G)
initcolorize(H)
initcolorize(F)
initcolorize(K)
print("G - H:", isIsomorphViacolor(G, H))
writeDOT(G, "G")
writeDOT(H, "H")
initcolorize(G)
initcolorize(H)
initcolorize(F)
initcolorize(K)
print("G - F:", isIsomorphViacolor(G, F))
writeDOT(F, "F")
initcolorize(G)
initcolorize(H)
initcolorize(F)
initcolorize(K)
print("G - K:", isIsomorphViacolor(G, K))
writeDOT(K, "K")
initcolorize(G)
initcolorize(H)
initcolorize(F)
initcolorize(K)
print("H - F:", isIsomorphViacolor(H, F))
initcolorize(G)
initcolorize(H)
initcolorize(F)
initcolorize(K)
print("H - K:", isIsomorphViacolor(H, K))
initcolorize(G)
initcolorize(H)
initcolorize(F)
initcolorize(K)
print("F - K:", isIsomorphViacolor(F, K))
end = time()
print(end - start)


          
                
                