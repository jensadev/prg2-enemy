class Enemy:
    def __init__(self, name: str, health: int, attack: int, size: int, speed: int, x: int = 0, y: int = 0, color: str = "gray", outline: str = "black"):
        self.health = health
        self.attack_power = attack
        self.name = name
        self.alive = True
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.outline = outline

    @property
    def is_dead(self) -> bool:
        return not self.alive

    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def move_direction(self, direction: str, canvas_width: int, canvas_height: int):
        """Move enemy in a direction with boundary checking"""
        if direction == "up":
            self.y = max(0, self.y - self.speed)
        elif direction == "down":
            self.y = min(canvas_height - self.size, self.y + self.speed)
        elif direction == "left":
            self.x = max(0, self.x - self.speed)
        elif direction == "right":
            self.x = min(canvas_width - self.size, self.x + self.speed)

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
        print(
            f"Fiende med namnet {self.name} har {self.health} hp och är vid liv: {self.alive}")

    def check_collision(self, other: 'Enemy') -> bool:
        """Check if this enemy collides with another enemy"""
        if (self.x < other.x + other.size and
            self.x + self.size > other.x and
            self.y < other.y + other.size and
            self.y + self.size > other.y):
            return True
        return False

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



def __main__():
    slime = Enemy("Slime", 100, 5, 40, 20)
    goblin = Enemy("Goblin", 160, 10, 40, 20)
    slime.print_status()
    goblin.print_status()

    # Istället för att skriva logiken för en fight här, så kan vi flytta den till enemy också
    goblin.battle_with(slime)
