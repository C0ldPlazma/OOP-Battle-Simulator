from goblin import Goblin
from hero import Hero


ARENA_NAME = "Balcony of Restless Whimsy"
Hero = Hero('Jimithy')


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gibblegobel")
    goblin2 = Goblin("Scribble")

    print(f"{goblin.name} and {goblin2.name} enter the arena with {goblin.health} and {goblin2.health} health.")
    print("But no hero has answered the call... yet.")
    print(f"And then the great, noble, awe inspiring humanoid thing {Hero.name} arives out of plot convinience!")
    print(f"This being claims that he is of the {Hero.role} class.")
    print(f"And the great benevolant being chooses violence, striking at {goblin.name}...")
    goblin.take_damage(Hero.attack())


if __name__ == "__main__":
    main()
