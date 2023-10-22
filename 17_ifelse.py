num = 14
mod = num % 2

if mod == 0:
    print("Even")
    if num > 10:                # nested if
        print("Bigger Number")
    elif num == 10:
        print("Equal Number")
    else:
        print("Smaller Number")
else:
    print("Odd")
