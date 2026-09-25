from goblin import Goblin
from hero import Hero
from boss import Boss


ARENA_NAME = "Balcony of Restless Whimsy"
JIM = Hero('Jimithy')


def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} has abused the poor thing to literal death.")
    else:
        print(f"{enemy.name}, the helpless creature puts the arrogant and horrible being in it's pathetic place.")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gibblegobel")
    goblin2 = Goblin("Scribble")

    print(f"{goblin.name} and {goblin2.name} enter the arena with {goblin.health} and {goblin2.health} health.")
    print("But no hero has answered the call... yet.")
    print(f"And then the great, noble, awe inspiring humanoid thing {JIM.name} arives out of plot convinience!")
    print(f"This being claims that he is of the {JIM.role} class.")
    print(f"And the great benevolant being chooses violence, striking at {goblin.name}...")
    battle(JIM, goblin)

    boss = Boss("Martha")
    print("Martha falls off of an airplane and falls onto the field.")
    battle(JIM, boss)


if __name__ == "__main__":
    main()
