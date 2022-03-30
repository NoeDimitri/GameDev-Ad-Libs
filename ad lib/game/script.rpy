#Aight gamers find the section youre assigned to and add in whatever you want
#to each of the strings

#Person 1
default charName = ""
default adjective = ""
default numberCheck = 12

#Person 2
default charName2 = ""
default adjective2 = ""

#Person 3
default charName3 = ""
default adjective3 = ""

define e = Character("[charName]")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "why did this not work [numberCheck]"

    # This ends the game.

    return
