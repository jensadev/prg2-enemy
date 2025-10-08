class Enemy:
    def __init__(self, health: int, attack: int, name: str):
        self.health = health
        self.attack_power = attack
        self.name = name
        self.alive = True

    def attack(self, target: 'Enemy') -> int:
        if self.alive:
            print(f"{self.name} attackerar {target.name}")
            return self.attack_power
        else:
            print(f"{self.name} kan inte attackera eftersom den är död")
            return 0

    def take_damage(self, damage: int):
        if not self.alive:
            print("Slå inte på den som är död.")
            return
        self.health -= damage
        print(f"{self.name} tar {damage} i skada och har {self.health} i liv kvar")
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} är död!")

    def print_status(self):
        print(f"Fiende med namnet {self.name} har {self.health} hp och är vid liv: {self.alive}")

slime = Enemy(100, 5, "Slajm")
goblin = Enemy(160, 10, "Goblin")
slime.print_status()
goblin.print_status()

while slime.alive and goblin.alive:
    goblin_attack_roll = goblin.attack(slime) # nu sköter attacken skriva ut + att target tar skada
    slime.take_damage(goblin_attack_roll)
    slime_attack_roll = slime.attack(goblin)
    goblin.take_damage(slime_attack_roll)
    slime.print_status()
    goblin.print_status()
