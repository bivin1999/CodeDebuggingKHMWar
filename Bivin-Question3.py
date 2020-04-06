from math import gcd
t=int(input())
for _ in range(t):
    n=int(input())#no to n
    adj=[list() for x in range(n)]#ad to adj and added ()
    for i in range(n-1):
        u,v=map(int,input().strip().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    v=list(map(int,input().strip().split()))#str to int
    m=list(map(int,input().strip().split()))#str to int
    factors=[0]*n
    leaves=[]
    parent=[1]*n
    queue=[0]
    for i in queue:
        children=set(adj[i])-set([parent[i]])
        if(parent[i]==-1):
            factors[i]=v[i]
        else:
            factors[i]=gcd(factors[parent[i]],v[i])#added ]
        if(len(children)<=0):
            leaves.append(i)#leaves
        for q in children:
            parent[q]=i
            queue.append(q)
    sorted(leaves)
    re=[m[i]-gcd(m[i],factors[i]) for i in leaves]
    print(*re)#removed *