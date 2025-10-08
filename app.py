class Enemy:
    def __init__(self, health: int, attack: int, name: str, x: int = 0, y: int = 0):
        self.health = health
        self.attack_power = attack
        self.name = name
        self.alive = True
        self.x = x
        self.y = y

    @property
    def is_dead(self) -> bool:
        return not self.alive

    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def attack(self, target: 'Enemy') -> int:
        if self.is_dead:
            print(f"{self.name} kan inte attackera eftersom den är död")
            return 0

        print(f"{self.name} attackerar {target.name}")
        return self.attack_power

    def take_damage(self, damage: int):
        if self.is_dead:
            print("Slå inte på den som är död.")
            return

        self.health -= damage
        print(f"{self.name} tar {damage} i skada och har {self.health} i liv kvar")
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} är död!")

    def print_status(self):
        print(f"Fiende med namnet {self.name} har {self.health} hp och är vid liv: {self.alive}")

    def battle_with(self, enemy: 'Enemy'):
        """Conduct a battle between this enemy and another enemy"""
        while self.alive and enemy.alive:
            # This enemy attacks
            damage = self.attack(enemy)
            enemy.take_damage(damage)

            # Other enemy attacks back (if still alive)
            if enemy.alive:
                damage = enemy.attack(self)
                self.take_damage(damage)

            # Show status after each round
            self.print_status()
            enemy.print_status()
            print("-" * 30)


slime = Enemy(100, 5, "Slajm")
goblin = Enemy(160, 10, "Goblin")
slime.print_status()
goblin.print_status()

# Istället för att skriva logiken för en fight här, så kan vi flytta den till enemy också
goblin.battle_with(slime)
