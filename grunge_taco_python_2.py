from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement"
        print " enter()."
        exit(1)


class Death(Scene):

    def enter(self):
        print "You died. Good Job!"
        exit(1)


class Kitchen(Scene):

    inventory = []
    tried_safe = False

    def enter(self):
        intro_text = self.dynamic_intro()
        print intro_text

        choice = raw_input("> ")

        if "north" in choice or "lobby" in choice:
            print "\n--------"
            print "You exit the kitchen and head back into the lobby. You"
            print "start walking towards the soda machine. A nice orange soda"
            print "would taste really good right about now. You notice that"
            print "Ray-Ray and Deshaun are no where to be seen. They must have"
            print "untied themselves while you were in the kitchen. You decide"
            print "not to worry about it. You just want to drink a nice"
            print "refreshing soda, chill out, and earn your hourly wage while"
            print "you wait for the cops arrive."
            print ""
            print "You grab an extra large cup, you add some ice, and then you"
            print "start filling it up with that delicious orange drink you've"
            print "been craving. You then start walking towards one of the"
            print "tables to sit down and enjoy your beverage when all of a"
            print "sudden the front doors to Grunge Taco swing open. You see"
            print "Ray-Ray and Deshaun and about a dozen police officers"
            print "dressed in full S.W.A.T. team gear."
            print ""
            print "\"That's the guy who did this\" says Ray-Ray pointing at"
            print "you."
            print ""
            print "You try to protest but one of the police officers yells at"
            print "you to keep quiet and to put your hands in the air. You"
            print "immediately raise your hands. You raise them so fast that"
            print "it causes the orange soda to go flying out of the cup and"
            print "into the air."
            print ""
            print "\"He's got a gun!\" yells Deshaun."
            print ""
            print "You don't have a gun, or anything that even remotely looks"
            print "like a gun. In the heat of the moment the flying ice cubes"
            print "and orange soda coupled with Deshaun's outcry must have"
            print "been enough to set off the itchy trigger fingers of the"
            print "S.W.A.T. Team. You are shot about fifty times and you and"
            print "your orange soda both die instantly."
            return 'death'
        elif "south" in choice or "back door" in choice:
            if "money" in self.inventory:
                print "\n--------"
                print "You open the back door and head into the alley. You"
                print "secure the trash bag full of cash to the rear rack of"
                print "your mountain bike with some bungee cords. Today must"
                print "be your lucky day you think to yourself. You avoided"
                print "getting slaughtered and you are now the proud owner of"
                print "a giant bag full of cash."
                print ""
                print "You jump on your bike, wave goodbye to Grunge Taco, and"
                print "ride home through the trail in the woods to your"
                print "apartment. You and your bag of money live happily ever"
                print "after. THE END."
                return None
            else:
                print "\n--------"
                print "You open the back door and head into the alley. Today"
                print "must be your lucky day you think to yourself. You"
                print "avoided getting slaughtered and you even had a nice"
                print "nap."
                print ""
                print "You jump on your bike, wave goodbye to Grunge Taco, and"
                print "begin riding home through the trail in the woods to"
                print "your apartment. You travel about 100 feet when you see"
                print "something large blocking the path so you slam on your"
                print "brakes. That something turns out to be a giant grizzly"
                print "bear. The bear stands up on its hind legs and begins"
                print "growling and waving its giant paws around. You try to"
                print "turn around and ride back Grunge Taco but the bear is"
                print "too fast for you and easily plucks you off of your bike"
                print "and slams your body repeatly on the ground like a"
                print "ragdoll until you die."
                return 'death'
        elif "safe" in choice and "money" in self.inventory:
            print "You already emptied out the safe, there's nothing more to"
            print "take."
            self.enter()
        elif "safe" in choice:
            safe_opened = self.safe_crack()
            self.tried_safe = True
            if safe_opened:
                print "\n--------"
                print "You guessed the correct combination! You open up the"
                print "safe and take out all of the money. This is the most"
                print "cash you've ever seen in your life! You place the money"
                print "in a trashbag and sling it over your shoulder. It's a"
                print "shame that your co-workers got mysteriously"
                print "slaughtered. You feel slightly bad about it but then"
                print "you think about all that cold hard cash and you feel"
                print "less bad. You're rich now!\n"""
                self.inventory.append("money")
                self.enter()
            else:
                self.enter()
        else:
            print "\n--------"
            print "you %s and it kills you" % choice
            return 'death'

    def safe_crack(self):
        is_safe_open = False
        last_digit = str(randint(0, 9))
        print "This is last digit: %s for testing purposes" % last_digit
        while not is_safe_open:
            safe_code = raw_input("Enter the 4 digit code to open the safe: ")
            if (safe_code == "138" + last_digit):
                is_safe_open = True
            else:
                print "You have entered an incorrect code"
                re_enter_code = raw_input("Would you like to try to re-enter"
                                          " the code? y or n?")
                if re_enter_code == 'y':
                    continue
                elif re_enter_code == 'n':
                    break
                else:
                    continue

        return is_safe_open

    def dynamic_intro(self):

        opt2 = """2. Head south out the back door and forget about all the
blood and guts. Forget about the money in the safe. Just quietly leave out the
back door, jump on your mountain bike, and ride home to your apartment through
the trail in the woods behind Grunge Taco."""

        opt3 = """3. Try to open the safe by guessing the last number of the
4 digit pin code and get rich quick after stealing all that Grunge Taco money.
With all the blood, hostages, and deep fried severed hands, no one is going to
suspect that you stole the money out of the safe. They will just add an
additional theft charge to whoever destroyed the place while you were sleeping.
"""

        if "money" not in self.inventory and not self.tried_safe:

            intro = """You enter the Grunge Taco kitchen. There's blood
splattered everywhere. There's blood in the sour cream station, blood on the
Grunge Taco take-out bags, and there appears to be a severed human hand in the
deep fryer basket.

How did you manage to sleep through this masacre? You wonder to yourself.

At this point you just want to go home. This is too much to handle. As you
look around the room at all the blood and guts your eyes land on the Grunge
Taco safe. It's Friday and there's a whole weeks worth of money in that safe.
Usually you aren't allowed to touch the safe. You are only the assistant
manager. The manager, Phil, who may not even still be alive, is the only person
who has full access to the safe. But Phil has a habit of thinking out loud.
You've heard him mumbling the 4 digit pin number but you are only sure of the
first three numbers. 1 3 8. You were never able to make out the last number."""

        elif "money" not in self.inventory and self.tried_safe:

            intro = "You are still in the Grunge Taco kitchen."

            opt3 = "3. Try to open the safe again" + opt3[23:]

        elif "money" in self.inventory:
            intro = """You are still in the Grunge Taco kitchen. But now you
are rich!"""

            opt2 = opt2[:73] + opt2[109:-1] + " and spend the rest of the\
night counting all your money!"

            opt3 = ""

        dynamic_intro = """
%s

You need to decide your next move. You only have a few options:

1. Head north and go back into the Grunge Taco lobby, pour yourself a large
orange soda from the soda machine, and wait for the police to show up and sort
out this mess. You are technically still on the clock, so you might as get paid
to chill out rather than punch out and go home.

%s

%s

""" % (intro, opt2, opt3)

        return dynamic_intro


class Lobby(Scene):

    def enter(self):
        print "You exit the restroom and enter the main lobby area of Grunge"
        print "Taco. Someone has blacked out all the windows with industrial"
        print "strength garbage bags and duct tape. With this new set-up, you"
        print "can't see out, and no one can see in."
        print ""
        print "You see two of your co-workers, Ray-Ray and Deshaun,"
        print "blindfolded and tied to the soda-fountain machine. They both"
        print "appear to have blood stains on their Grunge Taco uniforms. To"
        print "the east is the exit to the front parking lot, to the south is"
        print "the Grunge Taco kitchen area, To the north is the Grunge taco"
        print "Restroom that you just came out of."
        print ""
        print "This situation seems to be getting weirder by the moment. You"
        print "try to plan your next move. You don't have many options:"
        print ""
        print "1. Head north, go back into the restroom, and go back to sleep."
        print "You can just go hide and hope that everything will work itself"
        print "out while you catch some zzzz's"
        print ""
        print "2. Head east, go outside through the front door, get on your"
        print "bike, ride home, and start applying for a new job. It sure"
        print "would be nice to have a job that involved less blood and less"
        print "hostages than your current place of employment."
        print ""
        print "3. Head south into the Grunge Taco kitchen to further assess"
        print "the situation."
        print ""
        print "4. Untie Deshaun and Ray-Ray. Maybe they can fill you in on"
        print "what has happened and help you save the day."

        choice = raw_input("> ")

        if "north" in choice or "restroom" in choice:
            print "\n--------"
            print "You decide that this situation is way out of the realm of"
            print "your job discription and pay grade. You go back into the"
            print "restroom to hide in the handicapped stall and sleep."
            print ""
            print "You figure that this will all just blow over. It's best not"
            print "to get involved."
            print ""
            print "You open the door to the stall and lay down. You close your"
            print "eyes and are about to catch some ZZZZ's when all of a"
            print "sudden you hear a faint creaking noise. You try to ignore"
            print "it but it keeps getting louder."
            print ""
            print "You open your eyes to see what's causing this loud racket."
            print "You look up and see that the restroom's drop ceiling"
            print "appears to be moving. The next thing you know the ceiling"
            print "breaks open and a large fat man, wearing a nothing but a"
            print "Hawaiian Lei and grass skirt, falls on top of you killing"
            print "you instantly."
            return 'death'
        elif "east" in choice or "outside" in choice:
            print "\n--------"
            print "You decide you've had enough of Grunge Taco."
            print ""
            print "\"I Quit!\" you yell out loud to no one in particular."
            print ""
            print "It feels good to say those words. You feel reborn. You feel"
            print "free. Nothing is going to stop you now! You're gonna do it!"
            print ""
            print "You march out the front door into the Grunge Taco parking"
            print "lot. Everything is going to be better from now on. You"
            print "start walking to go get your bike from the back alleyway."
            print "As you are walking you notice a small red dot on your"
            print "chest. You try to flick it off but it won't budge."
            print "Suddenly, about a dozen more tiny red dots appear on your"
            print "body."
            print ""
            print "You look around and see that an entire S.W.A.T. team has"
            print "you surrounded. The S.W.A.T. team's trained snipers are all"
            print "pointing their riffles right at you."
            print ""
            print "You try to say \"What's this all about? Why are you"
            print "pointing guns at me?\""
            print ""
            print "But you only are able to utter the syllable \"Wha...\""
            print "before you are shot to death about 50 times."
            return 'death'
        elif "south" in choice or "kitchen" in choice:
            return 'kitchen'
        elif "untie" in choice:
            print "\n--------"
            print "You decide to help Ray-Ray and Deshaun. Hopefully they will"
            print "be able to explain what happened while you were sleeping in"
            print "the restroom. You quickly untie both of them and remove"
            print "their blindfolds."
            print ""
            print "\"Guys, why are you tied up? Why is there blood splattered"
            print "everywhere?\" You ask."
            print ""
            print "\"What you mean who tied us up?\" Says Ray-Ray"
            print ""
            print "\"You the fool who tied us up! And now we gonna kill you!\""
            print "says Deshaun."
            print ""
            print "You try to protest but neither of the men will listen to"
            print "you. They are completely convinced that you are the one who"
            print "tied them up. You try to fight back but they overpower you"
            print "and tie you to the soda-fountain machine. They then leave"
            print "you and head into the kitchen."
            print ""
            print "You decide to just remain calm. The police will eventually"
            print "show up and sort this whole thing out. The Grunge Taco"
            print "surveillance camera footage will show everyone that you"
            print "were in the restroom the whole time. It will prove your"
            print "innocence to Ray-Ray and Deshaun and you will all have a"
            print "nice big laugh about it all. So you just chill out and try"
            print "to get comfortable while you wait."
            print ""
            print "Ray-Ray and Deshaun soon emerge from the kitchen. Ray-Ray"
            print "has a large plastic funnel. Deshaun has a roll of duct"
            print "tape."
            print ""
            print "\"Hey guys... what are you going to do with that stuff?\""
            print "you nervously ask."
            print ""
            print "Neither one of them utters a word. They begin duct tapping"
            print "the funnel to your mouth. Next they position you under the"
            print "orange soda dispenser on the soda fountain."
            print ""
            print "Deshaun uses some duct tape to keep the orange soda flowing"
            print "into the funnel and down your throat. The two men exit the"
            print "building and leave you to die."
            print ""
            print "Death by drowning."
            print ""
            print "Death by Orange Soda."
            return 'death'
        else:
            print "\n--------"
            print "You decide to %s. You've always been good at" % choice
            print "%s-ing. So you just %s over and over." % (choice, choice)
            print " Suddenly you feel a sharp shooting pain in your abdomin."
            print "You must have %s-ed too hard this time. You" % choice
            print "double over in excruciating pain. You then die on the floor"
            print "of the Grunge Taco lobby."
            print ""
            print "Next time, if there is a next time, you might want to only"
            print "%s in moderation" % choice
            return 'death'


class Restroom(Scene):

    def enter(self):
        print "You wake up in the handicapped restroom stall of Grunge Taco."
        print "Grunge Taco is a 1990's themed fast food restaurant chain. You"
        print "work here as the assistant manager. This large handicapped"
        print "stall is a perfect hiding place to avoid work and to take"
        print "naps. You've taken many naps in this stall. Waking up in here"
        print "is not very unusual. What is unusual is that when you exit the"
        print "stall you see what appears to be blood splattered all over the"
        print "walls, floor, and ceiling."
        print ""
        print "You quickly look around the room and try to plan your next"
        print "move. You don't have many options."
        print "You can either:"
        print ""
        print "1. Go back in the stall, go back to sleep, and hope this is"
        print "all just a bad dream or some weird hallucination caused by the"
        print "Grunge Taco MUCHO Extreme-O Burrito you ate for lunch."
        print ""
        print "2. Search the restroom storage closet for something to protect"
        print "yourself with."
        print ""
        print "3. Leave the restroom and go into the restaurant lobby area."
        print "Hopefully one of your co-workers will be there and will be"
        print "able to explain why the restroom is covered in blood."

        choice = raw_input("> ")

        if "stall" in choice:
            print "\n--------"
            print "You decide the best course of action in this situation is"
            print "no action at all. You retreat back to your bathroom stall"
            print "hideaway. You lay down on the floor of the stall and close"
            print "your eyes. This is all just a bad dream. When you wake up"
            print "everything will be back to normal. You start to doze off."
            print "Suddenly you hear a loud explosion. You open your eyes and"
            print "the last thing you see is blindingly bright white light."
            print ""
            print "What happened? Did a bomb go off?"
            print ""
            print "Whatever happened killed you so at this point the fact that"
            print "you are dead is preventing you from doing any indepth"
            print "analysis or further investigation of the matter."
            return 'death'
        elif "closet" in choice:
            print "\n--------"
            print "Action movies have taught you that if you ever find"
            print "yourself in a crazy situation, like waking up in a"
            print "blood-splattered fast food restroom, the first thing you"
            print "should do is arm yourself with some kind of ridiculous"
            print "handmade weapon fashioned from random objects in your"
            print "immediate surroundings."
            print ""
            print "You begin to imagine yourself building a poisonous blow"
            print "dart device out of cardboard toilet paper tubes, bristles"
            print "from a toilet scrubber brush, and the mysterious \"blue\""
            print "brand of Grunge Taco all-purpose cleaner. You are sure that"
            print "the restroom storage closet will give you all you need to"
            print "become an action hero and save the day."
            print ""
            print "You open the door to the closet with your employee key. It"
            print "is completely dark inside the closet. As you are fumbling"
            print "around for the light switch you suddenly feel a stabbing"
            print "pain in your stomach. You flip the light on and see that"
            print "you have been stabbed with a plastic spork that has been"
            print "sharpenend into a primative spear."
            print ""
            print "The person who stabbed you is your co-worker Traynesha. As"
            print "you bleed to death in excrutiating pain you manage to utter"
            print "the word \"WHY??\"."
            print "Traynesha says nothing and then stabs you a second time,"
            print "this time in the jugular. You quickly bleed to death and"
            print "die."
            return 'death'
        elif "leave" in choice:
            return 'lobby'
        else:
            print "\n--------"
            print "You try to %s and that seems to be the right" % choice
            print "choice. You just keep %s-ing and %s-ing." % (choice, choice)
            print "You never realized how wonderful %s-ing could be." % choice
            print "But then suddenly you develop a deadly allergy to"
            print "%s. You try to scream but your throat closes up." % choice
            print " You try to dial 911 but your phone battery is dead from"
            print "all the %s-ing you were doing. You soon die from" % choice
            print "acute %s poisoning." % choice
            return 'death'


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True and current_scene is not None:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Map(object):

    scenes = {
        'restroom': Restroom(),
        'lobby': Lobby(),
        'kitchen': Kitchen(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('restroom')
a_game = Engine(a_map)
a_game.play()
