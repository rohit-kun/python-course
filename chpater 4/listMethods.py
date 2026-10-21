# Methods in list

#indexing

marks = [99, 100, 90, 95]

print(marks)
print(marks[1])

marks[1] = 98

print(marks)

#slicing

print(marks[1:3])

print(max(marks))

print(min(marks))
marks.append(92)
print(marks)

marks.sort()
print(marks)
marks.pop(1)
print(marks)
marks.remove(99)
print(marks)

marks.insert(1, 100)
print(marks)