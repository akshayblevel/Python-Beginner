# execute else part once entire for loop is done

nums = [3, 6, 9, 12, 14, 18]  # No number found
# nums = [3, 6, 9, 12, 15, 18] # 15

for num in nums:
    if num % 5 == 0:
        print(num)
        break

else:
    print("No number found")
