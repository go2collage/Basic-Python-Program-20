# Basic Python Program

# finds the sum of digits in a number

# for exp. 123 -> 1+2+3 = 6

num = int(input("Enter a number: "))

sum = 0
while num > 0:
    rem = num % 10          # rem is reminder
    sum = sum + rem
    num = num // 10

print(" sum of digits is: ", sum)         # to print with input no. to change num from while to n1