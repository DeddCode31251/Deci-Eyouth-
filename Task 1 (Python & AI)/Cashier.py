"""
Made by Mark Richard
You can add UI With tkinter library
"""
products = ["Milk", "Bread", "Rice", "Apple", "Juice"]

prices = [40, 70, 50, 65, 115]

 

cart = []

total = 0

 

print("=== Future Mall ===")

 

while True:

    print("\nProducts:")

    for i in range(5):

        print(i + 1,".", products[i], "-", prices[i], "EGP")

 

    choice = input("Choose product (1-5) or 0 to finish: ")

 

    if choice == "0":

        break

 

    if choice in ["1", "2", "3", "4", "5"]:

        choice = int(choice) - 1

        cart.append(products[choice])

        total += prices[choice]

        print(products[choice], "added.")

    else:

        print("Invalid choice!")

 

discount = 0

if total > 500:

    discount = total * 0.10

 

final_total = total - discount



print("\n===== RECEIPT =====")

print("Future Mall")

print("------------------")

 
for item in cart:

    print(item)

print("------------------")

print("Original Total:", total, "EGP\nDiscount:",discount,"EGP\nFinal Total:",final_total,"EGP\nThank you!")
