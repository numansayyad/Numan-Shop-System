

print("🛍️ Welcome to Numan Shop 🏪")

print("""
1. Electronics
2. Grocery
3. Clothing
4. Stationery
5. Exit
""")

choice = int(input("Enter your choice: "))
price = 0  # initialize price variable

if choice == 1:
    print("""
    ⚡ Electronics Section ⚡
    1. TV 
    2. Laptop
    3. Headphones
    4. Mobile
    5. Smart Watch
    6. Exit
    """)

    choice1 = int(input("Enter your choice: "))

    if choice1 == 1:
        price = 50000
        print(f"You have selected a TV! Price is Rs {price}.")
    elif choice1 == 2:
        price = 80000
        print(f"You have selected a Laptop! Price is Rs {price}.")
    elif choice1 == 3:
        price = 2500
        print(f"You have selected Headphones! Price is Rs {price}.")
    elif choice1 == 4:
        price = 15000
        print(f"You have selected a Mobile! Price is Rs {price}.")
    elif choice1 == 5:
        price = 5000
        print(f"You have selected a Smart Watch! Price is Rs {price}.")
    elif choice1 == 6:
        print("Thank you for visiting the Electronics section!")
    else:
        print("Invalid choice!")

elif choice == 2:
    print("""
    🛒 Grocery Section 🛒
    1. Sugar
    2. Rice
    3. Oil
    4. Tea Powder
    5. Salt
    6. Exit
    """)
    choice2 = int(input("Enter your choice: "))

    if choice2 == 1:
        price = 40
        print(f"You have selected Sugar! Price is Rs {price} per kg.")
    elif choice2 == 2:
        price = 80
        print(f"You have selected Rice! Price is Rs {price} per kg.")
    elif choice2 == 3:
        price = 160
        print(f"You have selected Oil! Price is Rs {price} per liter.")
    elif choice2 == 4:
        price = 120
        print(f"You have selected Tea Powder! Price is Rs {price} per pack.")
    elif choice2 == 5:
        price = 25
        print(f"You have selected Salt! Price is Rs {price} per pack.")
    elif choice2 == 6:
        print("Thank you for visiting the Grocery section!")
    else:
        print("Invalid choice!")

elif choice == 3:
    print("""
    👕 Clothing Section 👗
    1. T-Shirt
    2. Jeans
    3. Jacket
    4. Saree
    5. Shoes
    6. Exit
    """)
    choice3 = int(input("Enter your choice: "))

    if choice3 == 1:
        price = 700
        print(f"You have selected a T-Shirt! Price is Rs {price}.")
    elif choice3 == 2:
        price = 1500
        print(f"You have selected Jeans! Price is Rs {price}.")
    elif choice3 == 3:
        price = 2500
        print(f"You have selected a Jacket! Price is Rs {price}.")
    elif choice3 == 4:
        price = 2000
        print(f"You have selected a Saree! Price is Rs {price}.")
    elif choice3 == 5:
        price = 1200
        print(f"You have selected Shoes! Price is Rs {price}.")
    elif choice3 == 6:
        print("Thank you for visiting the Clothing section!")
    else:
        print("Invalid choice!")

elif choice == 4:
    print("""
    📚 Stationery Section ✏️
    1. Notebook
    2. Pen
    3. Pencil Box
    4. School Bag
    5. Water Bottle
    6. Exit
    """)
    choice4 = int(input("Enter your choice: "))

    if choice4 == 1:
        price = 50
        print(f"You have selected a Notebook! Price is Rs {price}.")
    elif choice4 == 2:
        price = 20
        print(f"You have selected a Pen! Price is Rs {price}.")
    elif choice4 == 3:
        price = 150
        print(f"You have selected a Pencil Box! Price is Rs {price}.")
    elif choice4 == 4:
        price = 600
        print(f"You have selected a School Bag! Price is Rs {price}.")
    elif choice4 == 5:
        price = 200
        print(f"You have selected a Water Bottle! Price is Rs {price}.")
    elif choice4 == 6:
        print("Thank you for visiting the Stationery section!")
    else:
        print("Invalid choice!")

# ---------------- EXIT ----------------
elif choice == 5:
    print("🙏 Thank you for visiting Numan Shop! Have a great day!")

else:
    print("Invalid choice! Please try again.")

# ---------------- BILL CALCULATION ----------------
if price > 0:
    quantity = int(input("Enter the quantity: "))
    total = price * quantity

    if total > 10000:
        discount = total * 0.20
        print(f"🎉 You got a 20% discount of Rs {discount}")
    elif total > 5000:
        discount = total * 0.15
        print(f"🎉 You got a 15% discount of Rs {discount}")
    elif total > 2000:
        discount = total * 0.10
        print(f"🎉 You got a 10% discount of Rs {discount}")
    else:
        discount = 0
        print("No discount applicable.")

    finalamount = total - discount
    print(f"🧾 Final amount to be paid: Rs {finalamount}")
    print("🙏 Thank you for shopping with Numan Shop! Visit again soon!")


