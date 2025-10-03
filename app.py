class Enemy:
    def __init__(self, health: int, attack: int, name: str):
        self.health = health
        self.attack_power = attack
        self.name = name

    def attack(self, target: 'Enemy'):
        print(f"{self.name} attackerar {target.name}")
        target.take_damage(self.attack_power) # Var ska detta ske och vem äger den biten

    def take_damage(self, damage: int):
        self.health -= damage
        print(f"{self.name} tar {damage} i skada och har {self.health} i liv kvar")

    def print_status(self):
        print(f"Fiende med namnet {self.name} har {self.health} hp")

slime = Enemy(10, 5, "Slajm")
goblin = Enemy(20, 10, "Goblin")
slime.print_status()
goblin.print_status()

# Hur ska vi göra här för att få goblin att attackera slime?
goblin.attack(slime) # nu sköter attacken skriva ut + att target tar skada
# slime.take_damage(goblin.attack_power)
slime.print_status()
