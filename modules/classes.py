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