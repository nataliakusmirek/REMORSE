# all "$" represent python syntax in the ren.py file, so it is read as python code rather than renpy
$ from . import module
$ from asyncore import loop
$ import keyboard

# make a text box for each character that speaks so you can understand who is who..
# ren py character is defined for dialogue purposes
define narrator = Character("")
define user = Character("5150")
define janet = Character("3019")
define roger = Character("Roger")

image user = "5150/5150-right.png"
image user dumb = "5150/5150-dumb.png"
image user cry = "5150/5150-cry.png"
image user sleep = "5150/5150-sleep.png"
image user tired = "5150/5150-tired.png"
image janet = "3051/3051-idle.png"
image janet right = "3051/3051-right.png"
image janet evilleft = "3051/3051-evilleft.png"
image janet dumb = "3051/3051-dumb.png"
image janet confused = "3051/3051-confused.png"

# the python block allows for python functions and syntax to be used without renpy (unless the renpy library is called)
init python:

    def glitch(xinput, yinput):
        for i in range(2):
            xinput_check = xinput.strip()
            yinput_check = yinput.strip()
        if xinput_check.lower() == "11" and yinput_check.lower() == "31":
            return 0
        else:
            renpy.say(narrator, "Wow, you're bad at puzzles. I'll do it myself-")

    def charleft():
        for i in range(4):
            if keyboard.is_pressed('a') == True:
                renpy.show("charleft")
                leftcount += 1
        else:
            renpy.show("box")

    def charright():
        for i in range(4):
            if keyboard.is_pressed('d') == True:
                renpy.show("charright")
                rightcount += 1
        else:
            renpy.show("box")

    # keyboard is not defined apparently

# beginning of game
label start:

    # first "room" is displayed based on an image: list is defined and is called on by the character "narrator"
    scene bg room
    $ list = ['{color=6DF244}Earth{/color}', '{color=F24444}council{/color}', '{color=F72F2F}downfall{/color}', '{color=6AE6E1}we{/color}']
    $renpy.pause(delay=3)
    show earth at truecenter with fade
    narrator "There was a time when humans lived on [list[0]]."
    narrator "A planet home to life, culture, and prosperity."
    narrator "But the humans began to damage the Earth."
    narrator "Some humans tried to fight for change, but those in the power, the [list[1]], ignored this."
    narrator "Earth fell into chaos and destruction, leading to its eventual...."
    narrator "I suppose you could say, [list[2]]."
    narrator "The council saved themselves by creating a ship, the very ship [list[3]] are on."
    window hide
    hide earth
    $renpy.pause(delay=2)

    # second "room" is displayed
    scene bg begin
    with fade
    $renpy.pause(delay=3)

    # screen Glitch (a pop-up window made in a different file) is displayed, then narrator dialogue, then Glitch() the function is called after parameters are inputted
    $renpy.show("bg room")
    call screen Glitch("ERROR\nGlitch Detected")
    narrator "You must reso1ve the gl1tch! Ent3r the r1ght numbers..."
    narrator "You only have one try.."
    $xinput = renpy.input("Number 1:", length=3)
    $yinput = renpy.input("Number 2:", length=3)
    $ glitch(xinput, yinput)
    call screen Glitch("ERROR RESOLVED\nREBOOTING...")
    $renpy.pause(delay=1)

    # make the cell background appear for chapter one, then 5150 should fall into the cell from the top of the screen
    scene bg room

    narrator "It seems you're back online... let's begin."
    $renpy.pause(delay=1)

    scene bg dorm1
    with fade
    call screen Glitch("This is you.\n You'll learn soon enough...")

    user "Where..what is this place?"
    scene bg dorm2
    janet "Oh, you must be my new roommate!"
    janet "I'm 3019. Nice to meet you."
    user "..."
    janet "Oh...you're 5150 aren't you.."
    janet "That's...we'll make it work."
    user "Wait..what?"
    janet "You'll learn in class, which, we should head to right now."
    user "Class??"
    janet "Yes. That's where we learn 'necessary ideas'."
    janet "It's almost time. Follow me."

    scene bg class1
    with dissolve
    roger "Ah.. a new student I presume."
    roger "Please take a seat, you're late enough as is. What is your name?"
    scene bgclass2
    menu:
        "How do I respond..?"

        "5150.":
            user "My name is 5150."
            roger "Welco- oh my. Do not say that so loudly.."
            user "Why...?"
            roger "New student, please meet me after class. Let's start today's lesson."
        "New student.":
            roger "Ah, I see. A clever one are you?"
            roger "Meet me after class."
    label after_menu:

        roger "Alright, can anyone tell me the motto of our sociology lesson?"
        janet "May I?"
        roger "Of course, 3019."
        janet "Ahem.."
        janet "To live is to hunter others, to make sure you are on top, and the rest fall to the bottom,"
        user "*What the hell...*"
        roger "Excellent! New student, this motto applies to every act, being, and thought you ever experience in your lifetime."
        roger "Now, we all know the past society was dreadful, in fact, what happened?"
        janet "They all died because they destroyed their planet."
        roger "Precisely! Now, think about us today: how are we doing?"
        roger "New student, I'd like to hear your thoughts on this."
    menu:
        "Well.."

        "I do not agree with these ideas, what society? What mistakes?":
            roger "Hm...a rebellious one truly."
            roger "3019, do keep an eye on them. New student, let's discuss this AFTER class and NOT during it."
            roger "Ahem."

        "I cannot say, I woke up and went to this weird lecture..":
            roger "Well, I wouldn't call us 'weird', but it seems you do not know the history of our ship."
            user "Ship? Wait what?"
            roger "Please, you are disturbing class..."
            roger "I shall discuss it with you once the lecture is OVER, not DURING IT."
    label after_menuu:
        "Let's continue."
        $renpy.pause(delay=2)

    scene bg room
    with dissolve
    # play bell ringing
    $renpy.pause(delay=2)

    scene bgclass3
    with dissolve
    janet "5150, let's head back to our dorm."
    user "I thought the teacher wanted to see me after class."
    janet "Eh, nothing I couldn't tell you."
    menu:
        "It's your choice, 5150."

        "Go back to the dorm.":
            user "You definitely showed you know about the ship, sure, let's go back."
            janet "Great! Alright, let's go."
            roger "*What is that bot up to?*"

        "Stay after class.":
            $default choiceDone = False
            user "I think I'll stay, it seems I really know nothing."
            janet "Eh, okay. I'll see you back at the dorm."
            scene bgclass4
            roger "Good, you are here."
            roger "You are a threat to this ship, everything they've built."
            roger "You must find six orbs that power the ship, then you can shut this down once and for all and send a distress signal to save us."
            label important:
                menu:
                    "What are you telling me all this?":
                        roger "I was once in the council, the group of engineer that run this ship."
                        roger "They denominated me after I tried taking over the ship. But you are our last chance."
                        roger "It will be dangerous, but anyone who shows TRUE emotions, you can trust."
                        $ choiceDone = True
                        jump important
                    "How am I dangerous? I'm just a kid...":
                        roger "A '5150' has not been seen since Earth exploded."
                        roger "You represent mass destruction and rebellion."
                        roger "Do you not remember anything when you woke up?"
                        user "Just a glitch..."
                        roger "I see... remember that. :)"
                        jump important
                    "What is the council?" if choiceDone:
                        roger "A group of engineers, who, instead of using their smarts to save Earth,"
                        roger "..they focused on finding ways to live without it."
                        roger "They became dictators of this ship, and no one knows how the ship runs: the unknown source."
                        roger "There is a rebellion called Kalon though, which can help."
                        roger "They stole one of the council's ships, and use it as a base of operations: thats who you need to send the distress signal to."
                        jump important

            label after_menuuuu:
                roger "Listen, I am going to give you my keycard."
                roger "It will give you access to all doors, but you probably won't be able to use it for awhile."
                roger "You need to get out of here, before I get reported and they come to dispose of you."
                user "Dispose?!"
                roger "I have a friend who you can trust, he lives in the vents to hide from all of this."
                roger "Use the vent in your room, and you'll get to him."
                roger "Good luck."

    label after_menuuu:
        scene bg room

        show bgdorm 4 with fade
        # we need to make the functions for moving up down left right of 5150, and a image for each type of movement for the 5150 sprite to be displayed

        # returns user to main menu
    return
