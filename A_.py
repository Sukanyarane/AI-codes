def head(tuple):
     return tuple[0]
def findlowf(open):
      min=999
      for i in open:
           if f[i]<min and i not in visited:
                min=f[i]
                j=i
      return j
def movgen(a):
    new=[]
    for i in graph:
        if a==i:
          for j in  graph[i]:
               new.append(j)
          break
    return new

def calcost(n,i):
     return cost[(n,i)]
def propimprov(i):
     nexts=movgen(i)
     for j in nexts:
          new=val=g[i]+calcost(i,j)
          if new<g[j]:
               parent[j]=i
               g[j]=new
          if j in closed:
              propimprov(j)

def constpath(n):
     path=[]
     current = n
     while current in parent:
        current = parent[current] 
        path.append(current)
     
     path.remove(0)
     return path[::-1]
               

h={}
f={}
parent={}
g={}
graph={}
visited=[]
print("The Total no of vertices")
cost={}
v=int(input())
for i in range(0,v):
    print("Enter the Vertices")
    c=input()
    graph[c]=[]
    print("Enter its Heuristic value")
    hv=float(input())
    h[c]=hv
    g[c]=0
    f[c]=0
    parent[c]='0'
for i in graph:
    print("Enter total number the vertices connected to {}".format(i))
    v=int(input())
    for j in range(0,v):
        print("Enter vertex")
        c=input()
        graph[i].append(c)
        graph[c].append(i)
        print("Enter cost from {} to {}".format(i,c))
        cst=int(input())
        cost[(i,c)]=cst
        cost[(c,i)]=cst
        visited.append((i,c))
              
print("The Graph is")
print(graph)
print("The Heuristic values are")
print(h)
#for i in graph:
 #    for j in graph[i]:
  #        if (j,i)  not in visited:
   #            print("Enter cost from {} to {}".format(i,j))
    #           c=int(input())
     #          cost[(i,j)]=c
      #         cost[(j,i)]=c
       #        visited.append((i,j))
print("The Cost values are")
print(cost)
print("Enter the start")
start=input()
f[start]=h[start]
parent[start]=0
print("Enter goal state")
goal=input()
open=[]
closed=[]
visited=[]
open.append(start)
ct=0
while open:
    print("")
    print("The Open state is ")
    for i in open:
         print("({},{},{},{},{})".format(i,parent[i],h[i],g[i],f[i]))
    print("\nThe Closed list is ")
    for i in closed:
         print("({},{},{},{},{})".format(i,parent[i],h[i],g[i],f[i]))
    n=findlowf(open)
    print("\nThe Selected node is {}".format(n))
    open.remove(n)
    visited.append(n)
    if n== goal:
         print("Solution Found")
         print("The path is ")
         path=constpath(n)
         path.append(n)
         print(path)
         ct=1
         break
    nextstate=movgen(n)
    for state in nextstate:
         if state in visited :
              nextstate.remove(state)
    for i in nextstate:
          if i not in open and i not in closed:
               parent[i]=n
               g[i]=g[n]+calcost(n,i)
               f[i]=g[i]+h[i]
          elif i in open:
               if (g[i]+ cost[(n,i)]) < g[n]:
                    parent[i]=n
                    g[i]=g[n]+calcost(n,i)
                    f[i]=g[i]+h[i]
          elif i in closed:
               if (g[i]+calcost(n,i)) < g[n]:
                    parent[i]=n
                    g[i]=g[n]+calcost(n,i)
                    f[i]=g[i]+h[i]
                    propimprov(i)
    for i in nextstate:
          if i not in open:
               open.append(i)
    closed.append(n)
if ct!=1:
     print("No Solution found")
