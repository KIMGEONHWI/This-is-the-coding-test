N = int(input())

List = []

for _ in range(N):
    List.append(int(input()))

List = sorted(List, reverse=True)

for i in List:
    print(i, end=' ')
