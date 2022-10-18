import random
from modules.logos import *
# Char Class


class Char:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.score = 0
        self.count = 0


humans = Char("Humans", 400, 150)
greys = Char("Greys", 600, 80)
martians = Char("Martians", 900, 200)
pleiadeans = Char("Pleiadeans", 1200, 300)

# Vessel Class


class Vessel:
    def __init__(self, name, hp, damage, speed):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed


tie_fighter = Vessel("Tie-Fighter", 800, 50, 800)
millienum_falcon = Vessel("Millienum Falcon", 2000, 150, 1500)
voyager = Vessel("Voyager", 3000, 300, 500)
serenity = Vessel("serenity", 1200, 100, 1200)

# Monster Class


class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

space_monster_lrg = Monster("Hedorah", 3000, 120)
space_monster_sml = Monster("Xenomorph", 1000, 75,)

def hud():
    print(f"""
                                                                                                        **___---HUD---___**
                                                                                                        Race:{character.name}
                                                                                                        Health :{character.hp}

                                                                                                        Ship: {vessel.name}
                                                                                                        Shields: {vessel.hp}
                                                                                                        Phasers: {vessel.damage}""")

# character Selection
while True:
    main_logo()
    choice = input("""
                                                    Choose your Race or Exit: """)
    if choice == "1" or str.lower(choice) == str.lower("humans"):
        character = humans

        human_logo()
        break
    elif choice == "2" or str.lower(choice) == str.lower("greys"):
        character = greys

        grey_logo()
        break
    elif choice == "3" or str.lower(choice) == str.lower("martians"):
        character = martians

        martian_logo()
        break
    elif choice == "4" or str.lower(choice) == str.lower("pleiadeans"):
        character = pleiadeans
        
        pleiadean_logo()
        break
    elif choice == "5" or str.lower(choice) == str.lower("exit"):
        exit()
    else:
        print("Unknown character")
        continue
print(f"""
                                        Congratulations! you have chosen to play as: {character.name}
                                                           Health: {character.hp}
                                                           Damage: {character.damage}
""")


# Vessel Selection

while True:
    ship()
    choice2 = input("""                                   
                                                  Choose your Vessel, flyboy: """)
    if choice2 == "1" or str.lower(choice2) == str.lower("tie-fighter"):
        vessel = tie_fighter
        break
    elif choice2 == "2" or str.lower(choice2) == str.lower("millienum falcon"):
        vessel = millienum_falcon
        break
    elif choice2 == "3" or str.lower(choice2) == str.lower("voyager"):
        vessel = voyager
        break
    elif choice2 == "4" or str.lower(choice2) == str.lower("Serenity"):
        vessel = serenity
        break
    elif choice2 == "5" or str.lower(choice2) == str.lower("exit"):
        exit()
    else:
        print("Unknown character")
        continue
    
# ship_choice()
print(f"""
                                        Congratulations! you have chosen to fly: {vessel.name}
                                                            Sheild: {vessel.hp}
                                                            Damage: {vessel.damage}""")
starmap()

# Game Start

bosses = [space_monster_lrg, space_monster_sml,
                  space_monster_sml, space_monster_sml]
while True:

    if character.name == "Humans":
        human_mission()
        break
    elif character.name == "Greys":
        grey_mission()
        break
    elif character.name == "Martians":
        martian_mission()
        break
    elif character.name == "Pleiadeans":
        pleiadean_mission()
        break
    else:
        # game_resuls()
        break

mission_obj = input("""
                                            Do you accept your mission:
                                            1) Yes
                                            2) Hell no, Im outta here
                                            Your Response:""")
                        
while True:
    if mission_obj == "1" or str.lower(mission_obj) == str.lower("yes"):
        print()
        break
    else:
        exit()

while True:
    req_turns = random.randint(8, 12)
    events = ["battle", "collect", "loss", "bonus", "collect", "loss", "bonus"]
    bonus_events = [
        "You pass through an intense electrical storm. To your suprise the the additional energy has boasted your shields and phasers",
        "You get sucked into a wormhole. Luckily it spits you out further along the path you were already on with a boost in shields!",
        "You have recovered the dark matter, Our race is saved!!!"]
    collect_events = [
        "You have come across an abandonded ship. You loot its contents for extra food and medicine.",
        "You find a nearby astorid to mine for supplies",
        "You find an abandoned space station, after boarding and checking for survivors you loot the remaining supplies"
    ]

    loss_events = [
        "You have been ambushed, the attackers snuck onto your ship, stole your supplies and damaged your hull.",
        "You get caught in a meotorite shower, well dangerously beautiful. Your ship and your crew take a beating",
        "Oh no! You have caught coronavirus from the Omicronians when you stopped to give their ship a jump on the Milky Way Express"
        ]


    turn = random.choice(events)
    if turn == "collect":
        character.hp += 200
        collect = random.choice(collect_events)
        character.count += 1
        print()
        print("Zoom Zoom.....Zoom Zoom.... Zoom Zoom....")
        print(collect)
        print("Health: + 200")
        hud()
        x = input("Press Enter")
        print()
    elif turn == "loss":
        character.hp -= 80
        vessel.hp -= 500
        character.count += 1
        character.score = character.hp
        loss = random.choice(loss_events)
        print("Zoom Zoom.....Zoom Zoom.... Zoom Zoom....")
        print(loss)
        print("Health: -80")
        print("Shields: -500")
        hud()
        if character.hp <= 0:
            print(f"""
                              Final Score: {character.score}
                        Your Health is failing, you have fallen ill
                            You have died of space dysynteria...
                                          Game Over""")
            exit()
        elif vessel.hp <= 0:
            print(f"""
                                     Final Score: {character.score}
                                Your Ship has been destroyed 
                                        Game Over""")
            exit()
        x = input("Press Enter")
        print()
    elif turn == "bonus":
        bonus = random.choice(bonus_events)
    
        
        if bonus == "You have recovered the dark matter, Our race is saved!!!":
            if character.count >= req_turns:
                character.score = (character.hp + vessel.hp + 20000)
                print()
                print(bonus)
                hud()
                print(f"""                                      
                                                Final Score: {character.score}
                                                            
                                                        Game Over
                """)
                exit()
            else:
                bonus2 = random.choice(bonus_events)
                if bonus2 != "You have recovered the dark matter, Our race is saved!!!":
                    character.count += 1
                    vessel.damage += 200
                    vessel.hp += 500
                    print()
                    print("Zoom Zoom.....Zoom Zoom.... Zoom Zoom....")
                    print(bonus2)
                    print("Shields: +500")
                    print("Phasers: + 200")
                    hud()
                    x = input("Press Enter")
                    print()
    elif turn == "battle":
        character.count += 1
        bosses = [space_monster_lrg, space_monster_sml,
                  space_monster_sml, space_monster_sml]
        boss = random.choice(bosses)
        if boss == space_monster_sml:
            print(f"""                     
                                    You have come across the dreaded Xenomorph's
                                      Better call Ripley for some assistance...
            """)
        elif boss == space_monster_lrg:
            print("""                                    
                                      You have run across the dreaded Hedorah
                                       Where is Godzilla when you need him...
            """)
        choice3 = input("""                                              
                                            Attempt to run or fight??
                                                   1) Run
                                                   2) Fight
                                                   Answer:""")
        if choice3 == "1" or str.lower(choice3) == str.lower("run"):
            if vessel.speed > 200:
                print("""
                                          You have escaped this time...
                                    "Zoom Zoom.....Zoom Zoom.... Zoom Zoom....")
                """)
                vessel.speed -= 200
                continue
            elif vessel.speed < 200:
                                print("""
                                          Not enough Fuel to outrun them....
                                             Get Ready for a Fight!!!
                """)
        while vessel.hp > 0:
            if boss.hp > 0:
                print(f"""{boss.name}'s: {boss.hp} hp""")
                boss.hp -= vessel.damage
                print(f"""The {character.name} damaged the {boss.name}!""")
                print(f"The {boss.name}s hitpoints are now: "+str(boss.hp))
                print()
            if boss.hp <= 0:
                print(f"The {boss.name} have lost the battle")
                x = input("Press Enter")
                print("Zoom Zoom.....Zoom Zoom.... Zoom Zoom....")
                space_monster_lrg = Monster("Hedorah", 10000, 500)
                space_monster_sml = Monster("Xenomorph", 5000, 250,)
                break
            elif vessel.hp >= 0:
                vessel.hp -= boss.damage
                print(
                    f"""The {boss.name}s strikes back at {character.name}'s""")
                print(f"""{vessel.name}'s hitpoints are now: """ +
                      str(vessel.hp))
                print()
                if vessel.hp <= 0:
                    character.score = character.hp
                    print(f""" 
                                         {character.name} have lost the battle"
                                              All hope is lost!!!
                                                Score: {character.score}
                                          Sorry you failed the mission...
                                                   Game Over""")
                    exit()

# Char Class Tests
# print(humans.name)
# print(humans.hp)
# print(humans.damage)

# print(greys.name)
# print(greys.hp)
# print(greys.damage)

# print(martians.name)
# print(martians.hp)
# print(martians.damage)

# print(pleiadeans.name)
# print(pleiadeans.hp)
# print(pleiadeans.damage)

# Vessel Class Tests
# print(tie_fighter.name)
# print(tie_fighter.hp)
# print(tie_fighter.damage)
# print(tie_fighter.speed)

# print(millienum_falcon.name)
# print(millienum_falcon.hp)
# print(millienum_falcon.damage)
# print(millienum_falcon.speed)

# print(voyager.name)
# print(voyager.hp)
# print(voyager.damage)
# print(voyager.speed)

# print(serenity.name)
# print(serenity.hp)
# print(serenity.damage)
# print(serenity.speed)

# Monster Class Tests

# print(space_monster_lrg.name)
# print(space_monster_lrg.hp)
# print(space_monster_lrg.damage)

# print(space_monster_sml.name)
# print(space_monster_sml.hp)
# print(space_monster_sml.damage)


# def travel():
#     print(f"{character.name}")
#     # global character.hp
#     # print(character.hp)

# travel()
