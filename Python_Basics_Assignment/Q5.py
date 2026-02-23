# bill splitter program
# this calculates how much each person has to pay at a restaurant

try:
    total = float(input("enter total bill: "))
    people = int(input("number of people: "))
    tax = float(input("tax percentage: "))
    tip = float(input("tip percentage: "))

    # calculate tax on the original bill
    tax_amount = total * tax / 100

    # add tax to get bill after tax
    after_tax = total + tax_amount

    # calculate tip on the after tax amount
    tip_amount = after_tax * tip / 100

    # final total = after tax + tip
    grand_total = after_tax + tip_amount

    # split among all people
    per_person = grand_total / people

    print()
    print("=== BILL BREAKDOWN ===")
    print("subtotal:    ₹" + str(round(total, 2)))
    print("tax:         ₹" + str(round(tax_amount, 2)))
    print("after tax:   ₹" + str(round(after_tax, 2)))
    print("tip:         ₹" + str(round(tip_amount, 2)))
    print("total:       ₹" + str(round(grand_total, 2)))
    print("per person:  ₹" + str(round(per_person, 2)))

except ZeroDivisionError:
    print("number of people cant be zero")

except:
    print("invalid input")