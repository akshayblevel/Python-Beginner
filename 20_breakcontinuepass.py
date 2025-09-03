maxreq = 5

userInput = int(input("Enter number of requests:"))

i = 1
while i <= userInput:
    if i > maxreq:
        break

    print("Request" + str(i))
    i += 1

print("End")

# print value from 1 to 30 except the number divisible by 3 and 5

for x in range(1, 30):
    if x % 3 == 0 and x % 5 == 0:
        continue
        print('after continue')
    
    print(x)

print("End")

# print only in else part and skip if part

for x in range(1, 10):
    if x % 2 == 0:
        pass
        print('after pass')
    else:
        print(x)

print("End")
