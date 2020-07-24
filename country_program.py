#dijkstras algorithm
def dijk(src):
    d=[999]*n
    d1=[999]*n
    d[src]=0
    d1[src]=0
    vis=[False]*n
    for k in range(n):
        m=999
        m1=999
        for v in range(n):
            if vis[v]==False:
                if d[v]<m:
                    m=d[v]
                    m1=d1[v]
                    minindex=v
                elif d[v]==m and d1[v]<m1:
                    m=d[v]
                    m1=d1[v]
                    minindex=v
        u=minindex
        vis[u]=True
        for v in range(n):
            if l[u][v]>0 and vis[v]==False and (d[v]>d[u]+l[u][v] or (d[v]==d[u]+l[u][v] and d1[v]<d1[u]+l1[u][v])):
                d[v]=d[u]+l[u][v]
                d1[v]=d1[u]+l1[u][v]
    return [d,d1]
def mapping_index(src):
    if src=='A':
        src=0
    elif src=='B':
        src=1
    elif src=='C':
        src=2
    elif src=='D':
        src=3
    return src
n=4
l=[[0 for i in range(4)] for j in range(4)]
l1=[[0 for i in range(4)] for j in range(4)]
print("Enter number of edges:")
t=int(input())
countries=['A','B','C','D']
while(t>0):
    t=t-1
    print("Enter the source country (A or B or C or D)")
    src=input()
    print("Enter the destination country (A or B or C or D)")
    des=input()
    if src not in countries or des not in countries:
        print("Enter valid countries")
        t=t+1
    elif src==des:
        print("No self loops")
    else:
        print("Enter the cost:")
        cost=int(input())
        print("Enter the distance")
        dis=int(input())
        src=mapping_index(src)
        des=mapping_index(des)
        l[src][des]=cost
        l1[src][des]=dis
while(1):
    print("Enter the source city:")
    src=input()
    print("Enter the destination city:")
    des=input()
    if src not in countries or des not in countries:
        print("Enter valid countries:")
        continue
    else:
        src=mapping_index(src)
        des=mapping_index(des)
        mm=dijk(src)
        mincs=mm[0]
        minds=mm[1]
        print("Minimum cost and dis is:",mincs[des],minds[des])
        break
'''
INPUT:
5
A
B
50
100
B
C
100
50
A
C
75
150
C
D
50
100
A
D
150
150
A
D
'''
