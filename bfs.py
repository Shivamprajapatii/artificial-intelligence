graph={'A':set(['B','C']),
       'B': set(['A','D','E']),
       'C': set(['A','F',]),
       'D': set(['B']),
       'E': set(['B','F']),
       'F': set(['C','E'])
       }
def bfs(start):
    Q=[start] #queue=Q
    levels = {}
    levels[start]=0
    v=set(start) #v=visited
    while Q:
        node=Q.pop(0)
        ns=graph[node] #neighbours=ns
        for ng in ns:
            if ng not in v: #neighbor=ng
                Q.append(ng)
                v.add(ng)
                levels[ng]=levels[node]+1
    print(levels)
    return v
print(str(bfs('A')))
