# Ask the player for their name.
name = input("Who has the pleasure of playing this game? Please provide your name: \n")

# Display a message that greets them and introduces them to the game world.
print(f"Welcome {name}, to the command-line world of Dungeons and Dragons!\n")

#room assignment: "c" = corridor; "l" = left (empty) room; "r" = right (dragon) room
player_pos = "c"

#possess sword?
sword = False

#dragon status
dragon_dead = False

while dragon_dead == False:
## Present them with a choice between two doors.
    player_pos = "c"
    while player_pos == "c":
        door_choice = input("As you enter into the dungeon and navigate its dark corridor,\nyou come accross two doors. Which will you enter? left or right: ")
        ## If they choose the left door, they'll see an empty room
        if door_choice == "left":
            player_pos = "l"
            print("You have entered into a dark and seemingly empty room.\n")
        ## If they choose the right door, then they encounter a dragon.
        if door_choice == "right":
            player_pos = "r"
            print("You have entered into the lair of an ornery dragon!\n")
    while player_pos == "l":
        ## When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
        if player_pos == "l":
            look_around = input("Do you want to further explore the seemingly empty room? yes or no: \n")
            if look_around == "yes":
                take_sword = input("You have found a sword! Do you wish to take the sword? yes or no: \n")
                if take_sword == "yes":
                    sword = True
                else:
                    sword = False
            left_to_hall = input("Do you want to remain in this room or return to the corridor? Please enter stay or return: \n")
            if left_to_hall == "return":
                player_pos = "c"
            else:
                print("Well, this is fun.\n")
                continue
    while player_pos == "r":
        ## When encountering the dragon, they have the choice to fight it.
        if player_pos == "r":
            fight_safety = input("Do you wish to fight the dragon or return to the safety of the corridor? Enter fight or safety: \n")
            if fight_safety == "fight" and sword == True:
                dragon_dead = True
                break
        # If they don't have the sword, then they will be eaten by the dragon and lose the game
            elif fight_safety == "fight" and sword == False:
                print("You made a poor decision. Fighting the dragon without a weapon resulted in your death. You lose.\n")
                quit()
            elif fight_safety == "safety":
                player_pos = "c"
                print("You safely regressed back to the corridor and out of danger from the dragon.\n")

print("You found the sword and chose to fight the dragon, which you successfully slayed. Congratulations - you win!")