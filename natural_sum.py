#Write a recursive function to calculate the sum of first n natural numbers.

def natural_sum(n):
    if(n==0):
        return 0
    return natural_sum(n-1)+n

sum=natural_sum(4)
print(sum)
