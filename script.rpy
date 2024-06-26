# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sam = Character("Samuel", color = "#0FAFE7")
define s = Character("Sean")
define b = Character("Boss", color = "#1EDB0E")
define c = Character("...", color = "#000000")


# The game starts here.

label start:
    play music "casual.mp3"


    scene bg tallbuilding

    show man1:
        zoom 2.5


    sam "Man how late can you be!"

    s "Probably much more"

    sam "Shut up"
    sam "The boss wants to see you anyway"
    sam "You're finished"

    s "Of course he does"
    s "Sick of that man"

    menu:
        "Go to the boss' office":
            s "(Well, may as well)"
            hide man1
            scene bg newspaper
            show bosstabletalking
            play sound "doorclose.MP3"
            b "Just the man I've been looking for!"
            b "I have a little propsition"
            hide bosstabletalking
            show bosstable
            s "Don't you mean proposition?"
            b "..."
            hide bosstable
            show bosstabletalking
            b "Shut up"
            b "Either you magically hand me up that 20 page document from the other day"
            b "Or you're fired"
            hide bosstabletalking
            show bosstable
            s "You're kidding! I was sick!"
            hide bosstable
            show bosstabletalking
            b "Well. There's also a third option..."
            hide bosstabletalking
            show bosstable
            menu:
                "What is it?":
                    s "What exactly?"
                    hide bosstable
                    show bosstabletalking
                    b "I just need you to get some paperclips from that door *points right*"
                    hide bosstabletalking
                    hide bg newspaper

                    show scaryroom
                    stop music
                    play music "heartbeat.MP3"
                    s "How have I never noticed that before?"
                    b "Idk man, bad eyesight or something"
                    b "Now"
                    b "Go on in my boy!"
                    hide scaryroom
                    show blackscreen

                    s "(Now where is this darned light switch)"
                    s "Ah!"
                    s "Found it *switches it*"
                    play sound "lightswitch.mp3"
                    hide blackscreen

                    show bossclone1
                    stop music
                    c "Do you have my sunshine?"
                    s "(What the hell is that?)"
                    show bossclone2
                    play sound "standingupclone.MP3"
                    c "Do you think I'm pretty?"
                    s ""
                    show blackscreen
                    play sound "creatureroar.mp3"
                    s "Uh oh"

                    show scaryroom
                    play sound "seanscream.mp3"
                    s "AGHHHHHHH"
                    show bosswins with fade
                    ""
                    scene bg badending
                    play sound "Loss.mp3"
                    ""

                "Don't care, I QUIT":
                    s "Nah, I've hated you for too long"
                    hide bosstable  
                    s "Wow"
                    s "I really got lucky"
                    stop music
                    scene bg goodending
                    play sound "Victory.mp3"
                    ""


        "Don't go and resign":
            s "Tell him I quit! *Walks out of building*"
            hide man1
            scene bg newspaper
            s "Wow"
            s "I really got lucky"
            stop music
            scene bg goodending
            play sound "Victory.mp3"
            ""

    # This ends the game.

    return
