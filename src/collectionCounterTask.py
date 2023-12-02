# https://www.hackerrank.com/challenges/collections-counter
shoesCount = input()
shoesSize = input().split(' ')
customerCount = input()
total = 0
i = 0
while i < int(customerCount):
    size, price = input().split(' ')
    if size in shoesSize:
        shoesSize.remove(size)
        total += int(price)
    i += 1
print(total)
