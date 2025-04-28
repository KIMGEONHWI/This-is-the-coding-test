n, m = map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 종료조건 1
    if x<0 or x>=n or y<0 or y>=m:
        return False  

    # 성공조건  
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x,y-1) # 좌
        dfs(x,y+1) # 우
        dfs(x-1,y) # 상
        dfs(x+1,y) # 하
        return True
      
    # 종료조건 2
    return False    
    
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1
print(result)