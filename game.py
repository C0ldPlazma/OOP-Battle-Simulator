from goblin import Goblin


ARENA_NAME = "Balcony of Restless Whimsy"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gibblegobel")
    goblin2 = Goblin("Scribble")

    print(f"{goblin.name} and {goblin2.name} enter the arena with {goblin.health} and {goblin2.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
