class Enemy:
    def __init__(self, health: int, attack: int, name: str):
        self.health = health
        self.attack_power = attack
        self.name = name

    def attack(self):
        print(f"{self.name} attackerar för {self.attack_power} skada")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} tar {damage} i skada och har {self.health} i liv kvar")

    def print_status(self):
        print(f"Fiende med namnet {self.name} har {self.health} hp")

slime = Enemy(10, 5, "Slajm")
slime.print_status()
slime.attack()
slime.take_damage(3)
