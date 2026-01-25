name_team = input()
name = []
for i in range(3):
    name.append(input())
name.sort()
print(f"{name_team}: {name[0]}, {name[1]}, {name[2]}")