# movie ticket pricing system

age = int(input("Enter age: "))
day = input("Enter day (Mon-Sun): ").strip().lower()
tickets = int(input("Enter number of tickets: "))

# set ticket price based on age group
if age < 3:
    base_price = 0        # toddlers are free
elif age <= 12:
    base_price = 150      # child price
elif age <= 59:
    base_price = 300      # adult price
else:
    base_price = 200      # senior price

# weekend days get 20% off, weekdays have no discount
if day in ["fri", "sat", "sun", "friday", "saturday", "sunday"]:
    discount_percent = 20
else:
    discount_percent = 0

discount_amount = base_price * (discount_percent / 100)
price_after_discount = base_price - discount_amount
total_amount = price_after_discount * tickets

print("\n--- Ticket Summary ---")
print(f"Base price per ticket: ₹{base_price}")
print(f"Discount: {discount_percent}%")
print(f"Price after discount per ticket: ₹{price_after_discount:.2f}")
print(f"Number of tickets: {tickets}")
print(f"Total amount: ₹{total_amount:.2f}")