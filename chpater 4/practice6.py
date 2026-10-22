# write a pprogram to check grade based on marks (A/B/C/D) using if-elif-else.

marks = int(input("Enter the mark: "))

if(marks >= 70):
    print("Grade is A")
elif( marks >= 50):
    print("Grade is B")
elif( marks >= 30 ):
    print("Grade is C")
else:
    print("D")

