# Check if string is a palindrome?

n = input("enter string:")
result = str(n) == str(n)[::-1]

print(result)

'''
We're checking if the string representation of n equals the inverted string representation of n
The [::-1] slice takes care of inverting the string
After that, we compare for equality using ==
'''