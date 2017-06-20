amount = int(input("Enter amount: "))

if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
elif amount < 5000:
    discount = amount * 0.10
    print("Discount", discount)
else:
    discount = amount * 0.15
    print("Discount", discount)

print("Net payable:", amount - discount)
count = 0
while count < 9:
    print('The count is:', count)
    count += 1
print("Good bye!")
count = 0
while count < 5:
    print(count, " is  less than 5")
    count += 1
else:
    print(count, " is not less than 5")
