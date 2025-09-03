import pygame
from .game import Game

TILE_SIZE = 48
INFO_HEIGHT = 40


def build_tiles() -> dict[str, pygame.Surface]:
    land = pygame.Surface((TILE_SIZE, TILE_SIZE))
    land.fill((34, 139, 34))
    for i in range(0, TILE_SIZE, 8):
        pygame.draw.line(land, (0, 100, 0), (i, 0), (i, TILE_SIZE))

    water = pygame.Surface((TILE_SIZE, TILE_SIZE))
    water.fill((65, 105, 225))
    for i in range(0, TILE_SIZE, 4):
        pygame.draw.line(water, (100, 149, 237), (0, i), (TILE_SIZE, i))

    village = land.copy()
    pygame.draw.rect(
        village,
        (205, 133, 63),
        (TILE_SIZE // 4, TILE_SIZE // 4, TILE_SIZE // 2, TILE_SIZE // 2),
    )

    return {"land": land, "water": water, "village": village}


def build_units() -> dict[str, pygame.Surface]:
    player = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
    pygame.draw.polygon(
        player,
        (255, 215, 0),
        [
            (TILE_SIZE / 2, 0),
            (TILE_SIZE * 0.62, TILE_SIZE * 0.38),
            (TILE_SIZE, TILE_SIZE * 0.38),
            (TILE_SIZE * 0.69, TILE_SIZE * 0.62),
            (TILE_SIZE * 0.81, TILE_SIZE),
            (TILE_SIZE / 2, TILE_SIZE * 0.76),
            (TILE_SIZE * 0.19, TILE_SIZE),
            (TILE_SIZE * 0.31, TILE_SIZE * 0.62),
            (0, TILE_SIZE * 0.38),
            (TILE_SIZE * 0.38, TILE_SIZE * 0.38),
        ],
    )

    enemy = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
    pygame.draw.polygon(enemy, (220, 20, 60), [(TILE_SIZE / 2, 0), (TILE_SIZE, TILE_SIZE), (0, TILE_SIZE)])

    return {"player": player, "enemy": enemy}


def draw_map(surface: pygame.Surface, game: Game, tiles: dict, units: dict) -> None:
    for y in range(game.map.height):
        for x in range(game.map.width):
            tile = game.map.get_tile(x, y)
            img = tiles["land"] if tile.terrain == "land" else tiles["water"]
            if tile.village:
                img = tiles["village"]
            surface.blit(img, (x * TILE_SIZE, y * TILE_SIZE))
            if tile.unit:
                key = "player" if tile.unit.player == 0 else "enemy"
                surface.blit(units[key], (x * TILE_SIZE, y * TILE_SIZE))


def main() -> None:
    pygame.init()
    game = Game(players=2)
    tiles = build_tiles()
    units = build_units()
    width, height = game.map.width * TILE_SIZE, game.map.height * TILE_SIZE + INFO_HEIGHT
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Polythorogue")
    font = pygame.font.Font(None, 24)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if game.game_over:
                    if event.key == pygame.K_r:
                        game = Game(players=2)
                else:
                    if event.key == pygame.K_UP:
                        game.move_player(0, -1)
                    elif event.key == pygame.K_DOWN:
                        game.move_player(0, 1)
                    elif event.key == pygame.K_LEFT:
                        game.move_player(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        game.move_player(1, 0)

        draw_map(screen, game, tiles, units)
        pygame.draw.rect(
            screen,
            (30, 30, 30),
            (0, game.map.height * TILE_SIZE, width, INFO_HEIGHT),
        )
        if game.game_over:
            msg = f"{game.message} Press R to restart."
        else:
            msg = "Arrows: move  |  Reach the village, avoid the enemy."
        text = font.render(msg, True, (255, 255, 255))
        screen.blit(text, (10, game.map.height * TILE_SIZE + 10))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

