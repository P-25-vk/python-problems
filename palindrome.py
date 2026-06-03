string=input("Enter a String to Reverse:")
temp=string
reverse=""
for char in string:
    reverse=char+reverse
if(temp==reverse):
    print("Palindrome!")
else:
    print("Not a palindrome!")
    
