# all "$" represent python syntax in the ren.py file, so it is read as python code rather than renpy
$ from . import module
$ from asyncore import loop
$ import keyboard

# ren py character is defined for dialogue purposes
define narrator = Character("")

leftcount = 0
rightcount = 0

transform moveleft:
    linear 0.5 xpos - 0.10

transform moveright:
    linear 0.5 xpos 0.10

image charleft:
    "box"
    pause .5
    moveleft
    "moving box"
    pause .3
    moveleft
    "box"
    pause .5
    repeat

image charright:
    "box"
    pause .5
    moveright
    "moving box"
    pause .3
    moveright
    "box"
    pause .5
    repeat

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
    show box
    $charleft()
    if leftcount == 4:
        moveleft
    $charright()
    if rightcount == 4:
        moveright

        # we need to make the functions for moving up down left right of 5150, and a image for each type of movement for the 5150 sprite to be displayed

        # returns user to main menu
    return
