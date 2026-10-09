"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# Start the player in the Hall
current_room = "Great Hall"

# print a welcome message and the current room.
print("Welcome to the Dragon Text Game!")

print("Move commands: North, South, East, West, exit")

print("-" * 40)
# loop until the player enters "exit" or a valid movement command.
while True:
    # display the room before each movement prompt for clarity.
    print(f"You are in the {current_room}.")

    # prompt for a movement command or "exit".
    command = input("Enter your move: \n").strip().lower()

    # check if the player wants to exit.
    if command == "exit":
        print("Thanks for playing the game. Hope you enjoyed it.")
        break
        print("-" * 40)

    # check if the command is a valid movement direction.
    if command in rooms[current_room]:
        # update the current room based on the movement command.
        current_room = rooms[current_room][command]
        print(f"You move {command} to the {current_room}.")
        print("-" * 40)
    else:
        # handle invalid movement commands.
        print("Invalid command entered!")
        print("-" * 40)
