# bill split calculator - take bill amount and number of friends as input and calculate how much each person will pay.

total_bill_amt = float(input("Enter the total bill amoumt: "))
num_friends = int(input("Enter number of friends: "))

each_person_pay_amt = total_bill_amt/num_friends

print(f"Each person will pay: {each_person_pay_amt}")