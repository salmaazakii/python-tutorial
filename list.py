numbers = [3,10, 5, 8, 2, 1, 4, 7, 6, 9]
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)


N = int(input())
i = 0
arr = []
temp = []
result = []
while i < N:
    cmd = input()
    if cmd.find("append") > -1:
        arr.append(int(cmd.split(" ")[1]))
    elif cmd.find("insert") > -1:
        arr.insert(int(cmd.split(" ")[1]),int(cmd.split(" ")[2]))
    elif cmd.lower() == "print":
        temp = arr.copy()
        result.append(temp)
    elif cmd.find("remove") > -1:
        arr.remove(int(cmd.split(" ")[1]))
    elif cmd.lower() == "sort":
        arr.sort()
    elif cmd.lower() == "pop":
        arr.pop()
    elif cmd.lower() == "reverse":
        arr.reverse()
    i+=1
for j in result:
    print(j)