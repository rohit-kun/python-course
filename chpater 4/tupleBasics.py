#tuples basics

myTuple = (78, 90, 75)
studentTuple = ("Khushi", "Divya", "Ishaan", "Divya")

print(studentTuple)

print(studentTuple[2])

print(type(studentTuple))

#empty tuples
emptyTuple = ()

print(type(emptyTuple))

#single tuple
singleTuple = (1, )
print(type(singleTuple))

print(studentTuple.index("Divya"))
print(studentTuple.count("Divya"))
print(studentTuple.count("Khushi"))
print(studentTuple.count("Aditya"))