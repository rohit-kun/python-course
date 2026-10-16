# write a program thattakes your fav food name as input and prints:
# the middle 3 characters
# the last 2 characters


food = input("Enter fav food: ")
mid = len(food)//2
output1 = food[mid-1:mid+2]
output2 = food[-2:]
print(output1)
print(output2)
