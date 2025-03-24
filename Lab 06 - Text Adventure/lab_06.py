class Room:
    def __init__(self, description, north=None, east=None, south=None, west=None, item=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.item = item

# Intro when ran
def main():
    print("Welcome to the Abandoned Factory Escape!")
    print("You are trapped in an old factory. Something seems off, find the key and use it to unlock the exit door.")
    print("Move using north (n), east (e), south (s), or west (w). Type 'use key' to escape when at the exit door.")
    print("If you find a key, grab it by typing 'grab key'. If you find the exit, use the key by typing 'use key'.")
    print("Type 'quit' to end the game.")

    room_list = []

    # Creating rooms with descriptions
    room_list.append(Room("You are in an old dusty office. You hear someone breathing.", 1, None, None, None))
    room_list.append(
        Room("You are in a dimly lit hallway. The walls are scratched. Something was here.", 2, None, 0, 4))
    room_list.append(
        Room("You are in a storage room. Rusty tools hang from the walls. A single key lies on the floor.", 5, 3, 1,
             None, "key"))
    room_list.append(
        Room("You are in a factory floor, old machines sit silently. The exit door stands locked. This is your way out!", None, None, None,
             2))
    room_list.append(
        Room("You are in a break room. The vending machine hums, but the snacks are long expired.", None, 1, None,
             None))
    room_list.append(
        Room("You are in a boiler room. Steam leaks from old pipes, and the air is thick with rust.", None, 6, 2, None))
    room_list.append(
        Room("You are in a security office. The monitors flicker, showing static and glimpses of movement.", None, None,
             5, None))

    current_room = 0
    inventory = []
    done = False

    # Code for key

    while not done:
        print("\n" + room_list[current_room].description)

        if room_list[current_room].item == "key" and "key" not in inventory:
            action = input("Would you like to grab the key? (grab key)\n").strip().lower()
            if action == "grab key":
                inventory.append("key")
                room_list[current_room].item = None
                print("You picked up the key.")
                continue

        action = input("What do you want to do?\n").strip().lower()

        if action in ["n", "north"]:
            next_room = room_list[current_room].north
        elif action in ["e", "east"]:
            next_room = room_list[current_room].east
        elif action in ["s", "south"]:
            next_room = room_list[current_room].south
        elif action in ["w", "west"]:
            next_room = room_list[current_room].west
        elif action == "use key" and current_room == 3:
            if "key" in inventory:
                print("You use the key to unlock the door. You have escaped!")
                break
            else:
                print("You don't have a key to use.")
                continue
        elif action == "quit":
            done = True
            continue
        else:
            print("Invalid command.")
            continue

        if next_room is not None:
            current_room = next_room
        else:
            print("You can't go that way.")


if __name__ == "__main__":
    main()
