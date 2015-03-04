'''
Created on Feb 18, 2015

@author: Tim
'''
from graphs.basicgraphs import graph

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

def initColourize(G):
    G.i = 0
    colourmap = {}
    max = -1
    for v in G.V():
        if v.deg() > max:
            max = v.deg()
        v.colournum = v.deg()
        if colourmap.get(v.colournum) is None:
            colourmap[v.colournum] = [v] 
        else:
            colourmap[v.colournum].append(v)
    G.colourmap = colourmap
    G.i = max    
    buildNeighbours(G)
    #for colour in colourmap:
    #    vertices = colourmap.get(colour)
    #    for v in vertices:
    #        for u in vertices:
    #            if not v.neighbourMap == u.neighbourMap:
    #                G.i += 1
    #                v.colournum = i
    #                buildNeighbours(G)
                    
def editcolourMap(G, item):
    my_dict = G.colourmap
    temp = my_dict.copy()
    for key, value in my_dict.items():
        if value is not None and item in value: #my_dict.get(entry).get(item) is not None:
            if len(value) > 1: #vertex uit de lijst van value bij deze kleur halen
                value.remove(item)
            else: #hoort niet te gebeuren, omdat bij len(entry.value) == 1 we al blij zijn (dan is er maar 1 kleur waarop deze heen kan)
                del temp[key]
            if temp.get(item.colournum) is None: #als deze kleur nog niet bestaat, deze toevoegen aan de map
                temp[item.colournum] = [item] 
                #temp.update({item.colournum:[item]})
                buildNeighbours(G)
            else:
                temp[item.colournum].append(item) #anders kun je deze gewoon toevoegen aan de kleur
                buildNeighbours(G)
    G.colourmap = temp.copy()
                    
def buildNeighbours(G):
    for v in G.V():
        v.neighbourMap = []
        for neigh in v.nbs():
            v.neighbourMap.append(neigh.colournum)
        v.neighbourMap.sort(key=None, reverse=False)
        
def reColourize(G):
    changed = 1
    done = True
    for colour in G.colourmap:
        if len(G.colourmap.get(colour)) > 1:
            done = False
            break
    for colour in G.colourmap:
        vertices = G.colourmap.get(colour)
        
        if done:
            break
        if len(vertices) == 1:
            continue
        for v in vertices:
            for u in vertices:
                if v != u and v.neighbourMap != u.neighbourMap and len(vertices) > 1:
                    G.i += 1
                    print("Changing vertex",v,"with colour",v.colournum,"to colour ",G.i,". Length of the colour: ",len(vertices), "(",vertices,")")
                    v.colournum = G.i
                    editcolourMap(G, v)
                    buildNeighbours(G)
                    changed = 0
                    break
                else:
                    changed += 1
    if changed < 2 and not done:
        reColourize(G)
    
def colourize(G):
    initColourize(G)
    reColourize(G)
    
def isIsomorphViaColour(G, H):
    if (len(G.V()) != len(H.V())) or (len(G.E()) != len(H.E())) or G.getDegrees() != H.getDegrees():
        print("The degrees, amount of vertices, or the amount of edges differ between these graphs.")
        return False
    colourize(G)
    colourize(H)
    return G.isEqualInColour(H)
    
    
G=graph(6)
for i in range(5):
    G.addedge(G[i-1], G[i])
G.addedge(G[4], G[2])
colourize(G)
print("Colours of G after colourizing:", G.colourmap)
F=graph(4)
F.addedge(F[0], F[1])
F.addedge(F[1], F[2])
F.addedge(F[2], F[3])
F.addedge(F[3], F[0])
F.addedge(F[3], F[1])
H=graph(4)
H.addedge(H[3], H[2])
H.addedge(H[2], H[1])
H.addedge(H[1], H[0])
H.addedge(H[0], H[3])
H.addedge(H[1], H[3])
H.addedge(H[0], H[2])
print(isIsomorphViaColour(H, F))
print("F:",F.colourmap)
print("H:",H.colourmap)

          
                
                