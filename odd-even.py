#WAF to take input from user and find the number is odd or even 
def odd_even(num=None):
    num=int(input("Enter the number"))
    if (num %2==0):
        print("Number is even") 
    else:
        print("Number is odd") 

odd_even()
