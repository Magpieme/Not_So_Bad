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

    "This was supposed to be a normal day..?"

    "Did you spend too much time in front of your T.V.?"

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

    "Shit.. why did landing on the ground hurt so much...?"


    "It's the only thing here that makes a dollup of sense."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show raidd fear


    # These display lines of dialogue.

    show raidd fearagape
    e "holy fuck."

    e "why am I..."
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

    e "why am i in fucking icarly???"

    play music "/audio/epicbgm.mp3" fadein 1

    show raidd fear
    "What would be blissful nostalgia about your favorite family-friendly sitcom from the early 2000's had been haulted by the... reality... of it all."

    "You scramble through your memory, trying to figure out how you got roped into.."

    show raidd alwayshasbeen

    "Whatever this hellish place was...."

    show raidd fear

    menu:
        "i dont know lmfao":
            jump choice1_yes



        "i came here after doin ur mom":
            jump choice1_no



    label choice1_yes:
        $mom_flag = False
        show raidd fearagape
        e "i dont fucking know either akjslkjfs"
        menu:
            "yeah":
                show raidd fearagape
                jump choice1_done
            "who does tho":
                jump add_buzzington

    label choice1_no:
        play sound "audio/doin-ur-mom.mp3"
        $mom_flag = True
        "You stop to process the words that was haphazardly spewed out of your own mouth."
        "Were those even your own words...?"
        show raidd fearagape
        e "why are you screwing my mom too???"
        show raidd blush
        e "the only thing i was screwing over was my chances with that cute girl!!"
        show raidd fearagape
        e "goddamnit ehwatthefuck"

        jump choice1_done



    label choice1_done:
    "Your mind jumps back to the room sprawled around you."

    "The consistency of the props.. the material of the floor below you"

    "How did they get the scenery so exact.."

    "You think back on how you are so distinclty aware of all this iCarly Information."

    e "my sister watched that fucking show when she was like eight??"

    e "god, it was an absolute slog to watch."

    e "i could have used the fucking sega xbox to play fucking sonic the hedgehog!!!"

    "You grimace as your fairly mild and inconsequential childhood trauma flashes befor your eyes."

    e "the themes is fucking awful, too."

    show raidd blush

    e "instead of the smooth buttery beats of knuckles the Echinda whispering sweet nothings to me.."

    show raidd forwardagape

    e "not in a gay way though. im not gay. i like girls. and pecenu."

    show raidd fearagape

    e "the way they got some fucking {b} FEMOID {/b} to screech into our eardrums!"

    e "giving all of our ears fucking cooties!"

    e "how did they physically make a song that painful to listen to-"

    play music"/audio/icarly-theme-dance.mp3" fadeout 1

    show raidd fear
    e " "

    show raidd fearagape
    e "OH GOD FUCKING DAMN IT"

    show raidd fear
    "You attempt to bury yourself in the depths of your hoodie."

    "Miranda Cosgrove's voice forces you out of your shelter."

    scene scenehelp

    hide raidd fear

    "You watch the universe convulse in horror."

    e "hello...?"

    "Nobody answers. The instrumental only continues to blast."

    "You can't just talk your way out of this one."

    "Instead of the easy comfort of ignoring the events around you, you were shoved facefirst into a surreal hellscape."

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
        "dad??? you came back from the store???":
            jump choice2_yes


        "i thought we broke up what the fuck!!!":
            jump choice2_no


    label choice2_yes:
        show raidd fear:
            xalign 0.25
            yalign 1.0
        "The world stops."

        "A confused plea dribbles out of your mouth."
        show raidd fearagape:
            xalign 0.25
            yalign 1.0
        e "dad..?"
        show raidd cryagape:
            xalign 0.25
            yalign 1.0
        e "its been... its been seven years..."

        e "mom.... shes gone..."

        e "do you know how ALONE i felt.????"

        show raidd cry

        "Your soft sniffling stifles the zany atmosphere of the props around you."

        "How alone you thought you were..."

        "After what feels like hours, you manage to conjure up a sentence."

        show raidd cryagape:
            xalign 0.25
            yalign 1.0

        e "where... where were you..."

        if mom_flag == True:

            "Gibby pauses before you."

            "Was this a moment of hope? A single giblet of solace?"

            show gibby smile:
                xalign 0.75
                yalign 1.0

            "His warped smile shoots down your hope."

            g "you know exactly what i was doing, Onyx."

            e "what??"

            scene goddiedonthisholyday
            hide gibby smile
            hide raidd cryagape

            "Gibby expands across the room. Your foot bumps into a chunk of his rolls."

            e "PLEASE!!"

            "You attempt to writhe yourself free."

            "Nothing happens."

            e "STOP!! PLEASE!!!"

            e "I WANT TO GO HOME!!!"

            e "ERIC!! MAMI!!!!"

            e "HELP!! PLEASE!!!"

            "Nobody answers."

            jump choice2_badend

        else:
            jump choice2_endtest


    label choice2_badend:
        g "your mom says hi."
        play sound "audio/doin-ur-mom.mp3"
        "\n\BAD END - STACEYS MOM"

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
        
        if buzz_flag == True:
		
		"Congratulations."
		
		"\n\BAD END - See you in the Sequal."
		
		return
		
		else
        menu:
            "give up":
                jump buzzington_end

    label buzzington_end:
    $buzz_flag = True
	
	b "I have taken control of the narrative now."
	
	b "This story, like all other stories, is mine."
	
	"I must protect causality."
	
    jump add_buzzington