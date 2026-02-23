
# palindrome checker
# checks text palindrome

text = input("enter: ")
rev = text[::-1]

print("palindrome" if text.lower()==rev.lower() else "not palindrome")