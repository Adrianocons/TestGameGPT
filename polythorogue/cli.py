from .game import Game


def main() -> None:
    game = Game()
    print(game.render())
    for _ in range(5):
        game.step()
        print()
        print(game.render())

if __name__ == '__main__':
    main()
