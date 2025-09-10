a = 9
b = 3
print(a ^ b)


lt=[1,2,3,4,5]
print(lt[1:4])
print( 4 not in lt)
print( 4 in lt)
print( 10 in lt)
print( 10 not in lt)
 
x= int(input("Enter a number:"))
if x%2==0:
    print("Even")
else:
    print("Odd")

    x= int(input("Enter a number:"))
    if x%2==0:
        print("Even")
    else:
        print("Odd")
        print("......")

 # write a prorgram to detuct the amount from the account
        balance=1000
        withdraw= int(input("Enter the amount to withdraw:"))
        if withdraw>balance:
            print(" Insufficient balance")
        else:

            balance=balance-withdraw
            print("Withdraw successful. New balance is:",balance)
            print("......")



        #write the program to tell the movie ticket price
        age= int(input("Enter your age:"))
        if age<3:
            print("Free")
        elif age<=12:
            print("Child ticket is $10")
        elif age<65:
            print("Adult ticket is $15")
        else:
            print("Senior citizen ticket is $10")
print("-------------------------------")
# Marks 
marks= int(input("Enter your marks:"))
if marks>=95:
    print("Excellent")
else:
    print("Not Excellent")
