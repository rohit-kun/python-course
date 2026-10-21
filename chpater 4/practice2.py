# write a program that takes names of 3 fav foods from the user and stores then in list then print the list and its length

food1 = input("Enter food 1: ")
food2 = input("Enter food 2: ")
food3 = input("Enter food 3: ")

my_list = []

my_list.append(food1)
my_list.append(food2)
my_list.append(food3)

print(f"my_list: {my_list} \nlength of the list: {len(my_list)}")