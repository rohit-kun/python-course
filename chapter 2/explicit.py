# take num as input, convert to float and print both original & converted value with their data types

num = input("Enter a value: ")
convertedvalue = float(num)

print(f"original input value: {num} and data type is: {type(num)}")
print(f"converted value is: {convertedvalue} and data type is: {type(convertedvalue)}")