print(".... Welcome to Ultimate Shop ....")
coins = 100
bill = 0
potion = 0
sword = 0
shield = 0
while True:

    print("<====Menu====>")
    print(f"Your coins: {coins}")
    print("1. Potion - 20\n" \
    "2. Sword - 50\n" \
    "3. Shield - 40\n" \
    "4. Exit"
    )
    user = int(input("Choose: "))

    if user == 1:
        if coins >= 20:
            print("\nPotion purchased.")
            coins -= 20
            bill += 20
            potion += 1
        else:
            print("\nNot enough coins.")
    elif user == 2:
        if coins >= 50:
            print("\nSword purchased.\n")
            coins -= 50
            bill += 50
            sword += 1
        else:
            print("\nNot enough coins.")
    elif user == 3:
        if coins >= 40:
            print("\nShield purchased.\n")
            coins -= 40
            bill += 40
            shield += 1

        else:
            print("\nNot enough coins.")
    elif user == 4:
            break
    else:
        print("\nInvalid Number!!")

print("\n<=== RECIPT ===>")
print(f"Potion x {potion} - {20*potion}\n" \
f"Sword x {sword} - {50*sword}\n" \
f"Shield x {shield} - {40*shield}\n"\
f"Bill : {bill}")