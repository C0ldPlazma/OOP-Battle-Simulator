from enemy import Enemy
import random

class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, 500)
        self.attack_power = 25

    def attack(self):
        """Return a random amount of damage."""
        attackStyle = random.randint(1,3)
        if attackStyle == 1:
            print("FIREBAL")
            return 4 * random.randint(1,2)
        if attackStyle == 2:
            print("LASSSSRX")
            return 20
        if attackStyle == 3:
            print("Swoocsh")
            return random.randint(1, 14)

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Return True while the boss has health remaining."""
        return self.health > 0
