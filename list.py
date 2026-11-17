numbers=[90,2,3,45,60,69]
numbers.append(78)
numbers.insert(2,30)
print(numbers)
numbers.append([1,1])
print(numbers)
numbers.extend([1,1])
print(numbers)
numbers.remove([1,1])
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers.remove(1)
print(numbers)
numbers.pop(1)
print(numbers)
numbers.index(3)
print(numbers.index(3))
numbers.append(1)
print(numbers.count(1))
numbers = [10, 20, 30, 20, 40, 10]
print(dict.fromkeys(numbers))
numbers=[87,87,68,56,56,43]
print(list(set(numbers)))
unique=[]
num=[90,90,89,78,67]
for n in num:
    if n not in unique:
        unique.append(n)
print(unique)
