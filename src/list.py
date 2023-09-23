# numbers = [3,10, 5, 8, 2, 1, 4, 7, 6, 9]
# max_num = numbers[0]
# for number in numbers:
#     if number > max_num:
#         max_num = number
# print(max_num)
#
#
# N = int(input())
# i = 0
# arr = []
# temp = []
# result = []
# while i < N:
#     cmd = input()
#     if cmd.find("append") > -1:
#         arr.append(int(cmd.split(" ")[1]))
#     elif cmd.find("insert") > -1:
#         arr.insert(int(cmd.split(" ")[1]),int(cmd.split(" ")[2]))
#     elif cmd.lower() == "print":
#         temp = arr.copy()
#         result.append(temp)
#     elif cmd.find("remove") > -1:
#         arr.remove(int(cmd.split(" ")[1]))
#     elif cmd.lower() == "sort":
#         arr.sort()
#     elif cmd.lower() == "pop":
#         arr.pop()
#     elif cmd.lower() == "reverse":
#         arr.reverse()
#     i+=1
# for j in result:
#     print(j)

# records = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     records.append([name, score])
# scores = []
# for i in records:
#     if i[1] not in scores:
#         scores.append(i[1])
# scores.sort()
# second_score = scores[1]
# result = []
# for j in records:
#     if j[1] == second_score:
#         result.append(j[0])
# result.sort()
# for k in result:
#     print(k)

# List Comprehensions
originalList = range(1, 11)
print("Original (Starting) list of numbers (1 to 10)")
for x in originalList:
    print(x)
print("Displaying the Cubes of 1..10 using the standard for-loop notation")
for i in range(1, 11):
    print(i ** 3)
print("Displaying the cubes by using List Comprehensions")
cubesUsingListComprehensions = [x ** 3 for x in originalList]
print(cubesUsingListComprehensions)
