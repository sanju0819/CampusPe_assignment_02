# sum, average, max and min calculator
# user enters how many numbers

n = int(input("How many numbers? "))

nums = []
for i in range(n):
    value = float(input(f"Enter number {i+1}: "))
    nums.append(value)

total = sum(nums)
average = total / n
maximum = max(nums)
minimum = min(nums)

print(f"\nSum: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")