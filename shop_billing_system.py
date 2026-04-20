total = 0.0

while True:
    user_input =  input("Enter item price (or 0 to finish): ")
    try:
        item_price = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
  

    if item_price == 0:
        break
    
    total += item_price     

    if item_price < 0:
       print("Input cannot be negative. Try again.")
       continue

    if total > 1000.0:
        discount =total*0.2
    elif total > 500.0 and total <=1000.0:
        discount=total*0.1
    else:
        discount=0.0

    final_total=total - discount

print(f"Total: R{total:.2f}")
print(f"Discount applied: R{discount:.2f}")
print(f"Final Total: R{final_total:.2f}")


