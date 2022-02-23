b=int(input("Enter a number:"))
input=b
rev=0
while(b>0):
    dig=b%10
    rev=rev*10+dig
    b=b//10
if(input==rev):
    print("The given number is a palindrome!")
else:
    print("The given number is not a palindrome!")