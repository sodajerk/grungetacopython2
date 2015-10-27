from sys import exit
from random import randint
import content


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement"
        print " enter()."
        exit(1)

    def dialog(self, t):
        print "\n--------"
        print t


class Death(Scene):

    def enter(self):
        print "\nYou died. Good Job!"
        exit(1)


class Kitchen(Scene):

    inventory = []
    tried_safe = False

    def enter(self):
        intro_text = content.KitchenTexts()
        self.dialog(intro_text.dynamic_intro(self.inventory, self.tried_safe))

        choice = raw_input("> ")

        if "north" in choice or "lobby" in choice:
            self.dialog(content.KitchenTexts.north)
            return 'death'
        elif "south" in choice or "back door" in choice:
            if "money" in self.inventory:
                self.dialog(content.KitchenTexts.south_win)
                return None
            else:
                self.dialog(content.KitchenTexts.south_lose)
                return 'death'
        elif "safe" in choice and "money" in self.inventory:
            self.dialog(content.KitchenTexts.safe_already_empty)
            self.enter()
        elif "safe" in choice:
            safe_opened = self.safe_crack()
            self.tried_safe = True
            if safe_opened:
                self.dialog(content.KitchenTexts.safe_open_text)
                self.inventory.append("money")
                self.enter()
            else:
                self.enter()
        else:
            self.dialog(content.KitchenTexts.default.format(choice))
            return 'death'

    def safe_crack(self):
        is_safe_open = False
        last_digit = str(randint(0, 9))
        # uncomment the line below to see the safe code solution
        # print "This is last digit: %s for testing purposes" % last_digit
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


class Lobby(Scene):

    def enter(self):
        self.dialog(content.LobbyTexts.enter)

        choice = raw_input("> ")

        if "north" in choice or "restroom" in choice:
            self.dialog(content.LobbyTexts.north)
            return 'death'
        elif "east" in choice or "outside" in choice:
            self.dialog(content.LobbyTexts.east)
            return 'death'
        elif "south" in choice or "kitchen" in choice:
            return 'kitchen'
        elif "untie" in choice:
            self.dialog(content.LobbyTexts.untie)
            return 'death'
        else:
            self.dialog(content.LobbyTexts.default.format(choice))
            return 'death'


class Restroom(Scene):

    def enter(self):
        self.dialog(content.RestroomTexts.enter)
        choice = raw_input("> ")

        if "stall" in choice:
            self.dialog(content.RestroomTexts.stall)
            return 'death'
        elif "closet" in choice:
            self.dialog(content.RestroomTexts.closet)
            return 'death'
        elif "leave" in choice:
            return 'lobby'
        else:
            self.dialog(content.RestroomTexts.default.format(choice))
            return 'death'


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True and current_scene is not None:
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
