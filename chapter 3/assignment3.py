# 1. write a program that takes a sentence and prints: total characters in length, uppercase version, lowercase version

msg = input("Enter your message: ")

total_len = len(msg)
upper = msg.upper()
lower = msg.lower()

print(f"Total characters: {total_len} \nUppercase version: {upper} \nLowercase version: {lower}")



# 2. write a program that takes any word or sentence as input and prints: the first character, the last character and the total number of characters

txt = input("Enter the message: ")

fst_char = txt[0]
lst_char = txt[-1]
total_char = len(txt)

print(f"The first character: {fst_char} \nThe last character: {lst_char} \nThe total number of characters: {total_char}")

