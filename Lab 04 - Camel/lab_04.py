import random

def main():
    print("Welcome to Outlaw Escape!")
    print("You are an outlaw, and have stolen a horse from a Native American to make your way across the vast prairie.")
    print("The Native Americans are chasing you down! Survive your journey and outrun them.")

    miles_traveled = 0
    thirst = 0
    horse_tiredness = 0
    natives_distance = -20  # Natives start 20 miles behind
    canteen_drinks = 3
    done = False

    while not done:
        print("\nA. Drink from your canteen.")
        print("B. Ride at moderate speed.")
        print("C. Gallop at full speed.")
        print("D. Rest for the night.")
        print("E. Check status.")
        print("Q. Quit.")

        user_choice = input("What is your choice? ").upper()

        if user_choice == "Q":
            print("You have quit the game.")
            done = True

        elif user_choice == "E":
            print(f"Miles traveled: {miles_traveled}")
            print(f"Drinks in canteen: {canteen_drinks}")
            print(f"The Native Americans are {miles_traveled - natives_distance} miles behind you.")

        elif user_choice == "D":
            horse_tiredness = 0
            print("Your horse is well-rested and happy!")
            natives_distance += random.randint(7, 14)

        elif user_choice == "C":
            distance = random.randint(10, 20)
            miles_traveled += distance
            thirst += 1
            horse_tiredness += random.randint(1, 3)
            natives_distance += random.randint(7, 14)
            print(f"You galloped {distance} miles!")

        elif user_choice == "B":
            distance = random.randint(5, 12)
            miles_traveled += distance
            thirst += 1
            horse_tiredness += 1
            natives_distance += random.randint(7, 14)
            print(f"You rode {distance} miles!")

        elif user_choice == "A":
            if canteen_drinks > 0:
                canteen_drinks -= 1
                thirst = 0
                print("You took a drink from your canteen. Ah, refreshing!")
            else:
                print("Your canteen is empty!")

        # Check thirst
        if thirst > 6:
            print("You died of thirst!")
            done = True
        elif thirst > 4:
            print("You are very thirsty!")

        # Check horse tiredness
        if horse_tiredness > 8:
            print("Your horse has collapsed from exhaustion! Game over.")
            done = True
        elif horse_tiredness > 5:
            print("Your horse is getting tired.")

        # Check if natives caught up
        if natives_distance >= miles_traveled:
            print("The Native Americans have caught you! Game over.")
            done = True
        elif miles_traveled - natives_distance < 15:
            print("The Native Americans are getting close!")

        # Check win condition
        if miles_traveled >= 200:
            print("Congratulations! You successfully escaped across the prairie!")
            done = True

        # Random chance of finding an oasis
        if not done and random.randint(1, 20) == 1:
            print("You found a small stream! You refill your canteen, quench your thirst, and rest your horse.")
            canteen_drinks = 3
            thirst = 0
            horse_tiredness = 0

if __name__ == "__main__":
    main()