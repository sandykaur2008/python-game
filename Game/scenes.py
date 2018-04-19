from random import randint 
from textwrap import dedent 
from sys import exit 

class Scene(object):
    def enter(self):
        pass

class Death(Scene):
    lines = ['Wow, you suck at this! Bye!', 
        'Dead already? Damn lol',
        'You dead, loser.',
        'We ate you, you dead.',]
    def enter(self):
        print Death.lines[randint(0,len(self.lines)-1)] + '\n'
        exit(1)

class ObservationRoom(Scene):
    def enter(self):
        print dedent("""
        You're an explorer on a submarine, enjoying the view 
        in the Observation Room. You suddenly see lots of sharks and
        feel a tremendous shaking - someone gets on the intercom
        and screams, 'We've been hit by sharks! We're taking on water
        AND sharks! ARGHHHHHHH!' You have a choice - enter '1' to go out
        and fight the sharks or '2' to make your way to the Main Corridor and 
        get to the escape pod that will take you to the surface. Remember that you
        currently have no weapons...gulp!
        """)

        choice = int(raw_input('>')) 

        if choice == 1:
            print dedent ("""
            Ah, bad choice. You were no match for the sharks...They have a 
            message for you:
            """)
            return 'death'
        elif choice == 2: 
            print "Good idea!" 
            return 'main_corridor'
        else:
            print "Don't understand your answer."
            return 'observation_room' 

class MainCorridor(Scene):
    def enter(self):
        print dedent("""
        So far, you've proven yourself to be a smart cookie...
        Hopefully you keep making good decisions! Right now, you are in the 
        Main Corridor and on your way to the Escape Pod...but someone is screaming,
        and it sounds a lot like your friends in the Control Room...
        """)

        choice = raw_input(dedent("""
        > If you want to help, enter 'help'. Enter 'nah' to carry on to the Escape Pod
        """))

        if choice == 'nah':
            print dedent("""
            Here comes karma - you chose the wrong time to bail on
            your friends...sharks down the corridor are gonna get you and they say:
            """)
            return 'death'
        elif choice == 'help':
            print "Good for you, you're a good person. Here we go!"
            return 'control_room'
        else:
            print "Don't understand your answer."
            return 'main_corridor' 
            
class ControlRoom(Scene):
    def enter(self):
        print dedent("""
        Alright, you're now in the control room and you've just helped
        your friends overcome the shark that was terrorizing them. Before dying,
        however, the shark shares a dark secret - the sharks that have attacked are 
        super intelligent and want to kill the crew to steal the submarine and go
        to the surface, where they then intend to take over the world...you now have 
        a choice to make. In the Control Room, there are two doors. Behind one door 
        is a bomb that can be set to explode after you and friends all escape, but the 
        other one may just have more sharks ready to overwhelm you. The doors are labelled
        '1' and '2'. Which door do you and your friends choose?
        """)

        choice = raw_input("> Enter '1' for door 1, '2' for door 2, or 'escape' to leave.") 

        if choice == '1' or choice == '2':
            print "You chose the right door, whew! Alright, here we go..."
            return 'bomb_room'
        elif choice == 'escape':
            print dedent("""
            Ah, as soon as you open the door to escape sharks get you all...
            They're pretty mean sharks. They say: 
            """)
            return 'death'
        else: 
            print "Don't understand your answer."
            return 'control_room' 
            

class BombRoom(Scene):
    choices = ['exterminator', 'police officer', 'policeman', 'police', 'police man']
    def enter(self):
        print dedent("""
        Argh, you can't catch a break...before you can set the bomb
        to detonate at the right time, you need to solve a riddle...
        """)
        choice = raw_input("> What hired killer never goes to jail?")

        if choice in BombRoom.choices:
            print dedent("""
            Correct! The bomb is now activated to detonate AFTER you all leave,
            so you can now all escape!
            """)
            return 'escape_pod'
        else:
            print dedent("""
            Nah, you're wrong. Also, you've wasted time, so now the sharks have got 
            you cornered and they say:
            """)
            return 'death'

class EscapePod(Scene):
    def enter(self):
        print dedent("""
        Well, well, well - you've made it to the Escape Pod! But you still
        have to answer one more riddle before you can escape.
        """)

        choice = raw_input("> What has a thumb and four fingers but is not alive?")

        if choice == 'glove':
            print "Huzzah! You've made it!!! WOOOOOOOOO"
            return 'the_end'
        else:
            print "Argh, you messed up! See ya, here come sharks, they say:"
            return 'death'

class TheEnd(Scene):
    def enter(self):
        print """Thanks for playing!"""
        exit(1)