#Aight gamers find the section youre assigned to and add in whatever you want
#to each of the strings

#someone needs to add a file to images called "bg room.jpg/png" to image
#someone needs to add a file to images called "char1 pogger.png/jpg"
#someone needs to add a file to images called "char2 pogger.png/jpg"
#someone needs to add a file to images called "object pogger.png.jpg"
#Hello world

#5 people

#Julia
#add a file to images called "bg room.jpg/png" to image
default charName1 = ""
default adjective1 = ""
default age = 0
default number = 0
default location = ""

#Ritvik
#someone needs to add a file to images called "char1 pogger.png/jpg"
default timeOfDay = "afternoon"
default season = ""
default relationship = "singular"
default activity = "present tense"
default charName2 = ""

#Frank
#someone needs to add a file to images called "char2 pogger.png/jpg"

default emotionNoun = "Flabbergasted"
default emotionNoun2 = "Depressed"
default emotionNoun3 = "Furious"
default material = "BRICK"
default verb = "shot"

#Ethan
#someone needs to add a file to images called "object pogger.png.jpg"
default relative = ""
default accident = ""
default excitedReponse = "Write out a full message, instead of just one word, kinda like this message"
default object = ""
default strongEmotion4 = ""

#Lucas
default emotionalVerb = "disliked"
default response = "If this happen my final grade will be a D"
default emotionalAdjective2 = "shy"
default object2 = "spoon"
default verb2 = "strike"
default relationship2 = "friend"


default currentAge = age + number


#add an image of the object to the image directory
#rename it to "object pogger.png" or "object pogger.jpg"

#add a character sprite to the images directory!
#you have to rename the file to follow the naming convention of
#charName emotion.png or charName emotion.png
#For our purposes, call the file
#"char1 pogger.png or char1 pogger.png"

#add a background whose file name follows naming convention of
#bg name.png or bg name.jpg, and add it to the images directory
#ex) "bg room.jpg" "bg room.png"


define char1 = Character("[charName1]")
define char2 = Character("[charName2]")
define char3 = Character("[charName3]")
define nar = Character("Narrator")


label start:

    #{color=#EA6A1A}[variable]{/color}

    scene bg room

    nar "It was a brisk, {color=#EA6A1A}[adjective1] [season] [timeOfDay]{/color}"

    show char1 pogger

    nar "{color=#EA6A1A}[charName1]{/color} had just arrived at {color=#EA6A1A}[location]{/color}"

    nar "They were here to {color=#EA6A1A}[activity]{/color}, and that's what they had planned to do if it was not for something unexpected."

    show char1 pogger at left

    # These display lines of dialogue.

    char1 "I didn't expect to see {color=#EA6A1A}[charName2]{/color}, their childhood {color=#EA6A1A}[relationship]{/color}"

    show char2 pogger at right

    char2 "Hello {color=#EA6A1A}[charName1]{/color}. We haven't seen each other since we were {color=#EA6A1A}[age]{/color} years old."

    char2 "How long has it been since then?"

    char1 "I think it's been {color=#EA6A1A}[number]{/color} years. That makes us-"

    char2 "{color=#EA6A1A}[currentAge]{/color} years old."

    char2 "...I still have strong feelings of {color=#EA6A1A}[emotionNoun]{/color} towards you, {color=#EA6A1A}[charName1]{/color}"

    nar "Hearing {color=#EA6A1A}[charName2]{/color} say this made {color=#EA6A1A}[char1]{/color} feel {color=#EA6A1A}[emotionNoun2]{/color}."

    char1 "Gosh, I don't know how to respond in an ambigious enough way that encompasses every possible emotion."

    char2 "It's okay, you don't have to."

    char1 "What brings you here anyways, {color=#EA6A1A}[charName2]{/color}, my childhood {color=#EA6A1A}[relationship]{/color}"

    char2 "Ever since you lost your {color=#EA6A1A}[relative]{/color} in the {color=#EA6A1A}[accident]{/color}, I have felt {color=#EA6A1A}[emotionNoun3]{/color}"

    char2 "Because of that, I came to give you this."

    nar "{color=#EA6A1A}[charName2]{/color} approached {color=#EA6A1A}[charName1]{/color} and handed them a package wrapped in {color=#EA6A1A}[material]{/color}."

    nar "In response to the gift, {color=#EA6A1A}[charName1]{/color} started {color=#EA6A1A}[verb]{/color}."

    nar "After collecting themselves, {color=#EA6A1A}[charName1]{/color} opened the package, revealing a..."

    show object pogger

    nar "{color=#EA6A1A}[object]{/color}"

    char1 "{color=#EA6A1A}[excitedReponse]{/color}"

    char1 "You got a {color=#EA6A1A}[object]{/color} just for me?!"

    char2 "Indeed."

    char1 "If my {color=#EA6A1A}[relative]{/color} had survived the {color=#EA6A1A}[accident]{/color}, I know that they would have {color=#EA6A1A}[emotionalVerb]{/color} this gift!"

    char2 "Gosh- I don't know what to say in response to that{color=#EA6A1A}[charName2]{/color}, my childhood {color=#EA6A1A}[relationship]{/color}"

    char2 "Actually- I do know what to say"

    char2 "{color=#EA6A1A}[response]{/color}"

    nar "{color=#EA6A1A}[charName1]{/color} started to feel {color=#EA6A1A}[emotionalAdjective2]{/color} towards {color=#EA6A1A}[charName2]{/color}"

    char1 "I will make sure to get you a {color=#EA6A1A}[object2]{/color} next time we meet."

    nar "The two came in close to {color=#EA6A1A}[verb2]{/color} eachother"

    nar "And thus started the change in {color=#EA6A1A}[charName1] and [charName2]'s{/color} relationship, from {color=#EA6A1A}[relationship]{/color} to {color=#EA6A1A}[relationship2]{/color}."



    # This ends the game.

    return
