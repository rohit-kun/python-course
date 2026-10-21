# create a tuple of your fav 5 fruits then print the total no. of fruits and the index of one selected fruit

fruit1 = input("Enter the fruit 1: ")
fruit2 = input("Enter the fruit 2: ")
fruit3 = input("Enter the fruit 3: ")
fruit4 = input("Enter the fruit 4: ")
fruit5 = input("Enter the fruit 5: ")

my_Tuple = (fruit1, fruit2, fruit3, fruit4, fruit5)

# my_Tuple.append(fruit1)
# my_Tuple.append(fruit2)
# my_Tuple.append(fruit3)  we cannot do append because tuples are immutable
# my_Tuple.append(fruit4)
# my_Tuple.append(fruit5)

print(f"total number of fruits: {len(my_Tuple)}")

select_fruit = input("Select one fruit: ")

print(f"index of {select_fruit}: {my_Tuple.index(select_fruit)}")