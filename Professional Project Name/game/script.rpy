# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Onyx Raidd", who_color="#9a0a0c")
define f = Character("???", who_color="#86cecb")
define g = Character("Gibby", who_color="#86cecb")
define b = Character("Mr. Buzzington", who_color="#b39700")

# The game starts here.

label start:

    "You slip between reverie and reality."

    "The universe falters before you."

    "This was supposed to be a normal day...?"

    "Did you spend too much time in front of your TV?"

    "Did you awaken the wrath of an eldritch beast whilst you were dancing in your dreams?"

    "Is this some sick form of cosmic retribution?"

    "You feel your grasp on this world leaving you..."

    $ renpy.movie_cutscene("stream.webm")



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg zoom
    with Dissolve(.5)

    pause .5


    play sound "/audio/bonk.mp3"

    "The firm knock of the wooden floor greets you as you open your eyes."

    "Shit. Why did landing on the ground hurt so goddamn much...?"


    "It's the only thing here that makes a dollup of sense."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show raidd fear


    # These display lines of dialogue.

    show raidd fearagape
    e "Holy fuck."

    e "Why am I..."
    show raidd fear:
        xalign 1.0
        yalign 1.0
    "You pace through the all-too familiar studio."
    show raidd fear:
        xalign 0.0
        yalign 1.0
    "The steps... The elevator..."
    show raidd fear:
        xalign 0.5
        yalign 1.0

    "Hell, even the cameras were set up..."

    show raidd fearagape

    e "...Am I in fucking iCarly."

    play music "/audio/epicbgm.mp3" fadein 1

    show raidd fear
    "What would be blissful nostalgia about your favorite family-friendly sitcom from the early 2000's had been hauted by the... absurdity of it all."

    "You scramble through your memory, trying to figure out how you got roped into.."

    show raidd alwayshasbeen

    "Whatever this shitshow was. You... you live in Philly, how the hell did you get to Los Angeles-"

    show raidd fear

    menu:
        "beats me lmfao":
            jump choice1_yes



        "i got here doin ur mom":
            jump choice1_no



    label choice1_yes:
        $mom_flag = False
        show raidd fearagape
        e "beats me lmfao"
        menu:
            "Yeah. Let's be honest though...":
                show raidd fearagape
                jump choice1_done
            "Who does?":
                $buzz_flag = False
                jump add_buzzington

    label choice1_no:
        play sound "audio/doin-ur-mom.mp3"
        $mom_flag = True
        "You stop to process the words that suddenly spewed from your mouth."
        "You... you didn't say that. That wasn't you."
        show raidd fearagape
        e "What the fuck???"
        show raidd blush
        e "The only thing I was screwing over was my chances with that cute girl!!!"
        show raidd fearagape
        "You think of who you left behind, back in your own world."
        "...Pecenu. When she comes back, she's going to wonder why you're not saying anything to her."
        e "...Shit."

        jump choice1_done



    label choice1_done:
    "You decide to try and figure out how you got here to keep your mind off of that whole thing. You can deal with it later."

    "The consistency of the props.. the material of the floor below you."

    "How did they always keep this place so... precise. Doesn't this stuff get pushed around from time to time?"

    "You think back on how you are so distinctly aware of all this iCarly Lore."

    e "...Oh my god my sister watched this show when she was like, a teenager."

    e "Shit was trash."

    e "Could've used the fucking Sega Xbox to play fucking Sonic the Hedgehog!!!"

    "You grimace as a milder part of your childhood trauma flashes before your eyes."

    e "That theme is like nails on a chalkboard, too."

    show raidd blush

    e "...Much prefer Knuckles the Echinda whispering sweet nothings to me..."

    show raidd forwardagape

    e "NOT IN A GAY WAY THOUGH. I'M NOT GAY. I like... girls. And Pecenu."
    
    "...You can almost *hear* the Pumpkin Hill theme."
    "Those chill tunes... those were simpler times."
    "Then again, anything is simpler than being mysteriously transported onto the set of iCarly."

    show raidd fearagape

    e "The way they got some fucking {b} FEMOID {/b} to perform... that!"

    e "Giving all of our ears fucking cooties! It's so damn loud!"

    e "How did they make a song that {b} PHYSICALLY PAINFUL {/b} to listen to!"

    play music"/audio/icarly-theme-dance.mp3" fadeout 1

    show raidd fear
    e " "

    show raidd fearagape
    e "OH GOD FUCKING DAMN IT-"

    show raidd fear
    "You attempt to bury yourself in the depths of your jacket."

    "Despite your efforts, you cannot escape the damning voice of Miranda Cosgrove."

    scene scenehelp

    hide raidd fear

    "She mocks you. You attempt to hide, but the music seems to be coming from inside your head."

    e "stop..."

    "Of course, nobody answers. In fact, you think you can {i} feel {/i} the instrumentals get louder."

    "It's deafening."

    "You're a few seconds away from curling up in a ball and just... giving up on all of this."

    scene helpcutscene
    with Dissolve(.5)

    "Carly Shay watches your crimes crawl across your back."

    "You could have done so much, Onyx."

    "You could have helped the people around you do something great with their lives."

    "The universe could have been standing."

    "Your family could have been proud of you."

    scene spooky

    "You could have been proud of yourself."

    "How does it feel being a faliure, Onyx?"

    stop music

    voice "audio/gibbay.mp3"
    f "GIBBBAAAAAAAYYYYYYY"

    scene bg zoom

    "The crash from above you throws you out of your carly-induced breakdown."

    "You whip around as that familiar voice grounds you once again."

    show gibby

    g "This isn't Build-A-Bra!!!"


    show gibby:
        xalign 0.75
        yalign 1.0
    show raidd fear:
        xalign 0.25
        yalign 1.0

    "You take a moment to proccess the icon himself standing before you."

    e "holy shit?????"

    menu:
        "...Dad?":
            jump choice2_yes


        "... (Why is my ex here?!)":
            jump choice2_no


    label choice2_yes:
        show raidd fearagape:
            xalign 0.25
            yalign 1.0
        "You can only stare for a few seconds before choking that one word out."

        show raidd fear:
            xalign 0.25
            yalign 1.0
        e "You..."
        show raidd cryagape:
            xalign 0.25
            yalign 1.0
        e "I..."

        e "Where have you been?!"

        e "...do you know how {b} ALONE {/b} I felt?"

        show raidd cry

        "Your soft sniffling is a stark contrast to the zany atmosphere around you."

        "You never met your dad, but you just {i} know {/i} that it's him..."

        "After what feels like hours, you manage to conjure up a pitiful sentence."

        show raidd cryagape:
            xalign 0.25
            yalign 1.0

        e "where... where were you..."

        if mom_flag == True:

            "Gibby- your dad- stares at you for a second."

            "You can't quite pin the expression on his face."

            show gibby smile:
                xalign 0.75
                yalign 1.0

            "You feel distraught, seeing his expression change like that."

            g "{b} you know exactly what i was doing, onyx. {/b}"

            e "...Huh?"

            scene goddiedonthisholyday
            hide gibby smile
            hide raidd cryagape

            "Gibby expands across the room. Your foot bumps into a chunk of his rolls before the mass starts to consume you."

            e "wAIT-"

            "You attempt to pull yourself free."

            "Nothing happens."

            e "S-STOP! WAIT!"

            e "DON'T- STOP!!"

            e "...I WANT TO GO HOME!"

            e "HELP!"
            
            e "MA! ERIC!"
            
            e "{i}S-SOMEONE!{/i}"

            "Nobody answers."

            jump choice2_badend

        else:
            jump choice2_endtest


    label choice2_badend:
        g "your mom says hi, by the way."
        play sound "audio/doin-ur-mom.mp3"
        "\n\BAD END - MEET YOUR MOTHER"

        return

    label choice2_endtest:
        # This ends the game.

        return
        
    label add_buzzington:
        stop music
        stop sound
    
        hide raidd fear
        
        b "You have done well, child."
        
        scene bg dark
        
        b "Welcome."
        
        play music "audio/reversereverb.mp3"
        
        b "The real game begins now."
        
        if buzz_flag == False:
            menu:
                "give up":
                    jump buzzington_end

        else:        
            "Congratulations."

            "\n\BAD END - See you in the Sequal."

            return

    label buzzington_end:
    $buzz_flag = True
    
    b "I have taken control of the narrative now."
    
    b "This story, like all other stories, is mine."
    
    "I must protect causality."
    
    jump add_buzzington
