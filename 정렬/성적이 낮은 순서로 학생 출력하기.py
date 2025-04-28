N  = int(input())

List = []

for _ in range(N):
    input_data = input().split()
    List.append((input_data[0], int(input_data[1])))

List = sorted(List, key=lambda list: list[1])

for student in List:
    print(student[0], end= ' ')