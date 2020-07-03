n=int(input("How many integers would you like to enter?\n"))
print("Please enter %d integers." %n)
small=999999999999999     #initialize small with some large numbers.
large=-999999999999999    #initialize large with some lease number.
for i in range (0,n) :   #loop will run to number of integers.
    k=int(input())       #read the integer one by one.
    if k<small:            #if integer is less than small.
        small=k            #stores the integer in small.
    if k>large:            #if integer is more than large.
        large=k            #stores the integer in large.
print("min:", small)       #printing the small value
print("max:", large)       #printing the large value